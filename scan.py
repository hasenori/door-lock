#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GPIOを制御するライブラリ
import wiringpi2 as wp
# タイマーのライブラリ
import time
# 引数取得
import sys

# from servo_motor import autoDoor_func
# autoDoor_func(0) #:ドアオープン関数

from bluetooth.ble import DiscoveryService

service = DiscoveryService()
devices = service.discover(1)

for address, name in devices.items():
    print("name: {}, address: {}".format(name, address))
