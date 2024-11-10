#!/usr/bin/env python
import argparse
import os
from datetime import datetime, timedelta
from random import randint
from subprocess import Popen
import sys


def main(def_args=sys.argv[1:]):
    args = arguments(def_args)
    curr_date = datetime.now()
    directory = 'repository-' + curr_date.strftime('%Y-%m-%d-%H-%M-%S')
    repository = args.repository
    user_name = args.user_name
    user_email = args.user_email

    # Create a directory based on the repository name
    if repository is not None:
        start = repository.rfind('/') + 1
        end = repository.rfind('.')
        directory = repository[start:end]
    
    no_weekends = args.no_weekends
    frequency = args.frequency
    days_before = args.days_before
    days_after = args.days_after

    # Validate days range
    if days_before < 0 or days_after < 0:
        sys.exit('Error: days_before and days_after must not be negative')

    # Create and navigate to the directory
    os.mkdir(directory)
    os.chdir(directory)
    run(['git', 'init', '-b', 'main'])

    # Set up Git user config if specified
    if user_name:
        run(['git', 'config', 'user.name', user_name])
    if user_email:
        run(['git', 'config', 'user.email', user_email])

    # Define the start date
    start_date = curr_date.replace(hour=20, minute=0) - timedelta(days=days_before)

    # Generate commits for each day within the range
    for day in (start_date + timedelta(n) for n in range(days_before + days_after)):
        if (not no_weekends or day.weekday() < 5) and randint(0, 100) < frequency:
            for commit_time in (day + timedelta(minutes=m) for m in range(contributions_per_day(args))):
                contribute(commit_time)

    # Push to remote repository if specified
    if repository:
        run(['git', 'remote', 'add', 'origin', repository])
        run(['git', 'branch', '-M', 'main'])
        run(['git', 'push', '-u', 'origin', 'main'])

    print('\nRepository generation \x1b[6;30;42mcompleted successfully\x1b[0m!')


def contribute(date):
    """Creates a commit with a specified date."""
    with open(os.path.join(os.getcwd(), 'README.md'), 'a') as file:
        file.write(message(date) + '\n')
    run(['git', 'add', '.'])
    run(['git', 'commit', '-m', f'"{message(date)}"', '--date', date.strftime('"%Y-%m-%d %H:%M:%S"')])


def run(commands):
    """Executes a shell command."""
    Popen(commands).wait()


def message(date):
    """Generates a commit message based on the date."""
    return date.strftime('Contribution: %Y-%m-%d %H:%M')


def contributions_per_day(args):
    """Determines the number of commits per day."""
    max_c = args.max_commits
    return randint(1, min(max_c, 20))


def arguments(argsval):
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-nw', '--no_weekends', action='store_true', default=False,
                        help="Do not commit on weekends")
    parser.add_argument('-mc', '--max_commits', type=int, default=10,
                        help="Max commits per day (1-20)")
    parser.add_argument('-fr', '--frequency', type=int, default=80,
                        help="Frequency percentage of days to commit")
    parser.add_argument('-r', '--repository', type=str,
                        help="Remote Git repository URL")
    parser.add_argument('-un', '--user_name', type=str,
                        help="Git user name")
    parser.add_argument('-ue', '--user_email', type=str,
                        help="Git user email")
    parser.add_argument('-db', '--days_before', type=int, default=365,
                        help="Days before today to start committing")
    parser.add_argument('-da', '--days_after', type=int, default=0,
                        help="Days after today to commit")
    return parser.parse_args(argsval)


if __name__ == "__main__":
    main()

