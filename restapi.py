#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT,jwt_required
from security import authenticate,identity
from user1 import userregister
from item1 import Item,Item_list
from crea import create

app=Flask(__name__)
api=Api(app)
app.secret_key='uday'
items=[]
jwt=JWT(app,authenticate,identity)




api.add_resource(Item,'/item/<string:name>')
api.add_resource(Item_list,'/items')
api.add_resource(userregister,'/register')

if __name__=='__main__':
    app.run(port=5000)
