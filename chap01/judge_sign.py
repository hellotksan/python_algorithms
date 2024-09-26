# 読み込んだ整数値の符号を表示

n = int(input('整数：'))

if n > 0:
    print('その値は正です。')
elif n < 0:
    print('その値は負です。')
else:
    print('その値は０です。')
