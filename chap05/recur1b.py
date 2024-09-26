# 真に再帰的な関数（再帰を除去）

from stack import Stack

def recur(n: int) -> int:
    """再帰を除去した関数recur"""
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)               # nの値をプッシュ
            n = n - 1
            continue
        if not s.is_empty():        # スタックが空でなければ
            n = s.pop()             # 保存していた値をnにポップ
            print(n)
            n = n - 2
            continue
        break
x = int(input('整数を入力せよ：'))

recur(x)
