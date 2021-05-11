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
class userregister(Resource):
    def post(self):
        conn=sqlite3.connect('data.db')
        cur=conn.cursor()
        parser=reqparse.RequestParser()
        parser.add_argument('username',type=str,required=True,help="this field can't be left blank")
        parser.add_argument('password',type=str,required=True,help="this field can't be left blank")
        data=parser.parse_args()
        select="select * from users"
        c=0
        for i in cur.execute(select):
            if(i[1]==data['username'] and i[2]==data['password']):
                conn.close()
                return {'message':'user already exists'}
          
           
        insert_query="insert into users values(NULL,?,?)"
        cur.execute(insert_query,(data['username'],data['password']))
        conn.commit()
        conn.close()



# In[ ]:




