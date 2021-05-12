#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sqlite3
class itemmodel:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def json(self):
        return {'name':self.name,'price':self.price}
    
    @classmethod
    def findbyname(cls,name):
        conn=sqlite3.connect('data.db')
        cur=conn.cursor()
        query="select * from items where name=?"
        cur.execute(query,(name,))
        row=cur.fetchone()
        conn.commit()
        conn.close()
        if row:
            return cls(*row)
            
    def insert(self):
        conn=sqlite3.connect('data.db')
        cur=conn.cursor()
        query="insert into items values(?,?)"
        cur.execute(query,(self.name,self.price))
        conn.commit()
        conn.close()
        