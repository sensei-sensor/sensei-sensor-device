import pymysql
import ConnectDB as cnDB
import os


def get_user_id(macAddress):
    print("macAddress:" + macAddress + "\n")
    get_user_id_sql = "SELECT userId FROM tag WHERE MACAddress='{}'".format(
        macAddress.replace(":", "")
    )
    with cnDB.db_connect.cursor() as cursor:
        cursor.execute(get_user_id_sql)
        cursor.close()
        userId = cursor.fetchone()
    if userId is None:
        return userId
    else:
        return userId[0]


def regist_ble(macAddress):
    userId = get_user_id(macAddress)
    if userId is None:
        exit
    print("userId:" + str(userId) + "\n")
    insert_discv_log_sql = "INSERT INTO discoveryLog (sensorId,userId,time) VALUES({},{},current_timestamp())".format(
        os.getenv("SENSOR_ID"), userId
    )
    with cnDB.db_connect.cursor() as cursor:
        cursor.execute(insert_discv_log_sql)
        cnDB.db_connect.commit()
        cursor.close()
