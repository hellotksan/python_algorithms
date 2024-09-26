# 単純挿入ソート

from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    """単純挿入ソート"""
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

if __name__ == '__main__':
    print('単純挿入ソート')
    num = int(input('要素数：'))
    x = [None] * num    # 要素数numの配列を生成

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    insertion_sort(x)   # 配列xを単純挿入ソート

    print('昇順にソートしました。')
    for i in range(num):
        print(f'x[{i}]＝{x[i]}')
