""" Copying the files after rendering. """
import os
import json


WORKING_DIR = os.getcwd()
OPTION_FILE = os.path.join(WORKING_DIR, 'options.json')


def make_gitignore(condition):
    """Create or delete gitignore file."""
    gitignore = os.path.join(WORKING_DIR, 'gitignore')
    dot_gitignore = os.path.join(WORKING_DIR, '.gitignore')
    if condition.startswith('yes'):
        os.rename(gitignore, dot_gitignore)
    else:
        os.remove(gitignore)


if __name__ == "__main__":
    with open(OPTION_FILE) as file:
        options = json.load(file)
    make_gitignore(options['create_gitignore'])
    os.remove(OPTION_FILE)
