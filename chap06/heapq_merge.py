# ソートずみ配列のマージ（heap.meregeを利用）

import heapq

a = [2, 4, 6, 8, 11, 13]
b = [1, 2, 3, 4, 9, 16, 21]
c = list(heapq.merge(a, b))              # 配列aとbをマージしてcに格納

print('配列aとbをマージして配列cに格納しました。')
print(f'配列a：{a}')
print(f'配列b：{b}')
print(f'配列c：{c}')
