# 右下側が直角の二等辺三角形を表示

print('右下直角の二等辺三角形')
n = int(input('短辺の長さ：'))

for i in range(n):
    for _ in range(n - i - 1):
        print(' ', end='')
    for _ in range(i + 1):
        print('*', end='')
    print()
