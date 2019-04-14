#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import web_link

def get_status_list():

    soup = web_link.get_status_list_soup()

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

    df = pd.DataFrame(data=data, columns=['name', 'desc'])

    return df
