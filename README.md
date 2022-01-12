# Sensei Sensor Device
Raspberry Piで作るBLEタグのセンサー

## デバイス

- Raspberry Pi 3 Model 3B+

## 環境

- Raspberry Pi OS Lite(32-bit) 5.4.51-v7+
- Python 3.7.3
    - pip3 18.1
    - bluepy 1.3.0

## 使い方

- `.env`ファイルに以下の項目を追加する。

```.env
ROOM_ID=
SERVER_ADDRESS=
DB_USER=
DB_PWD=
DB_NAME=
```

- 必要なパッケージ・モジュールのインストール

> pipenvが必要です

```sh
sudo apt-get install python3-pip python3-dev libbluetooth-dev libglib2.0-dev libcap2-bin
sudo setcap 'cap_net_raw,cap_net_admin+eip' "$(readlink -f "$(which python3)")"
sudo pipenv install
```
