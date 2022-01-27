import pymysql
import os

print("DB Info")
print("[connect_db]: " + os.getenv("DB_USER"))
print("[connect_db]: " + os.getenv("DB_PWD"))
print("[connect_db]: " + os.getenv("DB_NAME") + "\n")

connect = pymysql.connect(
    host="localhost",
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PWD"),
    db=os.getenv("DB_NAME"),
    charset="utf8",
)
