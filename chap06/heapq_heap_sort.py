# ヒープソート（heapq.pushとheapq.popを利用）

import heapq
from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    """ヒープソート（heapq.pushとheapq.popを利用）"""

    heap = []
    for i in a:
        heapq.heappush(heap, i)
    for i in range(len(a)):
        a[i] = heapq.heappop(heap)

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
