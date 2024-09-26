# aからbまでの総和を求める（求める過程の式も表示：その２）

print('aからbまでの総和を求めます。')
a = int(input('整数a：'))
b = int(input('整数b：'))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b):
    print(f'{i} + ', end='')
    sum += i        # sumにiを加える

print(f'{b} = ', end='')
sum += b            # sumにbを加える

print(sum)
