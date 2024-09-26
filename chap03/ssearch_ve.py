# 線形探索（for文：探索失敗時にValueErrorを送出）

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """シーケンスaからkeyと等価な要素を線形探索（for文）"""
    for i in range(len(a)):
        if a[i] == key:
            return i    # 探索成功（添字を返却）
    raise ValueError    # 探索失敗

if __name__ == '__main__':
    num = int(input('要素数：'))
    x = [None] * num    # 要素数numの配列を生成

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    ky = int(input('探す値：')) # キーkyの読込み

    try:
        idx = seq_search(x, ky)     # kyと等価な要素をxから探索
    except ValueError:
        print('その値の要素は存在しません。')
    else:
        print(f'それはx[{idx}]にあります。')
