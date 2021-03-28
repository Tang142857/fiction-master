"""
Tools manager.
All tools will be managed by manager ,don't use tools directly.

@author: Tang142857
@project: fiction
@file: manager.py
@date: 2021-03-27
Copyright(c): DFSA Software Develop Center
"""
import importlib


def get_downloader(website: str):
    """Get the downloader by website name."""
    model = importlib.import_module(website)
    return model.downloader


"""
Write some websites' host names here.
xbiquge http://www.xbiquge.la/
"""
