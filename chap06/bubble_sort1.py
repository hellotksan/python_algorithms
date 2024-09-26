# 単純交換ソート

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    """単純交換ソート"""
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]

if __name__ == '__main__':
    print('単純交換ソート（バブルソート）')
    num = int(input('要素数：'))
    x = [None] * num    # 要素数numの配列を生成

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    bubble_sort(x)      # 配列xを単純交換ソート

    print('昇順にソートしました。')
    for i in range(num):
        print(f'x[{i}]＝{x[i]}')
