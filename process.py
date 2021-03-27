"""
Processor for fiction-master

@author: Tang142857
@project: fiction-master
@file: process.py
@date: 2021-03-26
Copyright(c): DFSA Software Develop Center
"""
import sys
from tools import manager


def main(arg_list: dict):
    print('Starting getting...')
    downloader = manager.get_downloader(arg_list['website'])
    downloader_pointer = downloader(arg_list)
    downloader_pointer.main()


if __name__ == '__main__':
    main({})
