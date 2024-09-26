# 単純選択ソート

from typing import MutableSequence

def selection_sort(a: MutableSequence) -> None:
    """単純選択ソート"""
    n = len(a)
    for i in range(n - 1):
        min = i                         # 未ソート部の最小要素の添字
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]     # 未ソート部の先頭要素と最小要素を交換

if __name__ == '__main__':
    print('単純選択ソート')
    num = int(input('要素数：'))
    x = [None] * num    # 要素数numの配列を生成

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    selection_sort(x)   # 配列xを単純選択ソート

    print('昇順にソートしました。')
    for i in range(num):
        print(f'x[{i}]＝{x[i]}')
