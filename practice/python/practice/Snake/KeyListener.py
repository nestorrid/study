# -*- coding: UTF-8 -*-
#  
# @FILE        : Snake/KeyListener.py
# @Author      : Nestor
# @Date        : 2023/1/13 00:21      
# @Email       : admin@nestor.me
# 
# @Description : 
#

from pynput import keyboard


def on_press(key):
    '按下按键时执行。'
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
    # 通过属性判断按键类型。


def on_release(key):
    '松开按键时执行。'
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
