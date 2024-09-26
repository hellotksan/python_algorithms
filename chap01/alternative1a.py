# 記号文字+と-を交互に表示（その１：for文の開始値を1に変更）

print('記号文字+と-を交互に表示します。')
n = int(input('全部で何個：'))

for i in range(1, n + 1):
    if i % 2:               # 奇数
        print('+', end='')
    else:                   # 偶数
        print('-', end='')
print()
