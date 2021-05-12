#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sqlite3
from flask_restful import Resource,reqparse

class User:
    def __init__(self,_id,username,password):
        self.id=_id
        self.username=username
        self.password=password
    @classmethod
    def findbyusername(cls,username):
        conn=sqlite3.connect('data.db')
        cur=conn.cursor()
        select_query="select * from users where username=?"
        result=cur.execute(select_query,(username,))
        row=result.fetchone()
        if row:
            user=cls(*row)
        else:
            user=None
        conn.close()
        return user
    @classmethod
    def findbyid(cls,_id):
        conn=sqlite3.connect('data.db')
        cur=conn.cursor()
        select_query="select * from users where id=?"
        result=cur.execute(select_query,(_id,))
        row=result.fetchone()
        if row:
            user=cls(*row)
        else:
            user=None
        conn.close()
        return user




# In[ ]:




