import time
import read_json
from beacontools import BeaconScanner, IBeaconFilter, IBeaconAdvertisement

tag0 = 0
tag1 = 0

def callback(bt_addr, rssi, packet, additional_info):
    global tag0, tag1
    if (read_json.check_tag_number(bt_addr) is not None):
        print("Tag number: %s" % (read_json.check_tag_number(bt_addr)))
        print(" RSSI: %d" % (rssi))
        if (read_json.check_tag_number(bt_addr) == 0):
            tag0 += 1
        elif (read_json.check_tag_number(bt_addr) == 1):
            tag1 += 1


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

print()
print("Tag0: " + str(tag0))
print("Tag1: " + str(tag1))