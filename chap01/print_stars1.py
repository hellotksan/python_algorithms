# n個の記号文字*をw個ごとに改行しながら表示（その１）

print('記号文字*を表示します。')
n = int(input('全部で何個：'))
w = int(input('何個ごとに改行：'))

for i in range(n):
    print('*', end='')
    if i % w == w - 1:
        print()        # 改行

if n % w:
    print()            # 改行
t