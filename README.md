# Groenmaker

A command-line tool to interact with [try](https://treeherder.mozilla.org/jobs?repo=try) and [mozilla-central](https://treeherder.mozilla.org/jobs?repo=mozilla-central) pushes.


## Installation
This tool requires pipenv to be installed as a pip package:
```
python3 -m pip install pipenv
```

Once you have pipenv installed, install groenmaker's dependencies from the root directory of the groenmaker repo:
```
pipenv install
```

Finally, enter the virtual environment created by pipenv:
```
pipenv shell
```

## Usage
In order to see the usage, simply run `./groenmaker --help`, and you'll see the most up-to-date help doc, e.g.:
```
./groenmaker --help
groenmaker.

Usage:
    groenmaker compare <try_push> <central_push>
    groenmaker run -c <commit_hash> -q <fuzzy_query> [--leading-quote] [--fix]

Options:
    -h --help           Show this screen.
    -v --version        Show the groenmaker version.
    -q --query          Specify a fuzzy query for the mach tool
    -l --leading-quote  Add a leading single-quote to the mach fuzzy query
    -c --commit         Specify a Mercurial commit hash
    --fix               Run iteratively until all failing tests are disabled
```
