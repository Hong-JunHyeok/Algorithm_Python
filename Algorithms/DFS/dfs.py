# DFS 메서드 정의
def dfs(graph, v, visited):
  # 현재 노드를 방문 처리
  visited[v] = True
  print(v ,'-> ' , end='')

  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
    

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

# 방문 정보 스택
visited = [False] * 9

dfs(graph, 1, visited)
