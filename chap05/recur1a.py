# 真に再帰的な関数（末尾再帰を除去）

def recur(n: int) -> int:
    """末尾再帰を除去した関数recur"""
    while n > 0:
        recur(n - 1)
        print(n)
        n = n - 2

x = int(input('整数を入力せよ：'))

recur(x)
