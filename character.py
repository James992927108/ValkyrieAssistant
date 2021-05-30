#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
from copy import deepcopy
import web_link
import re
import status

class character():
    def __init__(self,char_Type,char_Index,char_Id,char_Name):
        # get_char_list
        self.char_Type = self.get_Type(char_Type)
        self.char_Index = char_Index
        self.char_Id = char_Id
        self.char_Name = char_Name
        
        self.Basic_Info = 0
        self.Action_Skill = 0 
        self.Limit_Burst = 0
        self.States = []

        # self.get_char_detail()

    def get_Type(self,page_index):
        return {
            '1':'近戰',
            '2':'中程',
            '3':'遠距'
        }.get(page_index,'error Type')

    def get_char_detail(self):
        # Id = char.Id
        df_Basic_Info = self.create_df('detail__data--txt', 'Basic_Info')
        df_Action_Skill = self.create_df('detail__skill--txt', 'Action_Skill')
        
        self.Basic_Info = deepcopy(df_Basic_Info)
        self.Action_Skill = deepcopy(df_Action_Skill)

        status_list = status.get_status_list()
        for state in status_list['name']:
            print(state)
            # 第二項為效果
            # if self.Action_Skill['Action_Skill'][2].find(state) > 0:
            #     self.States.append(state)

            # LB 和 States 未作

    def create_df(self,class_name, column_name):

        soup = web_link.get_character_detail_soup(self.char_Id)

        dl = soup.find('dl', class_= class_name)

        title_list = [re.sub('\s','',x.text) for _, x in enumerate(dl.find_all('dt'))]
        data_list = [re.sub('\s','',x.text) for _, x in enumerate(dl.find_all('dd'))]
        
        data = {
            'title': title_list,
            column_name : data_list
        }

        df = pd.DataFrame(data=data, columns=['title', column_name])
        return df

    def _print(self):
        print(self.char_Type, self.char_Index,  self.char_Id, self.char_Name)
        # print (self.Basic_Info)
        # print (self.Action_Skill)
        # for s in self.States:
        #     print (s)
            