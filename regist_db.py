import connect_db
import os


def get_user_id(mac_address):
    print("[regist_db] MAC Address: " + mac_address)
    get_user_id_sql = "SELECT userId FROM tag WHERE MACAddress='{}'".format(
        mac_address.replace(":", "")
    )
    with connect_db.connect.cursor() as cursor:
        cursor.execute(get_user_id_sql)
        cursor.close()
        userId = cursor.fetchone()
    if userId is None:
        return userId
    else:
        return userId[0]


def regist_ble(mac_address):
    user_id = get_user_id(mac_address)
    if user_id == None:
        return False
    print("[regist_db] user_id: " + str(user_id) + "\n")
    last_time_sql = "SELECT MIN(TIME_TO_SEC(TIMEDIFF(CURRENT_TIMESTAMP(),time))) AS diffTime FROM `discoveryLog` WHERE userId = {}".format(
        user_id
    )
    with connect_db.connect.cursor() as cursor:
        cursor.execute(last_time_sql)
        sensor_time = cursor.fetchone()[0]
        cursor.close()
    print( sensor_time)
    if sensor_time == None or sensor_time > int(os.getenv("SCAN_INTERVAL")):
        insert_discv_log_sql = "INSERT INTO discoveryLog (sensorId,userId,time) VALUES({},{},current_timestamp())".format(
            os.getenv("ROOM_ID"), user_id
        )
        with connect_db.connect.cursor() as cursor:
            cursor.execute(insert_discv_log_sql)
            connect_db.connect.commit()
            cursor.close()
