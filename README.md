# sensei-sensor-device
Raspberry Piで作るBLEタグのセンサー

## デバイス

- Raspberry Pi 3 Model 3B+

## 環境

- Raspberry Pi OS Lite(32-bit) 5.4.51-v7+

- BlueZ 5.50-1.2~deb10u1+rpt2

- Python 3.7.3

- pip3 18.1

- bluepy 1.3.0

## 使い方

- `.env`ファイルに以下の項目を追加する。

```
ROOM_ID=
SERVER_ADDRESS=
```

- 必要なモジュールのインストール

```
$ sudo pip3 install -r requirements.txt
```
