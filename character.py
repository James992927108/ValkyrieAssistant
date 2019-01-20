#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib import urlopen
import pandas as pd
import status


class character():
    def __init__(self, href, icon, name):
        self.href = href
        self.icon = icon
        self.name = name
# import character


def get_character_list():
    home_url = 'http://jam-capture-vcon-ww.ateamid.com/zh_TW'

    # all char page
    url = home_url + '/character_list/1.html?filter=#1'
    page = urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')

    td = soup.find('td')
    a = td.find('a')
    href = a.get('href').replace('..', '')
    # char page
    url = home_url + href
    page = urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')

    dl = soup.find('dl', class_='detail__skill--txt')
    dd = dl.text.replace('\n','')
    # print dd
    return dd

def find_state(dd):
    # print dd
    status_list = status.get_status_list()
    for state in status_list['name']:
        if dd.find(state)>0:
            print state  



if __name__ == "__main__":

    dd = get_character_list()
    value = find_state(dd)


# f = open('test1.html','w')
# all_td = soup.find_all('td')
# for td in all_td:
#     print type(td)
#     # f.write(td)
# f.close
