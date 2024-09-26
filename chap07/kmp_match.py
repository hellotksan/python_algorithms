# KMP法による文字列探索

def kmp_match(txt: str, pat: str) -> int:
    """KMP法による文字列探索"""
    pt = 1          # txtをなぞるカーソル
    pp = 0          # patをなぞるカーソル
    skip = [0] * (len(pat) + 1)     # スキップテーブル

    # スキップテーブルの作成
    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]

    # 探索
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]

    return pt - pp if pp == len(pat) else -1

if __name__ == '__main__':
    s1 = input('テキスト：')    # テキスト用文字列
    s2 = input('パターン：')    # パターン用文字列

    idx = kmp_match(s1, s2)     # 文字列s1から文字列s2をKMP法で探索

    if idx == -1:
        print('テキスト中にパターンは存在しません。')
    else:
        print(f'{(idx + 1)}文字目にマッチします。')
