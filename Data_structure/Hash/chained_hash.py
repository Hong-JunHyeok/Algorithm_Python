# 체인법으로 해시 함수 구현하기

from __future__ import annotations
from typing import Any, Type
import hashlib
from enum import Enum


class Node:
    """해시를 구성하는 노드"""

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """초기화"""
        self.key = key  # 키
        self.value = value  # 값
        self.next = next  # 뒤쪽 노드를 참조


class ChainedHash:
    """체인법으로 해시 클래스 구현"""

    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity  # 해시 테이블의 크기를 지정
        self.table = [None] * self.capacity  # 해시 테이블(리스트)을 선언

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        # 정수가 아닌 경우 해시값을 구하는 식
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key: Any) -> Any:
        hash = self.hash_value(key)  # 검색하는 키의 해시값
        p = self.table[hash]  # 노드를 주목

        while p is not None:
            if p.key == key:
                return p.value  # 검색 성공
            p = p.next  # 뒤쪽 노드를 주목

        return None

    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""
        hash = self.hash_value(key)  # 추가하는 key의 해시값
        p = self.table[hash]  # 노드를 주목

        while p is not None:
            if p.key == key:
                return False  # 추가 실패
            p = p.next  # 뒤쪽 노드를 주목

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True

    def remove(self, key: Any) -> bool:
        """키가 key인 원소를 삭제"""
        hash = self.hash_value(key)  # 삭제할 key의 해시값
        p = self.table[hash]  # 노드를 주목
        pp = None

        while p is not None:
            if p.key == key:  # key를 발견하면 아래를 실행
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next  # 뒤쪽 노드를 주목

        return False  # 삭제 실패

    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end="")
            while p is not None:
                print(f'   ->{p.key} ({p.value})', end='')
                p = p.next
            print()


if __name__ == '__main__':
    Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])  # 메뉴를 선언

    def select_menu() -> Menu:
        """메뉴 선택"""
        s = [f'({m.value}){m.name}' for m in Menu]
        while True:
            print(*s, sep='   ', end='')
            n = int(input(': '))
            if 1 <= n <= len(Menu):
                return Menu(n)

    hash = ChainedHash(13)  # 크기가 13인 해시 테이블을 생성

    while True:
        menu = select_menu()  # 메뉴 선택

        if menu == Menu.추가:
            key = int(input('추가할 키를 입력하세요 : '))
            val = input('추가할 값을 입력하세요')
            if not hash.add(key, val):
                print('추가를 실패했습니다.')

        elif menu == Menu.삭제:
            key = int(input('삭제할 키를 입력하세요 : '))
            if not hash.remove(key):
                print('삭제를 실패했습니다.')

        elif menu == Menu.검색:
            key = int(input('검색할 키를 입력하세요 : '))
            t = hash.search(key)

            if t is None:
                print('검색할 데이터가 없습니다.')
            else:
                print(f'검색한 키를 갖는 값은 {t}입니다.')
        elif menu == Menu.덤프:
            hash.dump()

        else:
            break
