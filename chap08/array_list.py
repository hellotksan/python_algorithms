# 線形リスト（配列カーソル版）

from __future__ import annotations
from typing import Any, Type

Null = -1

class Node:
    """線形リスト用ノードクラス（配列カーソル版）"""

    def __init__(self, data = Null, next = Null, dnext = Null):
        """初期化"""
        self.data  = data   # データ
        self.next  = next   # リストの後続ポインタ
        self.dnext = dnext  # フリーリストの後続ポインタ

class ArrayLinkedList:
    """線形リストクラス（配列カーソル版）"""

    def __init__(self, capacity: int):
        """初期化"""
        self.head = Null            # 先頭ノード
        self.current = Null         # 着目ノード
        self.max = Null             # 利用中の末尾レコード
        self.deleted = Null         # フリーリストの先頭ノード
        self.capacity = capacity    # リストの容量
        self.n = [Node()] * self.capacity     # リスト本体
        self.no = 0

    def __len__(self) -> int:
        """線形リスト上のノード数を返却する"""
        return self.no

    def get_insert_index(self):
        """次に挿入するレコードの添字を求める"""
        if self.deleted == Null:            # 削除レコードは存在しない
            if self.max < self.capacity:
                self.max += 1
                return self.max             # 新しいレコードを利用
            else:
                return Null                 # 容量オーバ
        else:
            rec = self.deleted                  # フリーリストから
            self.deleted = self.n[rec].dnext    # 先頭recを取り出す
            return rec

    def delete_index(self, idx: int) -> None:
        """レコードidxをフリーリストに登録"""
        if self.deleted == Null:            # 削除レコードは存在しない
            self.deleted = idx              # idxをフリーリストの
            self.n[idx].dnext = Null        # 先頭に登録
        else:
            rec = self.deleted              # idxをフリーリストの
            self.deleted = idx              # 先頭に挿入
            self.n[rec].dnext = rec

    def search(self, data: Any) -> int:
        """dataと等価なノードを探索"""
        cnt = 0
        ptr = self.head                     # 現在走査中のノード
        while ptr != Null:
            if self.n[ptr].data == data:
                self.current = ptr
                return cnt                  # 探索成功
            cnt += 1
            ptr = self.n[ptr].next          # 後続ノードに着目
        return Null                         # 探索失敗

    def __contains__(self, data: Any) -> bool:
        """線形リストにdataは含まれているか"""
        return self.search(data) >= 0

    def add_first(self, data: Any):
        """先頭にノードを挿入"""
        ptr = self.head                     # 挿入前の先頭ノード
        rec = self.get_insert_index()
        if rec != Null:
            self.head = self.current = rec  # 第recレコードに挿入
            self.n[self.head] = Node(data, ptr)
            self.no += 1

    def add_last(self, data: Any) -> None:
        """末尾にノードを挿入"""
        if self.head == Null:               # リストが空であれば
            self.add_first(data)            # 先頭に挿入
        else:
            ptr = self.head
            while self.n[ptr].next != Null:
                ptr = self.n[ptr].next
            rec = self.get_insert_index()
            if rec != Null:                # 第recレコードに挿入
                self.n[ptr].next = self.current = rec
                self.n[rec] = Node(data)
                self.no += 1

    def remove_first(self) -> None:
        """先頭ノードを削除"""
        if self.head != Null:              # リストが空でなければ
            ptr = self.n[self.head].next
            self.delete_index(self.head)
            self.head = self.current = ptr
            self.no -= 1

    def remove_last(self) -> None:
        """末尾ノードを削除"""
        if self.head != Null:
            if self.n[self.head].next == Null:  # ノードが１個だけであれば
                self.remove_first()             # 先頭ノードを削除
            else:
                ptr = self.head     # 走査中のノード
                pre = self.head     # 走査中のノードの先行ノード

                while self.n[ptr].next != Null:
                    pre = ptr
                    ptr = self.n[ptr].next
                self.n[pre].next = Null     # preは削除後の末尾ノード
                self.delete_index(pre)
                self.current = pre
                self.no -= 1

    def remove(self, p: int) -> None:
        """レコードpを削除"""
        if self.head != Null:
            if p == self.head:          # pが先頭ノードであれば
                self.remove_first()     # 先頭ノードを削除
            else:
                ptr = self.head

                while self.n[ptr].next != p:
                    ptr = self.n[ptr].next
                    if ptr == Null:
                        return          # pはリスト上に存在しない
                self.n[ptr].next = Null
                self.delete_index(ptr)
                self.n[ptr].next = self.n[p].next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        """着目ノードを削除"""
        self.remove(self.current)

    def clear(self) -> None:
        """全ノードを削除"""
        while self.head != Null:    # 空になるまで
            self.remove_first()     # 先頭ノードを削除
        self.current = Null

    def next(self) -> bool:
        """着目ノードを一つ後方に進める"""
        if self.current == Null or self.n[self.current].next == Null:
            return False            # 進めることはできなかった
        self.current = self.n[self.current].next
        return True

    def print_current_node(self) -> None:
        """着目ノードを表示"""
        if self.current == Null:
            print('着目ノードはありません。')
        else:
            print(self.n[self.current].data)

    def print(self) -> None:
        """全ノードを表示"""
        ptr = self.head

        while ptr != Null:
            print(self.n[ptr].data)
            ptr = self.n[ptr].next

    def dump(self) -> None:
        """配列をダンプ"""
        for i in self.n:
            print(f'[{i}]  {i.data} {i.next} {i.dnext}')

    def __iter__(self) -> ArrayLinkedListIterator:
        """イテレータを返却"""
        return ArrayLinkedListIterator(self.n, self.head)

class ArrayLinkedListIterator:
    """クラスArrayLinkedListのイテレータ用クラス"""

    def __init__(self, n: int, head: int):
        self.n = n
        self.current = head

    def __iter__(self) -> ArrayLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current == Null:
            raise StopIteration
        else:
            data = self.n[self.current].data
            self.current = self.n[self.current].next
            return data
