# チェイン法によるハッシュ

from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    """ハッシュを構成するノード"""

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """初期化"""
        self.key   = key    # キー
        self.value = value  # 値
        self.next  = next   # 後続ノードへの参照

class ChainedHash:
    """チェイン法を実現するハッシュクラス"""

    def __init__(self, capacity: int) -> None:
        """初期化"""
        self.capacity = capacity                # ハッシュ表の容量
        self.table = [None] * self.capacity     # ハッシュ表（リスト）

    def hash_value(self, key: Any) -> int:
        """ハッシュ値を求める"""
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16)
                % self.capacity)

    def search(self, key: Any) -> Any:
        """キーkeyをもつ要素の探索（値を返却）"""
        hash = self.hash_value(key)     # 探索するキーのハッシュ値
        p = self.table[hash]            # 着目ノード

        while p is not None:
            if p.key == key:
                 return p.value         # 探索成功
            p = p.next                  # 後続ノードに着目

        return None                     # 探索失敗

    def add(self, key: Any, value: Any) -> bool:
        """キーがkeyで値がvalueの要素の追加"""
        hash = self.hash_value(key)     # 追加するキーのハッシュ値
        p = self.table[hash]            # 着目ノード

        while p is not None:
            if p.key == key:
                return False            # 追加失敗
            p = p.next                  # 後続ノードに着目

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp         # ノードを挿入
        return True                     # 追加成功

    def remove(self, key: Any) -> bool:
        """キーkeyをもつ要素の削除"""
        hash = self.hash_value(key)     # 削除するキーのハッシュ値
        p = self.table[hash]            # 着目ノード
        pp = None                       # 前回の着目ノード

        while p is not None:
            if p.key == key:            # 見つけたら
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True             # 削除成功
            pp = p
            p = p.next                  # 後続ノードに着目
        return False                    # 削除失敗（keyは存在しない）

    def dump(self) -> None:
        """ハッシュ表をダンプ """
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'  → {p.key} ({p.value})', end='')
                p = p.next
            print()
