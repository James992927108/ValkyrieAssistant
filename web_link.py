#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
# for python3
# from urllib.request import urlopen
# for python2
from urllib import urlopen

home_url = 'http://jam-capture-vcon-ww.ateamid.com/zh_TW'

def get_soup(url):
    page = urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')
    return soup

# use in main.py
def get_character_list_soup(index):
    href = '/character_list/{}.html?filter=#{}'.format(index,index)
    return get_soup(home_url + href)

# use in character.py
def get_character_detail_soup(Id):
    href = '/character_detail/{}.html'.format(Id)
    return get_soup(home_url + href)

# use in status.py
def get_status_list_soup():
    href = '/status_list.html'
    return get_soup(home_url + href)

