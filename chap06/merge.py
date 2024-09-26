# ソートずみ配列のマージ

from typing import Sequence, MutableSequence

def merge_sorted_list(a: Sequence, b: Sequence, c: MutableSequence) -> None:
    """ソートずみ配列aとbをマージしてcに格納"""
    pa, pb, pc = 0, 0, 0                    # カーソル
    na, nb, nc = len(a), len(b), len(c)     # 要素数

    while pa < na and pb < nb:      # 小さいほうを格納
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1

    while pa < na:                  # aに残った要素をコピー
        c[pc] = a[pa]
        pa += 1
        pc += 1

    while pb < nb:                  # bに残った要素をコピー
        c[pc] = b[pb]
        pb += 1
        pc += 1

if __name__ == '__main__':
    a = [2, 4, 6, 8, 11, 13]
    b = [1, 2, 3, 4, 9, 16, 21]
    c = [None] * (len(a) + len(b))
    print('二つのソートずみ配列のマージ')

    merge_sorted_list(a, b, c)    # 配列aとbをマージしてcに格納

    print('配列aとbをマージして配列cに格納しました。')
    print(f'配列a：{a}')
    print(f'配列b：{b}')
    print(f'配列c：{c}')
