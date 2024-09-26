# 1からnまでの総和を求める（for文）

print('1からnまでの総和を求めます。')
n = int(input('nの値：'))

sum = 0
for i in range(1, n + 1):
    sum += i   # sumにiを加える

print(f'1から{n}までの総和は{sum}です。')
