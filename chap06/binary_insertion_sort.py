# ２分挿入ソート

from typing import MutableSequence

def binary_insertion_sort(a: MutableSequence) -> None:
    """２分挿入ソート"""
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0      # 探索範囲の先頭要素の添字
        pr = i - 1  # 探索範囲の末尾要素の添字

        while True:
            pc = (pl + pr) // 2     # 探索範囲の中央要素の添字
            if a[pc] == key:        # 探索成功
               break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr:
                break
        # 挿入すべき位置の添字
        pd = pc + 1 if pl <= pr else pr + 1

        for j in range(i, pd, -1):
            a[j] = a[j - 1]
        a[pd] = key

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
