# 配列の要素の最大値を求めて表示（タプル／文字列／文字列のリスト）

from max import max_of

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{t}の最大値は{max_of(t)}です。')
print(f'{s}の最大値は{max_of(s)}です。')
print(f'{a}の最大値は{max_of(a)}です。')
