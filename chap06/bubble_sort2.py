# 単純交換ソート（第２版：交換回数による打切り）

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    """単純交換ソート（第２版：交換回数による打切り）"""
    n = len(a)
    for i in range(n - 1):
        exchng = 0      # パスにおける交換回数
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                exchng += 1
        if exchng == 0:
            break

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
