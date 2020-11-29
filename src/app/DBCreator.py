# -*- coding: utf-8 -*-
import sqlite3

FILEPATH = "home/ec2-user/Database/Address.sqlite"
conn = sqlite3.connect(FILEPATH)

cur = conn.cursor()
cur.execute(
    
)

cur.execute("""CREATE TABLE Address(
        id INTEGER PRIMARY KEY,
        zipcode TEXT UNIQUE,
        prefecture TEXT UNIQUE
    )""")
conn.commit()

for line in open("home/ec2-user/src/assets/address.csv", "r"):
    input_data = tuple(line[:-1].split(","))
    cur.execute(
            "INSERT INTO address (id, zipcode, prefecture) VALUES (?, ?, ?)",input_data)
    conn.commit()
