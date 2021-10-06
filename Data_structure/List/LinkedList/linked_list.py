# 포인터로 연결 리스트 구현하기

from __future__ import annotations
from typing import Any, Type


class Node:
    """연결 리스트용 노드클래스"""

    def __init__(self, data: Any = None, next: Node = None):
        """초기화"""
        self.data = data  # 데이터
        self.next = next  # 뒤쪽 포인터


class LinkedList:
    """연결 리스트 클래스"""

    def __init__(self) -> None:
        """초기화"""
        self.no = 0  # 노드의 개수
        self.head = None  # 머리 노드
        self.current = None  # 주목 노드

    def __len__(self) -> int:
        return self.no
