# 오픈 주소법으로 해시 함수 구현하기

from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

# 버킷의 속성


class Status(Enum):
    OCCUPIED = 0  # 데이터를 저장
    EMPTY = 1  # 비어 있음
    DELETED = 2  # 삭제 완료


class Bucket:
    """해시를 구성하는 버킷"""

    def __init__(self, key: Any = None, value: Any = None, stat: Status = Status.EMPTY) -> None:
        """초기화"""
        self.key = key
        self.value = value
        self.stat = stat

    def set(self, key: Any, value: Any, stat: Status) -> None:
        """모든 필드에 값을 설정"""
        self.key = key
        self.value = value
        self.stat = stat

    def set_status(self, stat: Status) -> None:
        """속성을 설정"""
        self.stat = stat


class OpenHash:
    """오픈 주소법으로 구현하는 해시 클래스"""

    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity
        self.table = [Bucket()] * self.capacity

    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def rehash_value(self, key: Any) -> int:
        """재해시값을 구함"""
        return(self.hash_value(key) + 1) % self.capacity
