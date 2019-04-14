#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

import web_link
from character import character
from db_sqlite import DB

def get_char_list(page_index, soup):
    char_list = []
    all_td = soup.find_all('td')
    # all_td = soup.find('td')
    for i , td in enumerate(all_td):
        a = td.find('a')
        # 建立角色的id
        try:
            # in here also need to save char to db
            char_Type = str(page_index)
            char_Index = i
            char_Id = re.findall(r'\d+', str(a.get('href')))[0]
            char_Name = a.find('p',class_ = 'list_item_name').text

            char = character(char_Type,char_Index,char_Id,char_Name)
            
            db = DB("Valkyrie")
            db.insert_char(char)
            # db.test()
            
            char._print()
            char_list.append(char)
        except:
            print("no href")

    return char_list

if __name__ == "__main__":
    
    for page_index in range(1,4):
        soup = web_link.get_character_list_soup(page_index)
        char_list = get_char_list(page_index, soup)
