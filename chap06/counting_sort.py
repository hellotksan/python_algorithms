# 度数ソート

from typing import MutableSequence

def fsort(a: MutableSequence, max: int) -> None:
    """度数ソート（配列要素の値は0以上max以下）"""
    n = len(a)
    f = [0] * (max + 1)     # 累積度数
    b = [0] * n             # 作業用目的配列

    for i in range(n):             f[a[i]] += 1                     # [Step 1]
    for i in range(1, max + 1):    f[i] += f[i - 1]                 # [Step 2]
    for i in range(n - 1, -1, -1): f[a[i]] -= 1; b[f[a[i]]] = a[i]  # [Step 3]
    for i in range(n):             a[i] = b[i]                      # [Step 4]

def counting_sort(a: MutableSequence) -> None:
    """度数ソート"""
    fsort(a, max(a))

if __name__ == '__main__':
    print('度数ソート')
    num = int(input('要素数：'))
    x = [None] * num      # 要素数numの配列を生成

    for i in range(num):
        while True:
            x[i] = int(input(f'x[{i}]：'))
            if x[i] >= 0: break

    counting_sort(x)     # 配列xを度数ソート

    print('昇順にソートしました。')
    for i in range(num):
        print(f'x[{i}]＝{x[i]}')