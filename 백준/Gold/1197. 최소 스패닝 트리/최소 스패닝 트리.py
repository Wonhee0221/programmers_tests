"""
1.아이디어
- MST 기본문제, 외우기
- 간선을 인접리스트에 집어넣기
- 힙에 시작점 넣기
- 힙이 빌때까지 다음의 작업을 반복
 -  힙의 최소값 꺼내서, 해당 노드 방문을 안했다면
  - 방문표시, 해당 비용 추가, 연결된 간선들 힙에 넣어주기
  
2.시간복잡도
O(ElogE)
3.자료구조
- 간선저장되는 인접리스트 : (무게 ,노드번호)
- 힙( 무게, 노드번호)
- 방문 여부 : bool[]
- 결과값 int
"""
import sys, heapq
input = sys.stdin.readline

V,E = map(int,input().split())
edge = [[] for _ in range(V+1)]
chk = [False] * (V+1)
rs = 0
for i in range(E):
  a,b,c = map(int,input().split())
  edge[a].append([c,b])
  edge[b].append([c,a])

heap = [[0,1]]
while heap:
  w, node_num = heapq.heappop(heap)
  if chk[node_num] == False:
    chk[node_num] = True
    rs += w
    for next_edgs in edge[node_num]:
      if chk[next_edgs[1]] == False:
        heapq.heappush(heap,next_edgs)
print(rs)