# 1から12までを8をスキップして繰り返す（その１）

for i in range(1, 13):
    if i == 8:
        continue
    print(i, end=' ')
print()
