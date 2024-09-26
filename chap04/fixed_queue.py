# 固定長キュークラス

from typing import Any

class FixedQueue:

    class Empty(Exception):
        """空のFixedQueueに対してdequeあるいはpeekが呼び出されたときに
           送出する例外"""
        pass

    class Full(Exception):
        """満杯のFixedQueueに対してenqueが呼び出されたときに送出する例外"""
        pass

    def __init__(self, capacity: int) -> None:
        """初期化"""
        self.no = 0                    # 現在のデータ数
        self.front = 0                 # 先頭要素カーソル
        self.rear = 0                  # 末尾要素カーソル
        self.capacity = capacity       # キューの容量
        self.que = [None] * capacity   # キューの本体

    def __len__(self) -> int:
        """キューに押し込まれているデータ数を返す"""
        return self.no

    def is_empty(self) -> bool:
        """キューは空であるか"""
        return self.no <= 0

    def is_full(self) -> bool:
        """キューは満杯か"""
        return self.no >= self.capacity

    def enque(self, x: Any) -> None:
        """データxをエンキュー"""
        if self.is_full():
            raise FixedQueue.Full           # キューは満杯
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> Any:
        """データをデキュー"""
        if self.is_empty():
            raise FixedQueue.Empty          # キューは空
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def peek(self) -> Any:
        """データをピーク（先頭データを覗く）"""
        if self.is_empty():
            raise FixedQueue.Empty      # キューは空
        return self.que[self.front]

    def find(self, value: Any) -> Any:
        """キューからvalueを探して添字（見つからなければ-1）を返す"""
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:  # 探索成功
                return idx
        return -1                       # 探索失敗

    def count(self, value: Any) -> bool:
        """キューに含まれるvalueの個数を返す"""
        c = 0
        for i in range(self.no):        # 底側から線形探索
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:  # 探索成功
                c += 1                  # 入っている
        return c

    def __contains__(self, value: Any) -> bool:
        """キューにvalueは含まれているか"""
        return self.count(value)

    def clear(self) -> None:
        """キューを空にする"""
        self.no = self.front = self.rear = 0

    def dump(self) -> None:
        """全データを先頭→末尾の順に表示"""
        if self.is_empty():             # キューは空
            print('キューは空です。')
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end=' ')
            print()
