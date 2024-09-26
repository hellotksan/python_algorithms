# シーケンスの要素の最大値を表示する

from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    """シーケンスaの要素の最大値を返却する"""
    maximum = a[0]
    for i in range(1, len(a)):
         if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__ == '__main__':
    print('配列の最大値を求めます。')
    num = int(input('要素数：'))
    x = [None] * num  # 要素数numのリストを生成

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    print(f'最大値は{max_of(x)}です。')
