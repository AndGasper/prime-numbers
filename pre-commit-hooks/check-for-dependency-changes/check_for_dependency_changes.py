#!/usr/bin/env python3
# ^ this ain't it. 
import argparse
import json
from typing import Optional, Sequence, Set

from pre_commit_hooks.util import cmd_output 
from pre_commit_hooks.util import CalledProcessError


class Error(Exception):
    """Base class for exceptions - I am sure there are more complicated versions."""
    pass

class HasDependencyChangeError(Error):
    """
    Exception raised for a defined when a staged commit has dependency changes lumped in with a bunch of non-dependency changes.
    
    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
    
DEPENDENCY_ERROR_MESSAGE_HELP = "The staged changes contain 'code' and 'dependency' changes. Please unstage the 'code' changes, commit the dependency changes, then push."

# toggle the PIPENV_VERBOSITY=-1 based on
# the environment
#   -> "local"
#   -> "pipeline"/container
# check if there is a diff in the
# Pipfile.lock and force the dependency update to be logged
# separately
# you can imagine there may be other rules/errors surronding
# version control specific changes.

def diff_head() -> Set[str]:
    try:
        diff_return = cmd_output('git', 'diff', '--name-only', '--cached')
        files_list = diff_return.split('\n')
    except CalledProcessError:
        files_list = []
    return set(files_list)

# stop bikeshedding...
# you can imagine more complex validation, but for now a simple int will do
def commit_validate_dependency() -> int:
    """
    Description: Check if the staged changes contain any: Pipfile, Pipfile.lock, requirements.txt
    If dependency files are present then raise
    """
    python_dependency_file_types = set(
        ['Pipfile', 'Pipfile.lock', 'requirements.txt']
    )
    # take the compliment
    # dependency_file_types = [ 'Pipfile', 'Pipfile.lock', 'requirements.txt' ]
    # staged_changes = [ 'a.py', 'b.py', 'Pipfile', 'Pipfile.lock', 'requirements.txt' ]
    # compliment = dependency_file_types - staged_changes; # output:  set()

    compliment_of_staged_files = python_dependency_file_types - diff_head()

    try:
        # awkward -> the compliment should be the same if the other items are not present
        if (compliment_of_staged_files == python_dependency_file_types):
            return_value = 0
        else:
            raise HasDependencyChangeError(compliment_of_staged_files, DEPENDENCY_ERROR_MESSAGE_HELP)
    except HasDependencyChangeError as dependency_change_error:
        
        print("\ndependency_change_error")
        print(dependency_change_error)

        return_value = 1

    return return_value

def main(argv: Optional[Sequence[str]] = None) -> int:
    """
    argv: Optional[Sequence[str]]
    """
    return commit_validate_dependency()


# the trick is to return either a 
# 0 (success) exit code or 
# a non-zero ("failure") exit code 
if __name__ == '__main__':
    exit(main())