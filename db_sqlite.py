#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
from copy import deepcopy 

class DB():
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = self.connect_to_db()
        self.create_table("character")

    def connect_to_db(self):
        conn = sqlite3.connect("DB/{}.db".format(self.db_name))
        print ("Opened << {} >> database successfully".format(self.db_name))
        return conn

    def create_table(self, table_name):
        try:
            cmd = '''CREATE TABLE character
                    (
                        char_Type   TEXT,
                        char_Index  INT,
                        char_Id     INT PRIMARY KEY,
                        char_Name   TEXT
                    )'''

            self.conn.cursor().execute(cmd)
            print ("table << {} >> created successfully".format(table_name))
        except:
            print ("table << {} >> exist".format(table_name))
            return False
        self.conn.commit()
        self.conn.close()

    def insert_char(self, char):
        try:
            cmd = deepcopy("INSERT INTO character (char_Type,char_Index,char_Id,char_Name) VALUES (\"{}\", {}, {}, \"{}\")".format(
                deepcopy(char.char_Type),deepcopy(char.char_Index), deepcopy(char.char_Id), deepcopy(char.char_Name.encode("utf-8"))))
            print cmd
            self.conn.cursor().execute(cmd)
            print "character << {} >> insert successfully".format(char.char_Name)
        except:
            print ("fail")

        self.conn.commit()
        self.conn.close()

# db_name -> Valkyrie
#     table -> character
#           -> state