import pymysql
import os

print("DB Info")
print(os.getenv("DB_USER"))
print(os.getenv("DB_PWD"))
print(os.getenv("DB_NAME"))

connect = pymysql.connect(
    host="localhost",
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PWD"),
    db=os.getenv("DB_NAME"),
    charset="utf8",
)
