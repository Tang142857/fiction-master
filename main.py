#!/usr/bin/python3
"""
Fiction-master main file.

@author: Tang142857
@project: fiction
@file: main.py
@date: 2021-03-13
Copyright(c): DFSA Software Develop Center
"""
import sys
import process


class ArgList(object):
    """Argument list serve."""
    def __init__(self, argv: list):
        """Formatting the arg list to python object"""
        print(f'Received arg list {argv}')
        for index, element in enumerate(argv[1:]):  # ignore the first argument ,always file position.
            if element.startswith('-'):
                setattr(self, element[1:], argv[index + 2])

    def __str__(self):
        return str(dir(self))


if __name__ == '__main__':
    arg = ArgList(sys.argv)
    print(f'Generating tasks argument list...')
    argument={
        'name':
    }
