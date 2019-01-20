#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from urllib import urlopen

import pandas as pd

from bs4 import BeautifulSoup

def get_status_list():

    home_url = 'http://jam-capture-vcon-ww.ateamid.com/zh_TW'

    # 異常狀態
    url = home_url + '/status_list.html'
    page = urlopen(url).read()

    soup = BeautifulSoup(page, 'html.parser')

    # 有三個先製作出第一個
    status_item = soup.find('dl', class_='status__item')

    all_dt = status_item.find_all('dt')
    all_dd = status_item.find_all('dd')

    name_list = [dt.text for dt in all_dt]
    desc_list = [dd.text.replace('\n', '') for dd in all_dd]

    data = {
        'name': name_list,
        'desc': desc_list
    }
    # df = df[['name','desc']]
    df = pd.DataFrame(data=data, columns=['name', 'desc'])
    # print df
    return df

if __name__ == "__main__":
    df = get_status_list()
    print df
