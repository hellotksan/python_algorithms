# クイックソート

from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left]～a[right]をクイックソート"""
    pl = left                   # 左カーソル
    pr = right                  # 右カーソル
    x = a[(left + right) // 2]  # 枢軸（中央の要素）

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr:  qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    """クイックソート"""
    qsort(a, 0, len(a) - 1)

if __name__ == '__main__':
    print('クイックソート')
    num = int(input('要素数：'))
    x = [None] * num    # 要素数numの配列を生成

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    quick_sort(x)       # 配列xをクイックソート

    print('昇順にソートしました。')
    for i in range(num):
        print(f'x[{i}]＝{x[i]}')