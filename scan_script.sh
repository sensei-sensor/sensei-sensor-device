cd /home/pi/sensei-sensor-device/
sudo pipenv run python3 /home/pi/sensei-sensor-device/scan_beacon.py >> /home/pi/sensei-sensor-device/detect_beacon.log
bash /var/www/html/sensei-sensor-php/SyncSystem/dataSync.sh
