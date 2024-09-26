# シェルソート（第２版：h = …, 40, 13, 4, 1）

from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    """シェルソート（第２版）"""
    n = len(a)
    h = 1

    while (h < n // 9):
        h = h * 3 + 1

    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 3

if __name__ == '__main__':
    print('シェルソート（第２版）')
    num = int(input('要素数：'))
    x = [None] * num    # 要素数numの配列を生成

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    shell_sort(x)       # 配列xをシェルソート

    print('昇順にソートしました。')
    for i in range(num):
        print(f'x[{i}]＝{x[i]}')
