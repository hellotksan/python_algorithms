# リストの要素の型が揃う必要がないことを確認

x = [15, 64, 7, 3.14, [32, 55], 'ABC']

for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')
