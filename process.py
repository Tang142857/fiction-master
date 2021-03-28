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
import re


def main(arg_list: dict):
    print('Starting getting...')
    # Always ,use the website arg is not convenient , so we should get the host name
    url = arg_list['extend']['url']
    searcher = re.compile(r'(http|https)://\w+.\w+.\w+/')
    splitter=re.compile(r'(http|https)://(\w+).(\w+).(\w+)/')
    result = searcher.search(url)
    splitted=splitter.split(result.group())[1:-1]
    host_name=splitted[2]
    # get the host name end

    downloader = manager.get_downloader(host_name)
    downloader_pointer = downloader(arg_list)
    downloader_pointer.main()


if __name__ == '__main__':
    main({'extend': {'url': 'http://www.xbiquge.la/1/1710/'}})
