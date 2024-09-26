# シェーカーソート（双方向バブルソート）《ソート過程を表示》

from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:
    """"シェーカーソート（双方向バブルソート）《ソート過程を表示》"""
    ccnt = 0    # 比較回数
    scnt = 0    # 交換回数
    left = 0
    n = len(a)
    right = len(a) - 1
    last = right
    i = 0
    while left < right:
        print(f'パス{i + 1}')
        i += 1
        for j in range(right, left, -1):
            for m in range(0, n - 1):
               print(f'{a[m]:2}' + ('  ' if m != j - 1 else
                                    ' +' if a[j - 1] > a[j] else ' -'),
                     end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last
        for m in range(0, n - 1):
           print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')

        if (left == right):
             break
        print(f'パス{i + 1}')
        i += 1
        for j in range(left, right):
            for m in range(0, n - 1):
               print(f'{a[m]:2}' + ('  ' if m != j else
                                    ' +' if a[j] > a[j + 1] else ' -'),
                     end='')
            print(f'{a[n - 1]:2}')
            if a[j] > a[j + 1]:
                scnt += 1
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last
        for m in range(0, n - 1):
           print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')
    print(f'比較は{ccnt}回でした。')
    print(f'交換は{scnt}回でした。')

if __name__ == '__main__':
    print('シェーカーソート（双方向バブルソート）')
    num = int(input('要素数：'))
    x = [None] * num    # 要素数numの配列を生成

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    shaker_sort(x)      # 配列xを単純交換ソート

    print('昇順にソートしました。')
    for i in range(num):
        print(f'x[{i}]＝{x[i]}')
