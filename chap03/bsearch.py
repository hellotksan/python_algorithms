# ２分探索

from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    """シーケンスaからkeyと一致する要素を２分探索"""
    pl = 0              # 探索範囲先頭の添字
    pr = len(a) - 1     # 　 〃 　末尾の添字

    while True:
        pc = (pl + pr) // 2     # 中央要素の添字
        if a[pc] == key:
            return pc           # 探索成功
        elif a[pc] < key:
            pl = pc + 1         # 探索範囲を後半に絞り込む
        else:
            pr = pc - 1         # 探索範囲を前半に絞り込む
        if pl > pr:
            break
    return -1                   # 探索失敗

if __name__ == '__main__':
    num = int(input('要素数：'))
    x = [None] * num    # 要素数numの配列を生成

    print('昇順に入力してください。')

    x[0] = int(input('x[0]：'))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]：'))
            if x[i] >= x[i - 1]:
                 break

    ky = int(input('探す値：')) # キーkyの読込み

    idx = bin_search(x, ky)     # kyと等価な要素をxから探索

    if idx == -1:
        print('その値の要素は存在しません。')
    else:
        print(f'その値はx[{idx}]にあります。')
