import os
import pathlib
import shlex
import subprocess
import tomllib
from tomllib import TOMLDecodeError

import pexpect
from loguru import logger


def locate_groenmaker_config():
    """Find the groenmaker config (toml) file and set default values.

    This function also allows you to set the groenmaker config file's path.
    You just need to set the environment variable $GROENMAKER_CONFIG_PATH
    to an absolute or relative path pointing at the config file itself."""
    config = "~/.config/groenmaker.conf"
    custom = os.environ.get("GROENMAKER_CONFIG_PATH", None)
    if custom:
        if os.path.exists(custom):
            config = custom
    config_path = pathlib.Path(config).expanduser().absolute()
    return config_path


def read_groenmaker_config(config_path):
    """Read the config values from the config_path."""
    try:
        with open(config_path, "r") as cfg:
            config = cfg.read()
            config_t = tomllib.loads(config)
            return config_t
    except FileNotFoundError:
        raise SystemExit(f"groenmaker config file {config_path} does not exist.")
    except TOMLDecodeError as tde:
        e = f"groenmaker config file was malformed, raised toml error:\n{tde}"
        raise SystemExit(e)


def check_hg_installed():
    """Verify that hg is installed, otherwise raise SystemExit."""
    command = "/usr/bin/which hg"
    cmd = shlex.split(command)
    run = subprocess.run(cmd, capture_output=True)
    if run.returncode == 0:
        # No need to check stdout because returncode will be 1 if hg is missing
        return True
    else:
        return False


def ensure_mc_cloned(groenmaker_config):
    """Using groenmaker.conf, ensure the mozilla-central hg repo is cloned."""
    try:
        mc_dir = groenmaker_config["mozilla-central"]["repo"]
    except KeyError:
        e = "The groenmaker.conf file did not contain a [mozilla-central] header"
        e += ' with a "repo" key.'
        raise SystemExit(e)

    if os.path.exists(mc_dir):
        logger.info(f"mozilla-central dir exists at path: {mc_dir}")
    else:
        logger.info(f"mozilla-central dir does not exist at path: {mc_dir}")
        clone_answer = (
            input("Clone mozilla-central to this location now? [y/N]", end="")
            .lower()
            .strip()
        )
        if clone_answer == "y" or clone_answer == "yes":
            clone_mozilla_central(mc_dir)
        else:
            raise SystemExit("mozilla-central dir doesn't exist. Exiting.")


def clone_mozilla_central(mc_dir):
    """Use Mercurial to clone mozilla-central to `mc_dir`."""
    pass


def main():
    groenmaker_config_path = locate_groenmaker_config()
    groenmaker_config = read_groenmaker_config(groenmaker_config_path)
    logger.info(groenmaker_config)
    ensure_mc_cloned(groenmaker_config)

    # child = pexpect.spawnu("./mach vcs-setup")
    # child.expect("To begin, press the enter/return key.")
    # child.sendline("")
    # logger.info(child.before)


if __name__ == "__main__":
    main()
