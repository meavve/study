x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
a = x2 - x1
b = y2 - y1
if (a >= -1 and a <= 1) and (b >= -1 and b <= 1):
    print('YES')
else:
    print('NO')
