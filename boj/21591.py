# Laptop Sticker Problem

w_c, h_c, w_s, h_s = map(int, input().split())

if w_s <= w_c - 2 and h_s <= h_c - 2:
    print(1)
else:
    print(0)
