import time
import send_server
import read_json
from beacontools import BeaconScanner, IBeaconFilter, IBeaconAdvertisement


def callback(bt_addr, rssi, packet, additional_info):
    print("MAC Address: %s \n RSSI: %d" % (bt_addr, rssi))
    read_json.check_tag_number(bt_addr)


# scan for all iBeacon advertisements from beacons with certain properties:
# - uuid
# - major
# - minor
# at least one must be specified.

# scan for all iBeacon advertisements regardless from which beacon
scanner = BeaconScanner(callback,
                        packet_filter=IBeaconAdvertisement)
scanner.start()
time.sleep(5)
scanner.stop()
