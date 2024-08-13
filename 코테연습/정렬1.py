n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
graph = sorted(graph,key=lambda x:(x[1],x[0]))
for i,x in graph:
    print(i,x)