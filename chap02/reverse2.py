# ミュータブルなシーケンスの要素の並びを反転（変数nを使わない）

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    """ミュータブルなシーケンスaの要素の並びを反転"""
    for i in range(len(a) // 2):
         a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]

if __name__ == '__main__':
    print('配列の要素の並びを反転します。')
    nx = int(input('要素数は：'))
    x = [None] * nx    # 要素数nxのリストを生成

    for i in range(nx):
        x[i] = int(input(f'x[{i}]：'))

    reverse_array(x)   # xの並びを反転

    print('配列の要素の並びを反転しました。')
    for i in range(nx):
        print(f'x[{i}]＝{x[i]}')
