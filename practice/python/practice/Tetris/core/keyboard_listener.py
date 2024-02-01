# -*- coding: UTF-8 -*-
#  
# @FILE        : Tetris/keyboard_listener.py
# @Author      : Nestor
# @Date        : 2023/1/18 03:00      
# @Email       : admin@nestor.me
# 
# @Description : 
#

from threading import Thread

from pynput.keyboard import Listener, Key, Controller


class KeyCallback(object):

    def __init__(self, key, callback):
        self.key = key
        self.callback = callback


class LeftKeyCallback(KeyCallback):

    def __init__(self, callback):
        super().__init__(Key.left, callback)


class RightKeyCallback(KeyCallback):

    def __init__(self, callback):
        super().__init__(Key.right, callback)


class UpKeyCallback(KeyCallback):

    def __init__(self, callback):
        super().__init__(Key.up, callback)


class DownKeyCallback(KeyCallback):

    def __init__(self, callback):
        super().__init__(Key.down, callback)


class KeyboardListener(Thread):

    def __init__(self, key_callback: [KeyCallback], stop_key=Key.esc):
        super().__init__()
        self._key_callback = key_callback
        self._stop_key = stop_key

    def run(self) -> None:
        with Listener(on_press=self.on_release) as listener:
            listener.join()

    def stop_listener(self):
        keyboard = Controller()
        keyboard.press(self._stop_key)
        keyboard.release(self._stop_key)

    def on_release(self, key):
        if self._stop_key == key:
            return False

        for key_callback in self._key_callback:

            try:
                if key.char == key_callback.key:
                    key_callback.callback()
            except AttributeError:
                if key == key_callback.key:
                    key_callback.callback()


if __name__ == '__main__':
    def func1():
        print("func1")


    def func2():
        print("func2")


    t = KeyboardListener([KeyCallback(Key.left, func2), KeyCallback("a", func1)])
    t.start()
