#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask_restful import Resource,reqparse
import sqlite3
from flask_jwt import jwt_required


class Item(Resource):
    def post(self,name):
        if self.findbyname(name):
            return {'message':"item {} already exists".format(name)}
        parser=reqparse.RequestParser()
        parser.add_argument('price',type=float,required=True,help="this field is required")
        data=parser.parse_args()
        item={'name':name,'price':data['price']}
        try:
            self.insert(item)
        except:
            return {"message":"an error occurred"},500
        return item,201
    @classmethod
    def insert(cls,item):
        conn=sqlite3.connect('data.db')
        cur=conn.cursor()
        query="insert into items values(?,?)"
        cur.execute(query,(item['name'],item['price']))
        conn.commit()
        conn.close()
    @classmethod
    def findbyname(cls,name):
        conn=sqlite3.connect('data.db')
        cur=conn.cursor()
        query="select * from items where name=?"
        cur.execute(query,(name,))
        row=cur.fetchone()
        if row:
            return {'item':{'name':row[0],'price':row[1]}}
        
    @jwt_required()
    def get(self,name):
        item=self.findbyname(name)
        if item:
            return item
        return {'message':'item not found'},404
    def delete(self,name):
        conn=sqlite3.connect('data.db')
        cur=conn.cursor()
        query="delete from items where name=?"
        cur.execute(query,(name,))
        conn.commit()
        conn.close()
        return {'message':'item deleted'}
    def put(self,name):
        parser=reqparse.RequestParser()
        parser.add_argument('price',type=float,required=True,help="this field can't be left blank")
        data=parser.parse_args()
        res=self.findbyname(name)
        item={'name':name,'price':data['price']}
        if res:
            conn=sqlite3.connect('data.db')
            cur=conn.cursor()
            query="update items set price=? where name=?"
            cur.execute(query,(data['price'],name))
            conn.commit()
            conn.close()
        else:
            try:
                self.insert(item)
            except:
                return {'message':'something wrong has occured'},500
        return item
class Item_list(Resource):
    def get(self):
        items=[]
        conn=sqlite3.connect('data.db')
        cur=conn.cursor()
        query="select * from items"
        for i in cur.execute(query):
            items.append(i)
        conn.commit()
        conn.close()
        return {'items':items}