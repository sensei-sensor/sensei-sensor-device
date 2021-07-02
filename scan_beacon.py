import time
import send_server
from beacontools import BeaconScanner, IBeaconFilter, IBeaconAdvertisement


def callback(bt_addr, rssi, packet, additional_info):
    print("MAC Address: %s \n RSSI: %d" % (bt_addr, rssi))
    send_server.send_server(bt_addr)


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
