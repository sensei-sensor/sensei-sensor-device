import pymysql
import os
db_connect = pymysql.connect(host="localhost", user=os.getenv("DBUSER"),
                             password=os.getenv("DBPWD"), db=os.getenv("DBNAME"),  charset='utf8')
