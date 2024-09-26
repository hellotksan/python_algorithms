# 文字列に含まれる文字列を探索（find系メソッド）

txt = input('文字列txt：')
ptn = input('文字列ptn：')

c = txt.count(ptn)

if c == 0:                                              # 含まれない
    print('ptnはtxtに含まれません。')
elif c == 1:                                            # １個だけ含まれる
    print('ptnがtxtに含まれるインデックス：', txt.find(ptn))
else:                                                   # ２個以上含まれる
    print('ptnがtxtに含まれる先頭インデックス：', txt.find(ptn))
    print('ptnがtxtに含まれる末尾インデックス：', txt.rfind(ptn))
