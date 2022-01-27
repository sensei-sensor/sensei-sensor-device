import time
import regist_db as RDB
import datetime
from beacontools import BeaconScanner, IBeaconFilter, IBeaconAdvertisement


ble_dic = {}


def callback(bt_addr, rssi, packet, additional_info):
    if bt_addr in ble_dic:
        ble_dic[bt_addr] += 1
    else:
        ble_dic[bt_addr] = 1
    print("[scan_beacon] MAC Address: %s\n[scan_beacon] RSSI: %d" % (bt_addr, rssi))
    RDB.regist_ble(bt_addr.replace(":", ""))


# scan for all iBeacon advertisements from beacons with certain properties:
# - uuid
# - major
# - minor
# at least one must be specified.
# scan for all iBeacon advertisements regardless from which beacon
def main():
    scanner = BeaconScanner(callback, packet_filter=IBeaconAdvertisement)
    scanner.start()
    time.sleep(30)
    scanner.stop()


if __name__ == "__main__":
    main()
    print(datetime.datetime.now())
    print(ble_dic.keys())
