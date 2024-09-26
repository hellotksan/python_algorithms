# 配列の分割

from typing import MutableSequence

def partition(a: MutableSequence) -> None:
    """配列を分割して表示"""
    n = len(a)
    pl = 0          # 左カーソル
    pr = n - 1      # 右カーソル
    x = a[n // 2]   # 枢軸（中央の要素）

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    print(f'枢軸の値は{x}です。')

    print('枢軸以下のグループ')
    print(*a[0 : pl])                       # a[0] ～ a[pl - 1]

    if pl > pr + 1:
        print('枢軸と一致するグループ')
        print(*a[pr + 1 : pl])              # a[pr + 1] ～ a[pl - 1]

    print('枢軸以上のグループ')
    print(*a[pr + 1 : n])                   # a[pr + 1] ～ a[n - 1]

if __name__ == '__main__':
    print('配列を分割します。')
    num = int(input('要素数：'))
    x = [None] * num    # 要素数numの配列を生成

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    partition(x)        # 配列xを分割して表示
