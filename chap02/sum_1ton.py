# 1からnまでの総和を求めるプログラム

def sum_1ton(n):
    """1からnまでの整数の総和を求める"""
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s

x = int(input('xの値：'))
print(f'1から{x}までの総和は{sum_1ton(x)}です。')
