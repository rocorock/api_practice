# -*- coding: utf-8 -*-
import sqlite3

filepath = "restdata.sqlite"
conn = sqlite3.connect(filepath)

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS address")

cur.execute("""CREATE TABLE address(
        id INTEGER PRIMARY KEY,
        postnum TEXT UNIQUE,
        address TEXT UNIQUE
    )""")
conn.commit()

for line in open("address.csv", "r"):
    input_data = tuple(line[:-1].split(","))
    cur.execute(
            "INSERT INTO address (id, postnum, address) VALUES (?, ?, ?)",input_data)
    conn.commit()
