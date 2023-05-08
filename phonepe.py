#!/usr/bin/env python
# coding: utf-8

# In[59]:


import os
import json
import pandas as pd

path = "D:\\USHA\\presentations\\phonepe\\ghData\\pulse\\data\\aggregated\\transaction\\country\\india\\state\\"
user_state_list = os.listdir(path)
#Agg_state_list
# Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------->#

# This is to extract the data's to create a dataframe

clm = {'State': [], 'Year': [], 'Quater': [], 'Transacion_type': [],
       'Transacion_count': [], 'Transacion_amount': []}
for i in user_state_list:
    p_i = path+i+"/"
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = p_i+j+"/"
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D['data']['transactionData']:
                    Name = z['name']
                    count = z['paymentInstruments'][0]['count']
                    amount = z['paymentInstruments'][0]['amount']
                    clm['Transacion_type'].append(Name)
                    clm['Transacion_count'].append(count)
                    clm['Transacion_amount'].append(amount)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
            except:
                pass
# Succesfully created a dataframe
Agg_Trans = pd.DataFrame(clm)
#Agg_Trans.to_csv('D:\\USHA\presentations\\test folders\\test\\Aggregated_trans.csv')
#Agg_Trans


# In[60]:


# This is to direct the path to get the data as states
path = "D:\\USHA\\presentations\\phonepe\\ghData\\pulse\\data\\aggregated\\user\\country\\india\\state\\"
user_state_list = os.listdir(path)
#Agg_state_list
# Agg_state_list--> to get the list of states in India

#<---------------------------------------------------------------------------------------------------------------------->#

# This is to extract the data's to create a dataframe

clm = {'State': [], 'Year': [], 'Quater': [], 'Brand': [],
    'Brand_count': [], 'Brand_percentage': []}
for i in user_state_list:
    p_i = path+i+"/"
    year = os.listdir(p_i)
    for j in year:
        p_j = p_i+j+"/"
        file = os.listdir(p_j)
        for k in file:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D['data']["usersByDevice"]:
                    
                    brand = z['brand']

                    brand_count = z['count']
                    brand_percentage = z["percentage"]
                    clm['Brand'].append(brand)
                    clm['Brand_count'].append(brand_count)
                    clm['Brand_percentage'].append(brand_percentage)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
            except:
                pass 
                

user_by_device = pd.DataFrame(clm)
#user_by_device.to_csv('D:\\USHA\presentations\\test folders\\test\\aggregated_user.csv')
#user_by_device


# In[61]:


path = "D:\\USHA\\presentations\\phonepe\\ghData\\pulse\\data\\map\\transaction\\hover\\country\\india\\state\\"
state_list = os.listdir(path)
#Agg_state_list
# Agg_state_list--> to get the list of states in India

#<-------------------------------------------------------------------------------------------------------------------->#

# This is to extract the data's to create a dataframe

clm = {'State': [], 'Year': [], 'Quater': [], 'District': [],
    'Transaction_count': [], 'Transaction_amount': []}
for i in state_list:
    p_i = path+i+"/"
    year = os.listdir(p_i)
    for j in year:
        p_j = p_i+j+"/"
        file = os.listdir(p_j)
        for k in file:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D['data']["hoverDataList"]:
                    district = z['name']
                    transaction_count = z['metric'][0]['count']
                    transaction_amount = z['metric'][0]['amount']
                    clm['District'].append(district)
                    clm['Transaction_count'].append(transaction_count)
                    clm['Transaction_amount'].append(transaction_amount)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
# Succesfully created a dataframe
            except:
                pass   
                

map_transaction = pd.DataFrame(clm)
#map_transaction.to_csv('D:\\USHA\\presentations\\test folders\\test\\map_transaction.csv')
#map_transaction


# In[62]:


path = "D:\\USHA\\presentations\\phonepe\\ghData\\pulse\\data\\map\\user\\hover\\country\\india\\state\\"
state_list = os.listdir(path)
#Agg_state_list
# Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

# This is to extract the data's to create a dataframe

clm = {'State': [], 'Year': [], 'Quater': [], 'District': [],
    'Registered_user': [], 'App_opening': []}
for i in state_list:
    p_i = path+i+"/"
    year = os.listdir(p_i)
    for j in year:
        p_j = p_i+j+"/"
        file = os.listdir(p_j)
        for k in file:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D['data']["hoverData"]:
                    district = z
                    registered_user =  D['data']["hoverData"][z]["registeredUsers"]
                    app_opening = D['data']["hoverData"][z]["appOpens"]
                    clm['District'].append(district)
                    clm['Registered_user'].append(registered_user)
                    clm['App_opening'].append(app_opening)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
# Succesfully created a dataframe
            except:
                pass       
                 

district_registering = pd.DataFrame(clm)
#district_registering.to_csv('D:\\USHA\\presentations\\test folders\\test\\map_user.csv')
#district_registering


# In[ ]:





# In[63]:


path = "D:\\USHA\\presentations\\phonepe\\ghData\\pulse\\data\\top\\transaction\\country\\india\\state\\"
top_trans = os.listdir(path)
#Agg_state_list
# Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------->#

# This is to extract the data's to create a dataframe

clm = {'State': [], 'Year': [], 'Quater': [], 'District': [],
       'Transacion_count': [], 'Transacion_amount': []}
for i in top_trans:
    p_i = path+i+"/"
    toptran_yr = os.listdir(p_i)
    for j in toptran_yr:
        p_j = p_i+j+"/"
        toptran_yr_list = os.listdir(p_j)
        for k in toptran_yr_list:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D['data']['districts']:
                    Name = z['entityName']
                    count = z['metric']['count']
                    amount = z['metric']['amount']
                    clm['District'].append(Name)
                    clm['Transacion_count'].append(count)
                    clm['Transacion_amount'].append(amount)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
            except:
                pass
# Succesfully created a dataframe
TopTrans_Data = pd.DataFrame(clm)
#TopTrans_Data.to_csv('D:\\USHA\\presentations\\test folders\\test\\Top_Trans.csv')
#TopTrans_Data


# In[58]:


path = "D:\\USHA\\presentations\\phonepe\\ghData\\pulse\\data\\top\\user\\country\\india\\state\\"
top_user = os.listdir(path)
#Agg_state_list
# Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------->#

# This is to extract the data's to create a dataframe

clm = {'State': [], 'Year': [], 'Quater': [], 'District': [],
       'UserRegistered': []}
for i in top_user:
    p_i = path+i+"/"
    topUser_yr = os.listdir(p_i)
    for j in topUser_yr:
        p_j = p_i+j+"/"
        topUser_yr_list = os.listdir(p_j)
        for k in topUser_yr_list:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D['data']['districts']:
                    Name = z['name']
                    user_Reg = z['registeredUsers']
                    
                    clm['District'].append(Name)
                    clm['UserRegistered'].append(user_Reg)
                   
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
            except:
                pass
# Succesfully created a dataframe
TopUser_Data = pd.DataFrame(clm)
#TopUser_Data.to_csv('D:\\USHA\\presentations\\test folders\\test\\Top_User.csv')
#TopUser_Data


# In[19]:


pip install mysql-connector-python


# In[42]:


import mysql.connector
import pandas as pd

mydb=mysql.connector.connect(
host="localhost",
user="root",
password="govdonviv_K94",
auth_plugin="mysql_native_password"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE phonepe;")
mycursor.execute(" USE phonepe")


#mycursor.execute('CREATE TABLE samptab (MyIndex INT NOT NULL AUTO_INCREMENT,State INT,Year INT,Quater INT,Payment_Mode VARCHAR(50),Total_Transactions_count BIGINT,Total_Amount BIGINT,PRIMARY KEY (MyIndex))')

    
df = pd.read_csv("D:\\USHA\\presentations\\test folders\\test\\aggregated_user.csv")
#print(df.isna().sum())
df.to_sql(name='samptab',con=mydb, if_exists= "replace")


# In[ ]:





# In[21]:


pip install pymysql


# In[87]:


import pymysql
import pandas as pd
import sqlalchemy
from sqlalchemy import text
import socket


# In[88]:


user = 'root'
password = 'govdonviv_K94'
host = 'localhost'
port = 3306
database = 'phonepe'
connection = sqlalchemy.create_engine("mysql+pymysql://root:govdonviv_K94@localhost:3306/phonepe")


# In[60]:


sq_2=text('CREATE TABLE agg_userbydevice_table (MyIndex INT NOT NULL AUTO_INCREMENT,State INT,Year INT,Quater INT,Brand VARCHAR(50),Brand_count BIGINT,Brand_percentage BIGINT,PRIMARY KEY (MyIndex))')
connection.execute(sq_2)
df = pd.read_csv("D:\\USHA\\presentations\\test folders\\test\\aggregated_user.csv")
df.to_sql('agg_user',con=connection, if_exists= "replace",index=False, chunksize=1000)


# In[59]:


sq_1=text('CREATE TABLE agg_trans (MyIndex INT NOT NULL AUTO_INCREMENT,State INT,Year INT,Quater INT,Payment_Mode VARCHAR(50),Total_Transactions_count BIGINT,Total_Amount BIGINT,PRIMARY KEY (MyIndex))')
connection.execute(sq_1)
df = pd.read_csv("D:\\USHA\\presentations\\test folders\\test\\Aggregated_trans.csv")
df.to_sql('agg_trans',con=connection, if_exists= "replace",index=False, chunksize=1000)


# In[61]:


sq_3 = text('CREATE TABLE map_trans (MyIndex INT NOT NULL AUTO_INCREMENT,State INT,Year INT,Quater INT,District VARCHAR(50),Transaction_count BIGINT,Transaction_amount BIGINT,PRIMARY KEY (MyIndex))')
connection.execute(sq_3)
df = pd.read_csv("D:\\USHA\\presentations\\test folders\\test\\map_transaction.csv")
df.to_sql('map_trans',con=connection, if_exists= "replace",index=False, chunksize=1000)


# In[62]:


sq_4 = text('CREATE TABLE map_user (MyIndex INT NOT NULL AUTO_INCREMENT,State INT,Year INT,Quater INT,District VARCHAR(50),Registered_user BIGINT,App_opening BIGINT,PRIMARY KEY (MyIndex))')
connection.execute(sq_4)
df = pd.read_csv("D:\\USHA\\presentations\\test folders\\test\\map_user.csv")
df.to_sql('map_user',con=connection, if_exists= "replace",index=False, chunksize=1000)


# In[63]:


sq_5 = text('CREATE TABLE top_trans (MyIndex INT NOT NULL AUTO_INCREMENT,Code VARCHAR(50),Latitude BIGINT, Longitude BIGINT, State VARCHAR(50),PRIMARY KEY (MyIndex))')
connection.execute(sq_5)
df = pd.read_csv("D:\\USHA\\presentations\\test folders\\test\\Top_Trans.csv")
df.to_sql('top_trans',con=connection, if_exists= "replace",index=False, chunksize=1000)


# In[64]:


sq_6 = text('CREATE TABLE top_user(MyIndex INT NOT NULL AUTO_INCREMENT,State VARCHAR(50),District VARCHAR(50),Latitude BIGINT, Longitude BIGINT,PRIMARY KEY (MyIndex))')
connection.execute(sq_6)
df = pd.read_csv("D:\\USHA\\presentations\\test folders\\test\\Top_User.csv")
df.to_sql('top_user',con=connection, if_exists= "replace",index=False, chunksize=1000)


# In[ ]:


# -------------------------------------------------- Mysql server connection using sqlalchemy ---------------------------------------------
# --------------------------------------------------- Must install pymysql -----------------------------------------------------------------
user = 'root'
password = 'govdonviv_K94'
host = 'localhost'
port = 3306
database = 'phonepe'
connection = sqlalchemy.create_engine("mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
    user, password, host, port, database
))

# ---------------------------------------------------- Fetching datas from Mysql using pandas -----------------------------------------------
query1 = 'select * from agg_trans'
df = pd.read_sql(query1, con=connection)
query2 = 'select * from top_trans'
state = pd.read_sql(query2, con=connection)
query3 = 'select * from top_user'
districts = pd.read_sql(query3, con=connection)
query4 = 'select * from map_trans'
districts_tran = pd.read_sql(query4, con=connection)
query5 = 'select * from map_user'
app_opening = pd.read_sql(query5, con=connection)
query6 = 'select * from agg_user'
user_device = pd.read_sql(query6, con=connection)


# In[ ]:


import mysql.connector
import pandas as pd

mydb=mysql.connector.connect(
host="localhost",
user="root",
password="govdonviv_K94",
auth_plugin="mysql_native_password"
)
mycursor = mydb.cursor()

mycursor.execute(" USE phonepe")

#df = pd.read_csv("D:\\USHA\\presentations\\test folders\\test\\aggregated_user.csv")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[121]:





# In[ ]:





# In[ ]:






# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




