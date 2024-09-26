# マージソート（heapq.mergeを利用）

from typing import MutableSequence
import heapq

def merge_sort(a: MutableSequence) -> None:
    """マージソート"""
    atype = type(a)

    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        """a[left]～a[right]を再帰的にマージソート"""
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center)        # 前半部をマージソート
            _merge_sort(a, center + 1, right)   # 後半部をマージソート

            buff = atype(heapq.merge(a[left: center+1], a[center + 1: right+1]))
            for i in range(len(buff)):
                a[left + i] = buff[i]

    _merge_sort(a, 0, len(a))     # 配列全体をマージソート

if __name__ == '__main__':
    print('マージソート')
    num = int(input('要素数：'))
    x = [None] * num    # 要素数numの配列を生成

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    merge_sort(x)       # 配列xをマージソート

    print('昇順にソートしました。')
    for i in range(num):
        print(f'x[{i}]＝{x[i]}')
