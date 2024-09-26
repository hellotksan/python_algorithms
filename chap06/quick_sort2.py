# クイックソート（第２版）

from typing import MutableSequence

def sort3(a: MutableSequence, idx1: int, idx2: int, idx3: int):
    """a[idx1], a[idx2], a[idx3]を昇順にソートして中央値の添字を返却"""
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    if a[idx3] < a[idx2]: a[idx3], a[idx2] = a[idx2], a[idx3]
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    return idx2

def insertion_sort(a: MutableSequence, left: int, right: int) -> None:
    """a[left]～a[right]を単純挿入ソート"""
    for i in range(left + 1, right + 1):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left]～a[right]をクイックソート"""
    if right - left < 9:    # 要素数が9未満であれば単純挿入ソートに切りかえる
        insertion_sort(a, left, right)
    else:
        pl = left                   # 左カーソル
        pr = right                  # 右カーソル
        m = sort3(a, pl, (pl + pr) // 2, pr)
        x = a[m]

        a[m], a[pr - 1] = a[pr - 1], a[m]
        pl += 1
        pr -= 2
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
    print('クイックソート（第２版）')
    num = int(input('要素数：'))
    x = [None] * num    # 要素数numの配列を生成

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    quick_sort(x)       # 配列xをクイックソート

    print('昇順にソートしました。')
    for i in range(num):
        print(f'x[{i}]＝{x[i]}')
