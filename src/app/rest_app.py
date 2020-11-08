# -*- coding: utf-8 -*-
import sqlite3

filepath = "../../Database/Address.sqlite"
conn = sqlite3.connect(filepath)

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Address")

cur.execute("""CREATE TABLE Address(
        id INTEGER PRIMARY KEY,
        zipcode TEXT UNIQUE,
        prefecture TEXT UNIQUE
    )""")
conn.commit()

for line in open("../assets/address.csv", "r"):
    input_data = tuple(line[:-1].split(","))
    cur.execute(
            "INSERT INTO address (id, zipcode, prefecture) VALUES (?, ?, ?)",input_data)
    conn.commit()
