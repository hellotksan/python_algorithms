# 記号文字+と-を交互に表示（その２：for文の開始値を1に変更）

print('記号文字+と-を交互に表示します。')
n = int(input('全部で何個：'))

for _ in range(1, n // 2 + 1):
    print('+-', end='')

if n % 2:
    print('+', end='')
print()
