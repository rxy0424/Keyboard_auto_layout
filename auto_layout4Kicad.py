# -*- conding:utf-8 -*-

switch_begin="s"
switch_index = 2

rawData = r'''
["Tab","Q","W","E","R","T","Y","U","I","O","P","{\n[","}\n]","|\n\\"],
[{w:1.25},"Ctrl","A","S","D","F","G","H","J","K","L",":\n;","\"\n'",{w:1.75},"Enter"],
[{w:1.75},"Shift","Z","X","C","V","B","N","M","<\n.",">\n.","?\n/",{w:1.25},"Shift","del"],
[{w:1.25},"Ctrl","Win",{w:1.25},"Alt",{a:7,w:2.75},"",{a:4,w:2.75},"Fn",{w:1.25},"Backspace",{w:1.25},"Fn",{w:1.25},"Fn",{w:1.25},"Ctrl"]
'''

from layout2list import rawData2list

import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()


def activateKiCAD():
    time.sleep(1)
    k.press_key(k.alt_key)
    k.tap_key(k.tab_key)
    k.release_key(k.alt_key)
    time.sleep(1)


def moveComponment(name, x_position, y_position):
    # find it
    time.sleep(0.1)
    k.press_key(k.control_l_key)
    k.tap_key('f')
    k.release_key(k.control_l_key)
    time.sleep(0.1)
    k.type_string(name)
    time.sleep(0.1)
    k.tap_key(k.enter_key)

    # close find dialog
    time.sleep(0.1)
    k.tap_key(k.escape_key)

    # move it
    time.sleep(0.1)
    k.press_key(k.control_l_key)
    k.tap_key('m')
    k.release_key(k.control_l_key)
    time.sleep(0.1)
    k.tap_key(k.tab_key)
    time.sleep(0.1)
    k.type_string(x_position)
    time.sleep(0.1)
    k.tap_key(k.tab_key)
    time.sleep(0.1)
    k.type_string(y_position)
    time.sleep(0.1)
    k.tap_key(k.enter_key)
    time.sleep(0.1)

def main():
    activateKiCAD()
    switchPositions = rawData2list(rawData)

    mswitch_index = switch_index
    for now_x, now_y in switchPositions:
        switch_name = switch_begin + str(mswitch_index)
        mswitch_index += 1

        x_str = str(now_x)
        y_str = str(now_y)
        moveComponment(switch_name, x_str, y_str)


if __name__ == "__main__":
    main()
