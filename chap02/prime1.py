# 1,000以下の素数を列挙（第１版）

counter = 0         # 除算の回数

for n in range(2, 1001):
    for i in range(2, n):
        counter += 1
        if n % i == 0:  # 割り切れると素数ではない
            break       # それ以上の繰返しは不要
    else:           # 最後まで割り切れなかった
        print(n)
print(f'除算を行った回数：{counter}')
