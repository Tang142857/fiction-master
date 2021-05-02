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

VERSION = '0.0.0'


class ArgList(object):
    """
    Argument list serve.
    Arguments rules:
        -arg arg_string : this is used to pass a string arg like url.
        --argname : this is used as a switch ,will save as 'key':true/false
    """
    def __init__(self, argv: list):
        """Formatting the arg list to python object"""
        if len(argv) == 1:  # only path.
            self.version = True
            return

        for index, element in enumerate(argv[1:]):  # ignore the first argument ,always file position.
            if element.startswith('--'):
                setattr(self, element[2:], True)
            elif element.startswith('-'):  # if starts with --,then is not -
                setattr(self, element[1:], argv[index + 2])

    def __str__(self):
        result = ''
        for attribute_name in dir(self):
            if attribute_name.startswith('_'):
                continue
            else:
                result += attribute_name + ' -> ' + str(getattr(self, attribute_name)) + '\n'
        return result

    def __getattribute__(self, name):
        # to avoid the attribute error
        try:
            return super().__getattribute__(name)
        except AttributeError:
            return False


if __name__ == '__main__':
    arg = ArgList(sys.argv)
    # receive the user's command
    if arg.version:
        print(VERSION)
        exit(0)

    process.main(argument)
    # start downloader
