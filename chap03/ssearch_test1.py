# 線形探索を行う関数seq_searchの利用例（その１）

from ssearch_while import seq_search

print('実数の探索を行います。')
print('注："End"で入力終了。')

number = 0
x = []                  # 空リスト

while True:
    s = input(f'x[{number}]：')
    if s == 'End':
        break
    x.append(float(s))  # 末尾に追加
    number += 1

ky = float(input('探す値：'))   # キーkyの読込み

idx = seq_search(x, ky)         # kyと等価な要素をxから探索
if idx == -1:
    print('その値の要素は存在しません。')
else:
    print(f'それはx[{idx}]にあります。')
