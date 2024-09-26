# 線形探索を行う関数seq_searchの利用例（その２）

from ssearch_while import seq_search

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{t}中の5.6の添字は{seq_search(t, 5.6)}です。')
print(f'{s}中の"n"の添字は{seq_search(s, "n")}です。')
print(f'{a}中の"DTS"の添字は{seq_search(a, "DTS")}です。')
