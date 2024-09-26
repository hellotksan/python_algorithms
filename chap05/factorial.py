# 非負の整数の階乗値を求める

def factorial(n: int) -> int:
    """非負の整数nの階乗を再帰的に求める"""
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1

if __name__ == '__main__':
    n = int(input('何の階乗：'))
    print(f'{n}の階乗は{factorial(n)}です。')
