# 配列の要素の最大値を求めて表示（要素の値を読み込む）

from max import max_of

print('配列の最大値を求めます。')
print('注："End"で入力終了。')

number = 0
x = []                  # 空リスト

while True:
    s = input(f'x[{number}]：')
    if s == 'End':
        break
    x.append(int(s))    # 末尾に追加
    number += 1

print(f'{number}個読み込みました。')
print(f'最大値は{max_of(x)}です。')
