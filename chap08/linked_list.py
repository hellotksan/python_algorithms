# 線形リスト

from __future__ import annotations
from typing import Any, Type

class Node:
    """線形リスト用ノードクラス"""

    def __init__(self, data: Any = None, next: Node = None):
        """初期化"""
        self.data = data    # データ
        self.next = next    # 後続ポインタ

class LinkedList:
    """線形リストクラス"""

    def __init__(self) -> None:
        """初期化"""
        self.no = 0           # ノードの個数
        self.head = None      # 先頭ノード
        self.current = None   # 着目ノード

    def __len__(self) -> int:
        """線形リスト上のノード数を返却する"""
        return self.no

    def search(self, data: Any) -> int:
        """dataと等価なノードを探索"""
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data: Any) -> bool:
        """線形リストにdataは含まれているか"""
        return self.search(data) >= 0

    def add_first(self, data: Any) -> None:
        """先頭にノードを挿入"""
        ptr = self.head                     # 挿入前の先頭ノード
        self.head = self.current = Node(data, ptr)
        self.no += 1

    def add_last(self, data: Any):
        """末尾にノードを挿入"""
        if self.head is None:               # リストが空であれば
            self.add_first(data)            # 先頭に挿入
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(data, None)
            self.no += 1

    def remove_first(self) -> None:
        """先頭ノードを削除"""
        if self.head is not None:           # リストが空でなければ
            self.head = self.current = self.head.next
        self.no -= 1

    def remove_last(self):
        """末尾ノードを削除"""
        if self.head is not None:
            if self.head.next is None:      # ノードが１個だけであれば
                self.remove_first()         # 先頭ノードを削除
            else:
                ptr = self.head             # 走査中のノード
                pre = self.head             # 走査中のノードの先行ノード

                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next
                pre.next = None             # preは削除後の末尾ノード
                self.current = pre
                self.no -= 1

    def remove(self, p: Node) -> None:
        """ノードpを削除"""
        if self.head is not None:
            if p is self.head:              # pが先頭ノードであれば
                self.remove_first()         # 先頭ノードを削除
            else:
                ptr = self.head

                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return              # ptrはリスト上に存在しない
                ptr.next = p.next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        """着目ノードを削除"""
        self.remove(self.current)

    def clear(self) -> None:
        """全ノードを削除"""
        while self.head is not None:        # 空になるまで
            self.remove_first()             # 先頭ノードを削除
        self.current = None
        self.no = 0

    def next(self) -> bool:
        """着目ノードを一つ後方に進める"""
        if self.current is None or self.current.next is None:
            return False                    # 進めることはできなかった
        self.current = self.current.next
        return True

    def print_current_node(self) -> None:
        """着目ノードを表示"""
        if self.current is None:
            print('着目ノードはありません。')
        else:
            print(self.current.data)

    def print(self) -> None:
        """全ノードを表示"""
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

    def __iter__(self) -> LinkedListIterator:
        """イテレータを返却"""
        return LinkedListIterator(self.head)

class LinkedListIterator:
    """クラスLinkedListのイテレータ用クラス"""

    def __init__(self, head: Node):
        self.current = head

    def __iter__(self) -> LinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data
