# Boyer-Moore法による文字列探索（対象は0～255の文字）

def bm_match(txt: str, pat: str) -> int:
    """Boyer-Moore法による文字列探索"""
    skip = [None] * 256     # スキップテーブル

    # スキップテーブルの作成
    for pt in range(256):
        skip[pt] = len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1

    # 探索
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp \
              else len(pat) - pp

    return -1

if __name__ == '__main__':
    s1 = input('テキスト：')    # テキスト用文字列
    s2 = input('パターン：')    # パターン用文字列

    idx = bm_match(s1, s2)      # 文字列s1から文字列s2をBoyer-Moore法で探索

    if idx == -1:
        print('テキスト中にパターンは存在しません。')
    else:
        print(f'{(idx + 1)}文字目にマッチします。')
