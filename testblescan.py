#!/usr/bin/env python
# -*- coding: utf-8 -*-
from servo_motor import autoDoor_func
import blescan
import sys
import bluetooth._bluetooth as bluez
import re
# タイマーのライブラリ
import time

dev_id = 0
UUID = r"4346570584B444B7AEB3CA1884FE26B6"
door_flg = True
one_flg = True

try:
  sock = bluez.hci_open_dev(dev_id)
  print "ble thread started"
except:
  print "error accessing bluetooth device..."
  sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

while True:
  returnedList = blescan.parse_events(sock, 1)
  print "----------"
  for beacon in returnedList:
    matchBeacon = re.search(UUID, beacon,re.IGNORECASE)
    print(beacon)
    if matchBeacon:
      print "OK"
      if one_flg:
        one_flg = False
        autoDoor_func(0) #:ドアオープン関数
        # タイマーのライブラリ
        time.sleep(20.0) #sleep(秒指定)
        one_flg = True
      else:
        print("ESCAPE!!!!")

