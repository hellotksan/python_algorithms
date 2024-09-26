# リストの全要素をenumerate関数で走査（1からカウント）

x = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x, 1):
    print(f'{i}番目 = {name}')
