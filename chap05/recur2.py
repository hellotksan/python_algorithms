# 真に再帰的な関数（呼出しが逆）

def recur(n: int) -> int:
    """真に再帰的な関数recur"""
    if n > 0:
        recur(n - 2)
        print(n)
        recur(n - 1)

x = int(input('整数を入力せよ：'))

recur(x)
