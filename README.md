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

## Raspberry Piのセットアップ

1. PCに Raspberry Pi 用のSDカードを挿入

2. [Raspberry Pi 公式サイト](https://www.raspberrypi.org/downloads/) から **Raspberry Pi Imager** をダウンロード

3. ダウンロードしたファイルからRaspberry Pi Imagerをインストール

4. Raspberry Pi Imager を起動

5. Operating Systemの下にある、**CHOOSE OS** をクリック

	1. Raspberry Pi OS(other) をクリック

	2. Raspberry Pi OS Lite(32-bit) を選択

6. SD Cardの下、**CHOOSE SD CARD** をクリック

7. 最初に挿入したSDカードを選択

8. **WHITE** をクリック

## SSHの設定

> 外部モニターがある場合は飛ばしても構わないです。

1. エクスプローラーを開いて **boot** ディスクに入る

	> SDカードではなく、250MB程度が使用されている **boot** ディスクに入る。<br>
	表示されない場合は挿入し直す。

2. `ssh` というファイルを作成

	> 拡張子は **必要ない** 

3. SDカードを取り出す

## Raspberry Piの起動とSSHの接続

1. SDカードをスロットに挿入する

2. LANケーブルを接続する

3. Micro USB に電源を挿す

4. ちょっと待つ

5. SSH でアクセスする

```
Username:	pi
Password:	raspberry
Address:	raspberrypi.local or 同一ネットワークのIPアドレス
Port:		22
```

```shell
$ ssh pi@raspberrypi.local

The authenticity of host 'raspberrypi.local (2001:318:a20d:a60:e5ac:15f6:3bfd:a866)' can't be established.
ECDSA key fingerprint is SHA256:PSchbhMDd58sp+CpgSGGsUntKOR8vaav+em327HeMco.

Are you sure you want to continue connecting (yes/no)? yes

Warning: Permanently added 'raspberrypi.local,xxxx:xxxx:xxxx...' (ECDSA) to the list of known hosts.

pi@raspberrypi.local's password: raspberry ← 打っても表示はされませんが、あってればログインできます。
・
・
・

pi@raspberrypi:~ $ 
```

## Raspberry Piの初期設定

1. 時刻合わせ

```shell
$ sudo date --set='YYYY/MM/dd HH:mm:ss'
```

2. 余裕があるならNTPサーバーを設定

[参考](https://gris-et-blanc.net/raspi/152/)

```shell
sudo nano /etc/systemd/timesyncd.conf

-----timesyncd.conf
#  This file is part of systemd.
#
#  systemd is free software; you can redistribute it and/or modify it
#  under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 2.1 of the License, or
#  (at your option) any later version.
#
# Entries in this file show the compile time defaults.
# You can change settings by editing this file.
# Defaults can be restored by simply deleting this file.
#
# See timesyncd.conf(5) for details.

[Time]
+ NTP=ntp.nict.jp ntp.jst.mfeed.ad.jp
+ FallbackNTP=time.google.com
- #NTP
- #FallbackNTP=…
#RootDistanceMaxSec=5
#PollIntervalMinSec=32
#PollIntervalMaxSec=2048
-----
```

3. アップデート

```shell
$ sudo apt update
$ sudo apt upgrade
```

4. Python用Bluetoothライブラリ `Bluepy` のインストール

```shell
$ sudo apt install python3-dev python3-pip libglib2.0-dev
$ sudo pip3 install bluepy
```