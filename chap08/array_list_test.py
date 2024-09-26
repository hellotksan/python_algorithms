# 配列版線形リストクラスArrayLinkedListの利用例

from enum import Enum
from array_list import ArrayLinkedList

Menu = Enum('Menu', ['先頭に挿入', '末尾に挿入', '先頭を削除', '末尾を削除',
                     '着目を表示', '着目を進める', '着目を削除', '全削除',
                     '探索', '帰属性判定', '全ノードを表示', '走査', '終了'])

def select_Menu() -> Menu:
    """メニュー選択"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input('：'))
        if 1 <= n <= len(Menu):
            return Menu(n)

lst = ArrayLinkedList(100)                       # 線形リストを生成

while True:
    menu = select_Menu()                         # メニュー選択

    if menu == Menu.先頭に挿入:                  # 先頭に挿入
        lst.add_first(int(input('値：')))

    elif menu == Menu.末尾に挿入:                # 末尾に挿入
        lst.add_last(int(input('値：')))

    elif menu == Menu.先頭を削除:                # 先頭を削除
        lst.remove_first()

    elif menu == Menu.末尾を削除:                # 末尾を削除
        lst.remove_last()

    elif menu == Menu.着目を表示:                # 着目を表示
        lst.print_current_node()

    elif menu == Menu.着目を進める:              # 着目を進める
        lst.next()

    elif menu == Menu.着目を削除:                # 着目を削除
        lst.remove_current_node()

    elif menu == Menu.全削除:                    # 全削除
        lst.clear()

    elif menu == Menu.探索:                      # 探索
        pos = lst.search(int(input('値：')))
        if pos >= 0:
            print(f'そのキーをもつデータは{pos + 1}番目にあります。')
        else:
            print('該当するデータはありません。')

    elif menu == Menu.帰属性判定:                # 帰属性判定
        print('その値のデータは含まれま'
              + ('す。' if int(input('値：')) in lst else 'せん。'))

    elif menu == Menu.全ノードを表示:            # 全ノードを表示
        lst.print()

    elif menu == Menu.走査:                      # 全ノードを走査
        for e in lst:
             print(e)

    else:                                        # 終了
        break
