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

def main():
    switchPositions = rawData2list(rawData)

    mswitch_index = switch_index

    f = open("pos.txt", "w")
    for now_x, now_y in switchPositions:
        switch_name = switch_begin + str(mswitch_index)
        mswitch_index += 1

        # from inch to mils
        x_str = str(now_x * 1000)
        y_str = str(now_y * 1000)
        f.write("%s %s %s\n" % (switch_name, x_str, y_str))


if __name__ == "__main__":
    main()
