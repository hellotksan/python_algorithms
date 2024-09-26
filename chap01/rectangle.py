# 縦横が整数で面積がareaの長方形の辺の長さを列挙

area = int(input('面積は：'))

for i in range(1, area + 1):
    if i * i > area: break
    if area % i : continue
    print(f'{i}×{area // i}')
