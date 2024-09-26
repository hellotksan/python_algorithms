# n個の記号文字*をw個ごとに改行しながら表示（その２）

print('記号文字*を表示します。')
n = int(input('全部で何個：'))
w = int(input('何個ごとに改行：'))

for _ in range(n // w):
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)
