# オープンアドレス法によるハッシュの利用例

from enum import Enum
from open_hash import OpenHash

Menu = Enum('Menu', ['追加', '削除', '探索', 'ダンプ', '終了'])

def select_menu() -> Menu:
    """メニュー選択"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input('：'))
        if 1 <= n <= len(Menu):
            return Menu(n)

hash = OpenHash(13)                             # 容量13のハッシュ表

while True:
    menu = select_menu()                        # メニュー選択

    if menu == Menu.追加:                       # 追加
        key = int(input('キー：'))
        val = input('値：')
        if not hash.add(key, val):
            print('追加失敗！')

    elif menu == Menu.削除:                     # 削除
        key = int(input('キー：'))
        if not hash.remove(key):
            print('削除失敗！')

    elif menu == Menu.探索:                     # 探索
        key = int(input('キー：'))
        t = hash.search(key)
        if t is not None:
            print(f'そのキーをもつ値は{t}です。')
        else:
            print('該当するデータはありません。')

    elif menu == Menu.ダンプ:                   # ダンプ
        hash.dump()

    else:                                       # 終了
        break
