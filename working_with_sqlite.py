import sqlite3
import json
from pathlib import Path

try:
    data = json.loads(Path('data.json').read_text())
    # command = "CREATE TABLE IF NOT EXISTS products ('no' INTEGER, 'name' TEXT NOT NULL, 'count' INTEGER NOT NULL, PRIMARY KEY('no'))"
    with sqlite3.connect('db.sqlite3') as conn:
        # command = "INSERT INTO products VALUES (?, ?, ?)"
        # for product in data:
        #     conn.execute(
        #         command, (product['no'], product['name'], product['count']))
        command = "SELECT * FROM products"
        cursor = conn.execute(command)
        # cursor.fetchall()
        for row in cursor:
            print(row)
        # conn.commit()
except Exception as e:
    print(e)
