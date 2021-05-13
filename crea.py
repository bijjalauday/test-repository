#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sqlite3
def create():
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    create_table="create table if not exists users(id INTEGER PRIMARY KEY,username text,password text)"
    cur.execute(create_table)
    create_table="create table if not exists items(name text,price real)"
    cur.execute(create_table)
    conn.commit()
    conn.close()



# In[ ]:




