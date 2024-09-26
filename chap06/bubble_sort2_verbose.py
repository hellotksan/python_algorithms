# 単純交換ソート（第２版：交換回数による打切り）《ソート過程を表示》

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    """単純交換ソート（第２版：交換回数による打切り）《ソート過程を表示》"""
    ccnt = 0    # 比較回数
    scnt = 0    # 交換回数
    n = len(a)
    for i in range(n - 1):
        print(f'パス{i + 1}')
        exchng = 0      # パスにおける交換回数
        for j in range(n - 1, i, -1):
            for m in range(0, n - 1):
               print(f'{a[m]:2}' + ('  ' if m != j - 1 else
                                    ' +' if a[j - 1] > a[j] else ' -'),
                     end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                exchng += 1
        for m in range(0, n - 1):
           print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')
        if exchng == 0:
            break
    print(f'比較は{ccnt}回でした。')
    print(f'交換は{scnt}回でした。')

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
