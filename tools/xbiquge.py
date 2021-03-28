"""
Biquge new ,download serve for FM

@author: Tang142857
@project: fiction
@file: xbiquge.py
@date: 2021-03-27
Copyright(c): DFSA Software Develop Center
"""
import requests
from bs4 import BeautifulSoup


class BiqugeNewSpider(object):
    def __init__(self, arg_list: dict):
        # in this website ,just the home url is ok
        self.home_url = arg_list['extend']['url']
        self.save_directory = arg_list['extend']['output_dir']
        if self.save_directory.endswith('/'):
            pass
        else:
            self.save_directory += '/'

    def main(self):
        source = requests.get(self.home_url).content
        home_soup = BeautifulSoup(source, 'lxml')
        chapter_list_elements = home_soup.select('#list > dl > dd > a')
        chapter_list = []
        for element in chapter_list_elements:
            chapter_list.append([element['href'], element.text])
        # chapter list end

        for index, task in enumerate(chapter_list):
            url = f'http://www.xbiquge.la{task[0]}'
            source = requests.get(url).content
            soup = BeautifulSoup(source, 'lxml')
            # get html file

            ad_element = soup.select('#content > p')[0]
            content_element = soup.select('#content')[0]
            text = content_element.text.replace(ad_element.text, '')
            # get and clean the content
            print(f'\r{index}of{len(chapter_list)}--{task[1]}', end='')

            with open(f'{self.save_directory}{task[1]}.txt', 'w', encoding='utf-8') as f:
                f.write(text)


downloader = BiqugeNewSpider
if __name__ == '__main__':
    d = BiqugeNewSpider({
        'extend': {
            'url': 'http://www.xbiquge.la/23/23466/',
            'output_dir': '/home/tang/file/private/relaxing/customer/fiction/xdldl'
        }
    })
    d.main()
