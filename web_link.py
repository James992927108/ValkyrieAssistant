#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
# for python3
from urllib.request import urlopen
# for python2
# from urllib import urlopen

import os

home_url = 'http://jam-capture-vcon-ww.ateamid.com/zh_TW/'


def write_file(full_path, file):
    path, file_name = full_path.rsplit('/', 1)
    if not os.path.exists(path):
        os.mkdir(path)
    with open(path + file_name, 'wb') as f:
        f.write(str(file).encode("utf-8"))

def get_soup(url):
    page = urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')
    return soup

# use in main.py


def get_character_list_soup(index):
    href = 'character_list/{}.html'.format(index)
    url = home_url + href
    full_path = str("TempFile/" + href)
    soup =  get_soup(url)
    write_file(full_path, soup)
    return soup

# use in character.py


def get_character_detail_soup(Id):
    href = 'character_detail/{}.html'.format(Id)
    url = home_url + href
    full_path = str("TempFile/" + href)
    soup =  get_soup(url)
    write_file(full_path, soup)
    return soup
# use in status.py


def get_status_list_soup():
    href = 'status_list.html'
    url = home_url + href
    full_path = str("TempFile/" + href)
    soup =  get_soup(url)
    write_file(full_path, soup)
    return soup