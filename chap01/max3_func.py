# 三つの整数値の最大値を求めて表示（すべての大小関係に対して確認）

def max3(a, b, c):
    """a, b, cの最大値を求めて返却"""
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum

print(f'max3(3, 2, 1) = {max3(3, 2, 1)}')   # [A] a＞b＞c
print(f'max3(3, 2, 2) = {max3(3, 2, 2)}')   # [B] a＞b＝c
print(f'max3(3, 1, 2) = {max3(3, 1, 2)}')   # [C] a＞c＞b
print(f'max3(3, 2, 3) = {max3(3, 2, 3)}')   # [D] a＝c＞b
print(f'max3(2, 1, 3) = {max3(2, 1, 3)}')   # [E] c＞a＞b
print(f'max3(3, 3, 2) = {max3(3, 3, 2)}')   # [F] a＝b＞c
print(f'max3(3, 3, 3) = {max3(3, 3, 3)}')   # [G] a＝b＝c
print(f'max3(2, 2, 3) = {max3(2, 2, 3)}')   # [H] c＞a＝b
print(f'max3(2, 3, 1) = {max3(2, 3, 1)}')   # [I] b＞a＞c
print(f'max3(2, 3, 2) = {max3(2, 3, 2)}')   # [J] b＞a＝c
print(f'max3(1, 3, 2) = {max3(1, 3, 2)}')   # [K] b＞c＞a
print(f'max3(2, 3, 3) = {max3(2, 3, 3)}')   # [L] b＝c＞a
print(f'max3(1, 2, 3) = {max3(1, 2, 3)}')   # [M] c＞b＞a
