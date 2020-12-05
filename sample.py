# https://www.ipride.co.jp/blog/2510 このサンプルコード

from bluepy import btle

# デバイスをスキャンするためのクラスを初期化する。
# 引数(index=0)は、使用するBluetoothインターフェースの番号を表す
# ※ index=0 が /dev/hci0 に対応する
scanner = btle.Scanner(0)

# デバイスをスキャンする(結果はValuesView[ScanEntry]型で返される)
# 引数(timeout=10.0)は、スキャンする秒数を表す
devices = scanner.scan(3.0)

# # スキャンした結果を表示
# #  ペリフェラルデバイスとの接続にはMACアドレスとアドレスタイプが必要
# #  RSSIは要するに電波強度で、それなりにないと接続に成功しない
# #  アドバタイシングデータは、そのペリフェラルデバイスがアドバタイズパケットで
# #  周囲に発信している、デバイスの情報を表すデータ
# device = devices
# print(device, end='\n')
# print(type(device))\
connectable_devices = [device for device in list(devices) if device.connectable]
for device in connectable_devices:
    print(f'MAC Address:    {device.addr}')
    print(f'  Address Type: {device.addrType}')
    print(f'  iface:        {device.iface}')
    print(f'  RSSI:         {device.rssi}')
    print(f'  Connectable?: {device.connectable}')
    print(f'  Update Count: {device.updateCount}')
    

# adTypeCodeはアドバタイシングデータのキーで、
# descriptionはそれを人間が読めるように翻訳したもの。
# そしてvalueTextはアドバタイシングデータの値
    # print(f'  アドバタイシングデータ：')
    # for (adTypeCode, description, valueText) in device.getScanData():
    #     print(f'    {description}：{valueText}')
