# sorted関数によるソート

print('sorted関数によるソート')
num = int(input('要素数：'))
x = [None] * num    # 要素数numの配列を生成

for i in range(num):
    x[i] = int(input(f'x[{i}]：'))

# 配列xを昇順にソート
x = sorted(x)
print('昇順にソートしました。')
for i in range(num):
    print(f'x[{i}]＝{x[i]}')

# 配列xを降順にソート
x = sorted(x, reverse=True)
print('降順にソートしました。')
for i in range(num):
    print(f'x[{i}]＝{x[i]}')
