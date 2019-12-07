import sqlite3

#create database
con = sqlite3.connect('db.sqlite3')
cur = con.cursor() # instantiate a cursor obj

#Creating Tables
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

#Loading the Data

product_sql = "INSERT INTO products (name, price) VALUES (?, ?)"
cur.execute(product_sql, ('Introduction to Combinatorics', 7.99))
cur.execute(product_sql, ('A Guide to Writing Short Stories', 17.99))
cur.execute(product_sql, ('Data Structures and Algorithms', 11.99))
cur.execute(product_sql, ('Advanced Set Theory', 16.99))

cur.execute("SELECT id, name, price FROM products")
formatted_result = [f"{id:<5}{name:<35}{price:>5}" for id, name, price in cur.fetchall()]
id, product, price = "Id", "Product", "Price"
print('\n'.join([f"{id:<5}{product:<35}{price:>5}"] + formatted_result))
