def similarRGB(color):
    def rounding(color):
        q, r = divmod(int(color, 16), 17)
        if r > 8: q += 1
        return '{:02x}'.format(17*q)

    return '#' + \
            rounding(color[1:3]) + rounding(color[3:5]) + rounding(color[5:7])

assert similarRGB("#09f166") == "#11ee66"
assert similarRGB("#010000") == "#000000"