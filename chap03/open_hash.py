# オープンアドレス法によるハッシュ

from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

# バケットの属性
class Status(Enum):
    OCCUPIED = 0    # データ格納
    EMPTY = 1       # 空
    DELETED = 2     # 削除ずみ

class Bucket:
    """ハッシュを構成するバケット"""

    def __init__(self, key: Any = None, value: Any = None,
                       stat: Status = Status.EMPTY) -> None:
        """初期化"""
        self.key   = key    # キー
        self.value = value  # 値
        self.stat  = stat   # 属性

    def set(self, key: Any, value: Any, stat: Status) -> None:
        """全フィールドに値を設定"""
        self.key   = key    # キー
        self.value = value  # 値
        self.stat  = stat   # 属性

    def set_status(self, stat: Status) -> None:
        """属性を設定"""
        self.stat = stat

class OpenHash:
    """オープンアドレス法を実現するハッシュクラス"""

    def __init__(self, capacity: int) -> None:
        """初期化"""
        self.capacity = capacity                    # ハッシュ表の容量
        self.table = [Bucket()] * self.capacity     # ハッシュ表

    def hash_value(self, key: Any) -> int:
        """ハッシュ値を求める"""
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.md5(str(key).encode()).hexdigest(), 16)
                % self.capacity)

    def rehash_value(self, key: Any) -> int:
        """再ハッシュ値を求める"""
        return (self.hash_value(key) + 1) % self.capacity

    def search_node(self, key: Any) -> Any:
        """キーがkeyであるバケットの探索"""
        hash = self.hash_value(key)     # 探索するキーのハッシュ値
        p = self.table[hash]            # 着目バケット

        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(hash)      # 再ハッシュ
            p = self.table[hash]
        return None

    def search(self, key: Any) -> Any:
        """キーkeyをもつ要素の探索（値を返却）"""
        p = self.search_node(key)
        if p is not None:
            return p.value              # 探索成功
        else:
            return None                 # 探索失敗

    def add(self, key: Any, value: Any) -> bool:
        """ キーがkeyで値がvalueの要素の追加"""
        if self.search(key) is not None:
            return False                # このキーは登録ずみ

        hash = self.hash_value(key)     # 追加するキーのハッシュ値
        p = self.table[hash]            # 着目バケット
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)  # 再ハッシュ
            p = self.table[hash]
        return False                        # ハッシュ表が満杯

    def remove(self, key: Any) -> int:
        """キーkeyをもつ要素の削除"""
        p = self.search_node(key)       # 着目バケット
        if p is None:
            return False                # このキーは登録されていない
        p.set_status(Status.DELETED)
        return True

    def dump(self) -> None:
        """ハッシュ表をダンプ"""
        for i in range(self.capacity):
            print(f'{i:2} ', end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')

            elif self.table[i].stat == Status.EMPTY:
                print('-- 未登録 --')

            elif self.table[i].stat == Status.DELETED:
                print('-- 削除ずみ --')
