# -*- conding:utf-8 -*-
import demjson


# all unit is inch
def rawData2list(rawData):

    layout = demjson.decode('[' + rawData + ']')

    now_x = -0.75
    now_y = -0.75
    last_width_rate = 1.0

    switch_position = []

    for row in layout:
        now_y = now_y + 0.75
        now_x = -0.75
        last_width_rate = 1.0
        key_width_rate = 1.0
        for item in row:
            if isinstance(item, dict):
                if item.has_key('w'):
                    key_width_rate= item['w']
                if item.has_key('x'):
                    now_x = now_x + item['x']*0.75
                if item.has_key('y'):
                    now_y = now_y + item['y']*0.75
            elif isinstance(item, (str, unicode)):
                x_offset = (last_width_rate+key_width_rate)*0.75/2.0
                now_x = now_x + x_offset
                switch_position.append((now_x, now_y))

                last_width_rate = key_width_rate
                key_width_rate = 1.0
    return switch_position

if __name__ == "__main__":
    raw_string = r'''
    ["Esc","Q","W","E","R","T","Y","U","I","O","P","Back<br>Space"],
    [{w:1.25},"Tab","A","S","D","F","G","H","J","K","L",{w:1.75},"Enter"],
    [{w:1.75},"Shift","Z","X","C","V","B","N","M","<\n.",{x:1.25},"Fn"],
    [{w:1.25},"Hyper","Super","Meta",{a:7,w:6.25},"",{a:4,w:1.25},"Meta",{w:1.25},"Super"]
    '''
    print(rawData2list(raw_string))
