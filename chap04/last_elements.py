# 好きな個数だけ値を読み込んで要素数nの配列に最後のn個を格納

n = int(input('何個の整数を記憶しますか：'))
a = [None] * n  # 読み込んだ値を格納する配列

cnt = 0         # 読み込んだ個数
while True:
    a[cnt % n] = int(input((f'{cnt + 1}個目の整数：')))
    cnt += 1

    retry = input(f'続けますか？（Y…Yes／N…No）：')
    if retry in {'N', 'n'}:
        break

i = cnt - n
if i < 0: i = 0

while i < cnt:
    print(f'{i + 1}個目＝{a[i % n]}')
    i += 1
