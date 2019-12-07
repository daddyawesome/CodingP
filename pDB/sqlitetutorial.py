import sqlite3

#create database
con = sqlite3.connect('db.sqlite3')
cur = con.cursor() # instantiate a cursor obj

Creating Tables
customers_sql = """
 CREATE TABLE customers (
     id integer PRIMARY KEY,
     first_name text NOT NULL,
     last_name text NOT NULL)"""
cur.execute(customers_sql)

products_sql = """
 CREATE TABLE products (
     id integer PRIMARY KEY,
     name text NOT NULL,
     price real NOT NULL)"""
cur.execute(products_sql)

orders_sql = """
 CREATE TABLE orders (
     id integer PRIMARY KEY,
     date text NOT NULL,
     customer_id integer,
     FOREIGN KEY (customer_id) REFERENCES customers (id))"""
cur.execute(orders_sql)

