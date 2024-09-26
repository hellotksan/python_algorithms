# 線形探索（while文）

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """シーケンスaからkeyと等価な要素を線形探索（while文）"""
    i = 0

    while True:
        if i == len(a):
            return -1   # 探索失敗（-1を返却）
        if a[i] == key:
            return i    # 探索成功（添字を返却）
        i += 1

if __name__ == '__main__':
    num = int(input('要素数：'))
    x = [None] * num    # 要素数numの配列を生成

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    ky = int(input('探す値：')) # キーkyの読込み

    idx = seq_search(x, ky)     # kyと等価な要素をxから探索

    if idx == -1:
        print('その値の要素は存在しません。')
    else:
        print(f'それはx[{idx}]にあります。')
