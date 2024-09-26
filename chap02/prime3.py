# 1,000以下の素数を列挙（第３版）

counter = 0             # 乗除算の回数
ptr = 0                 # 得られた素数の個数
prime = [None] * 500    # 素数を格納する配列

prime[ptr] = 2          # ２は素数である
ptr += 1
prime[ptr] = 3          # ３は素数である
ptr += 1

for n in range(5, 1001, 2):       # 対象は奇数のみ
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:     # 割り切れると素数ではない
            break                 # それ以上の繰返しは不要
        i += 1
    else:                         # 最後まで割り切れなかったら
        prime[ptr] = n            # 素数として配列に登録
        ptr += 1
        counter += 1

for i in range(ptr):              # 求めたptr個の素数を表示
    print(prime[i])
print(f'乗除算を行った回数：{counter}')
