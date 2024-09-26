# シェーカーソート（双方向バブルソート）

from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:
    """"シェーカーソート（双方向バブルソート）"""
    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        for j in range(right, left, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last

        for j in range(left, right):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last

if __name__ == '__main__':
    print('シェーカーソート（双方向バブルソート）')
    num = int(input('要素数：'))
    x = [None] * num    # 要素数numの配列を生成

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    shaker_sort(x)      # 配列xを単純交換ソート

    print('昇順にソートしました。')
    for i in range(num):
        print(f'x[{i}]＝{x[i]}')
