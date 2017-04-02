#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GPIOを制御するライブラリ
import wiringpi2 as wp
# タイマーのライブラリ
import time
# 引数取得
import sys

#初期設定
SERVO_PIN  =  18 # サーボモータに接続したGPIO端子番号を指定

# サーボモータを動かす角度を指定する
DOOR_UNLOCK = 26 # 解錠：90°の時
DOOR_LOCK= 78    # 施錠：0°の時(初期値は施錠)

#PWMの設定
wp.wiringPiSetupGpio()                    # winringPiの初期設定
wp.pinMode(SERVO_PIN,wp.GPIO.PWM_OUTPUT)  # ハードウェアPWMで出力する
wp.pwmSetMode(wp.GPIO.PWM_MODE_MS)        # サーボモータに合わせたPWM波形の設定
wp.pwmSetClock(375)                       # 周波数を50Hzにすると、18750/周波数=375
wp.pwmSetRange(1024)

# 引数から値を受け取る
param = sys.argv
set_key = int(param[1])

if(set_key == 0):
    #解錠
    # print(set_key)
    wp.pwmWrite(SERVO_PIN, DOOR_UNLOCK)
    time.sleep(5.0) #sleep(5秒指定)
    print("DOOR_LOCK")
    wp.pwmWrite(SERVO_PIN, DOOR_LOCK) # 0°の位置に移動

elif(set_key == 1):
    #施錠
    wp.pwmWrite(SERVO_PIN, DOOR_LOCK) # 0°の位置に移動
else:
    #エラー時にサーボをOFFする
    wp.pwmWrite(SERVO_PIN,0) # 0°の位置に移動

time.sleep(5.0) #sleep(秒指定)
print("OFFSET")
wp.pwmWrite(SERVO_PIN, 0) # 0°の位置に移動
