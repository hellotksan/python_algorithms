# ユークリッドの互除法によって最大公約数を求める

def gcd(x: int, y: int) -> int:
    """整数値xとyの最大公約数を求めて返却"""
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

if __name__ == '__main__':
    print('二つの整数の最大公約数を求めます。')
    x = int(input('整数：'))
    y = int(input('整数：'))

    print(f'最大公約数は{gcd(x, y)}です。')
