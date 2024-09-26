# ヒープソート

from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    """ヒープソート"""

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        """a[left]～a[right]をヒープ化"""
        temp = a[left]      # 根

        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1     # 左の子
            cr = cl + 1             # 右の子
            child = cr if cr <= right and a[cr] > a[cl] else cl # 大きいほう
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)

    for i in range((n - 1) // 2, -1, -1):   # a[i]～a[n-1]をヒープ化
        down_heap(a, i, n - 1)

    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]     # 最大要素と未ソート部末尾要素を交換
        down_heap(a, 0, i - 1)      # a[0]～a[i-1]をヒープ化

if __name__ == '__main__':
    print('ヒープソート')
    num = int(input('要素数：'))
    x = [None] * num    # 要素数numの配列を生成

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    heap_sort(x)        # 配列xをヒープート

    print('昇順にソートしました。')
    for i in range(num):
        print(f'x[{i}]＝{x[i]}')
