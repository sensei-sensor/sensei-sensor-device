# Sensei Sensor Device
Raspberry Piで作るBLEタグのセンサー

## デバイス

- Raspberry Pi 3 Model 3B
- Raspberry Pi Zero WH

## 環境

- Raspberry Pi OS Lite(32-bit) 5.10.63-v7+
- Python 3.9.9
    - pip3 21.3.1
    - pipenv

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
