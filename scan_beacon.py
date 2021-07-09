import time
import send_server
from beacontools import BeaconScanner, IBeaconFilter, IBeaconAdvertisement


ble_dic = {}


def callback(bt_addr, rssi, packet, additional_info):
    if bt_addr in ble_dic:
        ble_dic[bt_addr] += 1
    else:
        ble_dic[bt_addr] = 1
    print("MAC Address: %s \n RSSI: %d" % (bt_addr, rssi))


# scan for all iBeacon advertisements from beacons with certain properties:
# - uuid
# - major
# - minor
# at least one must be specified.
# scan for all iBeacon advertisements regardless from which beacon
def main():
    scanner = BeaconScanner(callback, packet_filter=IBeaconAdvertisement)
    scanner.start()
    time.sleep(5)
    scanner.stop()

    return ble_dic


if __name__ == "__main__":
    main()
    print(ble_dic.keys())
