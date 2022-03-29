from collections import deque

def bfs(graph, start,visited):
  queue = deque([start])
  
  visited[start] = True

  # 큐가 빌 때까지
  while queue:
    v = queue.popleft()
    print(v, end='')

    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

# 각 노드에 연결된 그래프 정보를 2차원 리스트로 표현
graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)
