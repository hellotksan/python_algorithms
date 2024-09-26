# 固定長スタッククラス（collections.dequeを利用）

from typing import Any
from collections import deque

class Stack:
    """固定長スタッククラス（collections.dequeを利用）"""

    def __init__(self, maxlen: int = 256) -> None:
        """初期化"""
        self.capacity = maxlen
        self.__stk = deque([], maxlen)

    def __len__(self) -> int:
        """スタックに積まれているデータ数を返す"""
        return len(self.__stk)

    def is_empty(self) -> bool:
        """スタックは空であるか"""
        return not self.__stk

    def is_full(self) -> bool:
        """スタックは満杯か"""
        return len(self.__stk) == self.__stk.maxlen

    def push(self, value: Any) -> None:
        """スタックにvalueをプッシュ"""
        self.__stk.append(value)

    def pop(self) -> Any:
        """スタックからデータをポップ（頂上のデータを取り出す）"""
        return self.__stk.pop()

    def peek(self) -> Any:
        """スタックからデータをピーク（頂上のデータを覗き見）"""
        return self.__stk[-1]

    def clear(self) -> None:
        """スタックを空にする（全データの削除）"""
        self.__stk.clear()

    def find(self, value: Any) -> Any:
        """スタックからvalueを探して添字（見つからなければ-1）を返す"""
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self, value: Any) -> int:
        """スタックに含まれるvalueの個数を返す"""
        return self.__stk.count(value)

    def __contains__(self, value: Any) -> bool:
        """スタックにvalueは含まれているか"""
        return self.count(value)

    def dump(self) -> int:
        """ダンプ（スタック内の全データを底→頂上の順に表示）"""
        print(list(self.__stk))
