# 非負の整数の階乗値を求める（nが負であればValueErrorを送出）

def factorial(n: int) -> int:
    """非負の整数nの階乗を再帰的に求める（nが負であればValueErrorを送出）"""
    if n > 0:
        return n * factorial(n - 1)
    elif n == 0:
        return 1
    else:
        raise ValueError

if __name__ == '__main__':
    n = int(input('何の階乗：'))
    try:
        print(f'{n}の階乗は{factorial(n)}です。')
    except ValueError:
        print(f'{n}の階乗は求められませんでした。')
