# ハノイの塔

def move(no: int, x: int, y: int) -> None:
    """no枚の円盤をx軸からy軸へ移動"""
    if no > 1:
        move(no - 1, x, 6 - x - y)

    print(f'円盤[{no}]を{x}軸から{y}軸へ移動')

    if no > 1:
        move(no - 1, 6 - x - y, y)

print('ハノイの塔')
n = int(input('円盤の枚数：'))

move(n, 1, 3)   # 第1軸に積まれたn枚を第3軸に移動
