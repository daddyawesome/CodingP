import sqlite3

#create database
con = sqlite3.connect('db.sqlite3')
cur = con.cursor() # instantiate a cursor obj

#Creating Tables
<<<<<<< HEAD
cur.execute('DROP TABLE IF EXISTS customers')
cur.execute('DROP TABLE IF EXISTS products')
cur.execute('DROP TABLE IF EXISTS orders')
cur.execute('DROP TABLE IF EXISTS lineitems')
=======
>>>>>>> bc9ac2429747cc303da6c07d113ccb69787e6384
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

lineitems_sql = """
 CREATE TABLE lineitems (
     id integer PRIMARY KEY,
     quantity integer NOT NULL,
     total real NOT NULL,
     product_id integer,
     order_id integer,
     FOREIGN KEY (product_id) REFERENCES products (id),
     FOREIGN KEY (order_id) REFERENCES orders (id))"""
cur.execute(lineitems_sql)

#Loading the Data

product_sql = "INSERT INTO products (name, price) VALUES (?, ?)"
cur.execute(product_sql, ('Introduction to Combinatorics', 7.99))
cur.execute(product_sql, ('A Guide to Writing Short Stories', 17.99))
cur.execute(product_sql, ('Data Structures and Algorithms', 11.99))
cur.execute(product_sql, ('Advanced Set Theory', 16.99))

#Checking Data
cur.execute("SELECT id, name, price FROM products")
formatted_result = [f"{id:<5}{name:<35}{price:>5}" for id, name, price in cur.fetchall()]
id, product, price = "Id", "Product", "Price"
print('\n'.join([f"{id:<5}{product:<35}{price:>5}"] + formatted_result))

#Creating Methods to Insert Data to Tables
def create_customer(con, first_name, last_name):
    sql = """
        INSERT INTO customers (first_name, last_name)
        VALUES (?, ?)"""
    cur = con.cursor()
    cur.execute(sql, (first_name, last_name))
    return cur.lastrowid

def create_order(con, customer_id, date):
    sql = """
        INSERT INTO orders (customer_id, date)
        VALUES (?, ?)"""
    cur = con.cursor()
    cur.execute(sql, (customer_id, date))
    return cur.lastrowid

def create_lineitem(con, order_id, product_id, qty, total):
    sql = """
        INSERT INTO lineitems
            (order_id, product_id, quantity, total)
        VALUES (?, ?, ?, ?)"""
    cur = con.cursor()
    cur.execute(sql, (order_id, product_id, qty, total))
    return cur.lastrowid

#Inserting data
#
try:
    codd_id = create_customer(con, 'Edgar', 'Codd')
    codd_order = create_order(con, codd_id, '1969-01-12')
    codd_li = create_lineitem(con, codd_order, 4, 1, 16.99)
    knuth_id = create_customer(con, 'Donald', 'Knuth')
    knuth_order = create_order(con, knuth_id, '1967-07-03')
    knuth_li1 = create_lineitem(con, knuth_order, 2, 1, 17.99)
    knuth_li2 = create_lineitem(con, knuth_order, 3, 1, 11.99)

    # commit the statements
    con.commit()
except:
    # rollback all database actions since last commit
    con.rollback()
    raise RuntimeError("Uh oh, an error occurred ...")

cur.execute("SELECT id, first_name, last_name FROM customers")
results = cur.fetchall()
for row in results:
     print(row)

cur.close()
