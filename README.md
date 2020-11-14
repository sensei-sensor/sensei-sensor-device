# sensei-sensor-device
Raspberry Piで作るBLEタグのセンサー

## デバイス

- Raspberry Pi 3 Model 3B+

## Raspberry Piのセットアップ

1. PCに Raspberry Pi 用のSDカードを挿入

1. [Raspberry Pi 公式サイト](https://www.raspberrypi.org/downloads/) から **Raspberry Pi Imager** をダウンロード

1. ダウンロードしたファイルからRaspberry Pi Imagerをインストール

1. Raspberry Pi Imager を起動

1. Operating Systemの下にある、**CHOOSE OS** をクリック

	1. Raspberry Pi OS(other) をクリック

	1. Raspberry Pi OS Lite を選択

1. SD Cardの下、**CHOOSE SD CARD** をクリック

1. 最初に挿入したSDカードを選択

1. **WHITE** をクリック

## SSHの設定

> 外部モニターがある場合は飛ばしても構わないです。

1. エクスプローラーを開いて **boot** ディスクに入る

	> SDカードではなく、250MB程度が使用されている **boot** ディスクに入る。<br>
	表示されない場合は挿入し直す。

1. `ssh` というファイルを作成

	> 拡張子は **必要ない** 

1. SDカードを取り出す

## 3. Raspberry Piの起動とSSHの接続

1. SDカードをスロットに挿入する

1. LANケーブルを接続する

1. Micro USB に電源を挿す

1. ちょっと待つ

1. SSH でアクセスする

```
Username:	pi
Password:	raspberry
Address:	raspberrypi.local or 同一ネットワークのIPアドレス
Port:		22
```

- Open SSHだと↓

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

1. アップデート

```shell
$ sudo apt update
$ sudo apt upgrade
```