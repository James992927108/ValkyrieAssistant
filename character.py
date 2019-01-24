#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib import urlopen
import pandas as pd
import status
import re


class character():
    def __init__(self, href, icon, name):
        self.href = href
        self.icon = icon
        self.name = name
# import character



# character_list/1.html?filter=#1
# character_list/1.html#1
# get_char_list_soup(index)

def get_char_list_soup(index):
    char_url = home_url + '/character_list/{}.html?filter=#{}'.format(index,index)
    page = urlopen(char_url).read()
    soup = BeautifulSoup(page, 'html.parser')
    return soup

def get_all_char_href(soup):
    char_href_list = []
    # 方便測試先以find
    all_td = soup.find_all('td')
    for td in all_td:
        a = td.find('a')
        try:
            href = a.get('href').replace('..', '')
            char_href_list.append(href)
        except:
            print("no href")
    # 可以作過濾重複

    return char_href_list

def get_char_detail(href):
            
    df_data = create_table('detail__data--txt', 'data')
    df_skill = create_table('detail__skill--txt', 'skill')
    # 還有能力值未取得
    
    return df_data, df_skill

def create_table(class_name, column_name):
    char_url = home_url + href
    page = urlopen(char_url).read()
    soup = BeautifulSoup(page, 'html.parser')

    dl = soup.find('dl', class_= class_name)

    title_list = [re.sub('\s','',x.text) for i, x in enumerate(dl.find_all('dt'))]
    data_list = [re.sub('\s','',x.text) for i, x in enumerate(dl.find_all('dd'))]
    
    data = {
        'title': title_list,
        column_name : data_list
    }

    df = pd.DataFrame(data=data, columns=['title', column_name])
    return df    

def find_state(df_skill):
    s = []
    status_list = status.get_status_list()
    for state in status_list['name']:
        # 第二項為效果
        if df_skill['skill'][2].find(state)>0:
            s.append(state)
    return s  

if __name__ == "__main__":

    home_url = 'http://jam-capture-vcon-ww.ateamid.com/zh_TW'
    for index in range(1,4):
        soup = get_char_list_soup(index)
        char_href_list = get_all_char_href(soup)
        for href in char_href_list:
            df_data, df_skill = get_char_detail(href)
            states = find_state(df_skill)
            for s in states:
                print df_data['data'][1] , s
 
