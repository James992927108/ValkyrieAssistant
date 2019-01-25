#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib import urlopen
import pandas as pd
import status
import re
from copy import deepcopy


class character():
    def __init__(self,Index=0, Type = 0, Id=0 ,Name=0, Data=0, Action_Skill=0, Limit_Burst=0, States=0):
        self.Type = Type
        self.Index = Index
        self.Id = Id
        self.Name = Name
        self.Data = Data
        self.Action_Skill = Action_Skill
        self.Limit_Burst = Limit_Burst
        self.States = States

# character_list/1.html?filter=#1
# character_list/1.html#1
# get_char_list_soup(index)

def get_soup(url):
    page = urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')
    return soup

def get_char_list_soup(index):
    url = home_url + '/character_list/{}.html?filter=#{}'.format(index,index)
    return get_soup(url)


def get_Type(page_index):
    return {
        '1':'前排',
        '2':'中排',
        '3':'後排'
    }.get(page_index,'error Type')

def get_all_char_id_name(page_index, soup):
    list_all_char_db = []
    # 方便測試先以find
    all_td = soup.find_all('td')
    for i , td in enumerate(all_td):
        char = character()
        a = td.find('a')
        # 建立角色的id
        try:
            char.Type = get_Type(str(page_index))
            char.Index = i
            char.Id = re.findall(r'\d+', str(a.get('href')))[0]
            # href = a.get('href').replace('..', '')
            # char_href_list.append(href)
            char.Name = a.find('p',class_ = 'list_item_name').text
            list_all_char_db.append(char)
        except:
            print("no href")
        # print char.Type, char.Index, char.Id, char.Name

    return list_all_char_db

def get_char_detail(Index ,char):
    Id = char.Id
    df_Data = create_table(Id, 'detail__data--txt', 'Data')
    df_Action_Skill = create_table(Id, 'detail__skill--txt', 'Action_Skill')
    print Index ,char.Type, char.Index, char.Id, char.Name
    if Index == char.Index:
        char.Data = deepcopy(df_Data)
        char.Action_Skill = deepcopy(df_Action_Skill)
        # LB 和 States 未作
        # print char.Index, char.Id, char.Name ,char.Data, char.Action_Skill

    # print df_Data.to_json(orient= "records")
    # with open('df.json', 'w') as file:
    #     df_Data.set_index('title')['Data'].to_json(file, force_ascii=False)
    
    return char

def create_table(Id,class_name, column_name):

    href = '/character_detail/{}.html'.format(Id)
    url = home_url + href
    soup = get_soup(url)

    dl = soup.find('dl', class_= class_name)

    title_list = [re.sub('\s','',x.text) for i, x in enumerate(dl.find_all('dt'))]
    data_list = [re.sub('\s','',x.text) for i, x in enumerate(dl.find_all('dd'))]
    
    data = {
        'title': title_list,
        column_name : data_list
    }

    df = pd.DataFrame(data=data, columns=['title', column_name])
    return df    

def find_state(df_Action_Skill):
    # 需要紀錄狀態對特定種族
    s = []
    status_list = status.get_status_list()
    for state in status_list['name']:
        # 第二項為效果
        if df_Action_Skill['Action_Skill'][2].find(state)>0:
            s.append(state)
    return s  

if __name__ == "__main__":
    df_all_char_db = pd.DataFrame(columns=['Id','Name','Data','Action_Skill','Limit_Burst','States'])
    home_url = 'http://jam-capture-vcon-ww.ateamid.com/zh_TW'
    
    for page_index in range(1,4):
        soup = get_char_list_soup(page_index)
        list_all_char_db = get_all_char_id_name(page_index, soup)
        for index ,char in enumerate(list_all_char_db):
            # df_Data, df_Action_Skill = get_char_detail((index+1),char)
            char = get_char_detail(index,char)
            states = find_state(char.Action_Skill)
            for s in states:
                print char.Data['Data'][1] , s
 
