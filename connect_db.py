import pymysql
import os

db_connect = pymysql.connect(
    host="localhost",
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PWD"),
    db=os.getenv("DB_NAME"),
    charset="utf8",
)
