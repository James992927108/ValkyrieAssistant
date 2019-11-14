#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
from copy import deepcopy 

class DB():
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = self.connect_to_db()
        self.cursor = self.conn.cursor()

    def connect_to_db(self):
        try:
            conn = sqlite3.connect("DB/{}.db".format(self.db_name))
            print ("Opened << {} >> database successfully".format(self.db_name))
        except sqlite3.Error as error:
            print ("Failed connected to SQLite", error)
        return conn

    def create_table(self, table_name):
        try:
            cmd = '''CREATE TABLE {}
                    (
                        char_Type   TEXT,
                        char_Index  INT,
                        char_Id     INT PRIMARY KEY,
                        char_Name   TEXT
                    )'''.format(table_name)
            print (cmd)
            self.cursor.execute(cmd)
            print ("table << {} >> created successfully".format(table_name))
        except:
            print ("table << {} >> exist".format(table_name))
 
    def insert_data(self, table_name, data):
        # 如果資料庫原本就有資料，不需要加入，要額外新增判斷重複insert問題
        try:
            cmd = deepcopy("INSERT INTO {} (char_Type,char_Index,char_Id,char_Name) VALUES (\"{}\", {}, {}, \"{}\")".format(table_name,
                deepcopy(data.char_Type),deepcopy(data.char_Index), deepcopy(data.char_Id), deepcopy(data.char_Name.encode("utf-8"))))
            print (cmd)
            self.cursor.execute(cmd)
            print ("Successed to insert data {} into {} table".format(data.char_Name.encode("utf-8"), table_name))
            self.conn.commit()
        except sqlite3.Error as error:
            print ("Failed to insert data into {} table, reason is ".format(table_name, error))