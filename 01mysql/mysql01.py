# -*- conding:utf8 -*-

import pymysql

db = pymysql.connect(host = 'localhost',user = 'root',db = 'bkzd',)

cursor = db.cursor()

cursor.execute("SELECT * from orgfull")

data = cursor._get_db()

print("Database version: %s" % data)
db.close()

