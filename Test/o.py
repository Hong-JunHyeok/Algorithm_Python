class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Queue가 생성될 때 호출됩니다. 기본 데이터를 생성합니다."""

        # 최대로 입력받을 수 있는 요소의 갯수
        self._cap = ArrayQueue.DEFAULT_CAPACITY
        # 최대 입력 갯수만큼 공간을 미리 확보해서 _data를 생성합니다.
        self._data = [None] * self._cap
        # 처음 생성시 Queue안에 요소는 0개입니다.
        self._size = 0
        # 첫번째 요소의 _data 내 index는 0부터 시작합니다.
        self._front = 0

    def __len__(self):
        """Queue 안의 요소 갯수를 반환합니다.
        len(변수) 로 사용할 때 이 함수가 호출됩니다."""

        return self._size

    def is_empty(self):
        """Queue가 비어있는지 여부를 반환합니다."""

        return self._size == 0

    def first(self):
        """Queue의 첫번째 요소를 반환합니다. (제거하지는 않습니다.)
        Queue가 비어있다면, 오류가 발생합니다."""

        # 현재 Queue가 비어있다면
        if self.is_empty():
            # 오류 발생
            raise AssertionError('Queue is empty')

        # 첫번째 요소 반환
        return self._data[self._front]

    def enqueue(self, e):
        """Queue의 끝에 새 요소(e)를 추가합니다."""

        # Queue 사이즈가 가득찼을 경우 늘려주기
        if self._size == self._cap:
            self.resize(2 * self._cap)

        # TODO: 현재 Queue에 다음 요소를 넣을 위치 찾기
        current = self._size
        # TODO: 해당 위치에 요소 넣기
        self._data[current] = e
        # Queue 요소 갯수 반영
        self._size += 1

    def dequeue(self):
        """Queue의 첫번째 요소를 반환하면서 동시에 삭제합니다. (FIFO)
        Queue가 비어있다면, 오류를 발생합니다."""

        # TODO: 현재 Queue가 비어있다면 오류
        if self.is_empty():
            raise AssertionError('Queue is empty')
        # TODO: answer = 첫번째 요소
        answer = self.first()
        # TODO: 원래 첫번째 요소 위치에 None 값 넣기
        self._data[self._front] = None
        # TODO: _front 변수가 다음 요소를 가리키도록 업데이트
        if self._front + 1 == self._data:
            self._front = 0
        else:
            self._front += 1

        # Queue 요소 갯수 반영
        self._size -= 1

        return answer

    def _resize(self, cap):
        """Queue의 capacity를 조정합니다.
        cap >= len(self), 즉 새 capacity가 현재 보다는 항상 큰 것으로 가정합니다."""

        # 기존 데이터를 옮겨둠
        old = self._data
        # _data를 새 크기만큼 새로 할당
        self._data = [None] * cap
        # 현재 최대크기 변수 값 반영
        self._cap = cap

        # 기존 데이터를 새 _data로 옮기기
        # walk: 기존 데이터의 첫번째 index부터 순서대로 다음
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

    def print_contents(self):
        print('Queue content:',
              self._data[self._front:self._front + self._size])


if __name__ == '__main__':
    print('=== Queue 생성 및 5, 3 추가')
    Q = ArrayQueue()
    Q.enqueue(5)
    Q.enqueue(3)
    Q.print_contents()

    print()
    print('len:', len(Q))
    print('dequeue:', Q.dequeue())
    print('is_empty:', Q.is_empty())
    print('dequeue:', Q.dequeue())
    print('is_empty:', Q.is_empty())

    print()
    print('=== Queue 에 2, 8 추가')
    Q.enqueue(2)
    Q.enqueue(8)
    Q.print_contents()

    print('first:', Q.first())
    print('dequeue:', Q.dequeue())
    Q.print_contents()
    print('dequeue:', Q.dequeue())
    Q.print_contents()
