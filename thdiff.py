#!/usr/bin/env python3
import sys

from mozci.push import Push


def thdiff(commit_mc, commit_try):
    """Given one ref from central and one from try, show failures in try."""
    relevant_failures = []
    central = Push(commit_mc, branch="mozilla-central")
    _try = Push(commit_try, branch="try")

    central_tasks = set([x.label for x in central.tasks])
    try_tasks = set([x.label for x in _try.tasks])
    both = set.intersection(central_tasks, try_tasks)

    for task in _try.tasks:
        if task.label in both and task.failed:
            relevant_failures.append(task)

    print("Tasks failed in both try and central:")
    if relevant_failures:
        print("\n".join(list(set([t.label for t in relevant_failures]))))
    else:
        print("    Found 0 tasks that failed in both try and central.")


def usage():
    usage_str = "USAGE: thdiff <CENTRAL_COMMIT_HASH> <TRY_COMMIT_HASH>"
    raise SystemExit(usage_str)


def main():
    try:
        commit_mc = sys.argv[1]
        commit_try = sys.argv[2]
    except IndexError:
        usage()

    thdiff(commit_mc, commit_try)


if __name__ == '__main__':
    main()
