# 10～99の乱数をn個生成（13が生成されたら中断）

import random

n = int(input('乱数は何個：'))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end=' ')
    if r == 13:
        print('\n事情により中断します。')
        break
else:
    print('\n乱数生成終了。')
