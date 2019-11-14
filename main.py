#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

import web_link
from character import character
from db_sqlite import DB

def get_char_list(page_index, soup):
    char_list = []
    # all_td = soup.find_all('td',limit = 2)
    all_td = soup.find_all('td')
    db = DB(db_name = "Valkyrie")
    db.create_table(table_name = "character")
    
    for i , td in enumerate(all_td):
        a = td.find('a')
        # get character infomation
        char_Type = str(page_index)
        char_Index = i
        char_Id = re.findall(r'\d+', str(a.get('href')))[0]
        char_Name = a.find('p',class_ = 'list_item_name').text
        # use "character" class
        data = character(char_Type,char_Index,char_Id,char_Name)
        # save data to DB
        db.insert_data(table_name = "character" ,data = data)

        data._print()
        char_list.append(data)

    return char_list

if __name__ == "__main__":
    
    for page_index in range(1,2):
        soup = web_link.get_character_list_soup(page_index)
        char_list = get_char_list(page_index, soup)
