# 配列の要素の最大値を求めて表示（要素の値を乱数で生成）

import random
from max import max_of

print('乱数の最大値を求めます。')
num = int(input('乱数の個数：'))
lo = int(input('乱数の下限：'))
hi = int(input('乱数の上限：'))
x = [None] * num  # 要素数numのリストを生成

for i in range(num):
    x[i] = random.randint(lo, hi)

print(f'{(x)}')
print(f'最大値は{max_of(x)}です。')
