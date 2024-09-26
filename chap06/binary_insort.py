# ２分挿入ソート（bisect.insortを利用）

from typing import MutableSequence
import bisect

def binary_insertion_sort(a: MutableSequence) -> None:
    """２分挿入ソート（bisect.insortを利用）"""
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)

if __name__ == '__main__':
    print('２分挿入ソート')
    num = int(input('要素数：'))
    x = [None] * num            # 要素数numの配列を生成

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    binary_insertion_sort(x)    # 配列xを２分挿入ソート

    print('昇順にソートしました。')
    for i in range(num):
        print(f'x[{i}]＝{x[i]}')
