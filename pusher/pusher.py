import shlex
import subprocess


def run(shell_cmd):
    """Run a Linux shell command with subprocess.

       Return a three-tuple with (returncode, stdout, stderr)."""
    cmd = shlex.split(shell_cmd)
    result = subprocess.run(cmd, capture_output=True)
    return (result.returncode, result.stdout, result.stderr)
