# 1,000以下の素数を列挙（第３版の別解：配列primeの要素数を事前に決定しない）

counter = 0             # 乗除算の回数
prime = [2, 3]          # 素数を格納する配列

for n in range(5, 1001, 2):       # 対象は奇数のみ
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:     # 割り切れると素数ではない
            break                 # それ以上の繰返しは不要
        i += 1
    else:                         # 最後まで割り切れなかったら
        prime += [n]              # 素数として配列に追加
        counter += 1

for i in prime:                   # 求めた素数を表示
    print(i)
print(f'乗除算を行った回数：{counter}')
