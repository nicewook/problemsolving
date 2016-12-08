"""
허민석님 원래코드 https://github.com/minsuk-heo/problemsolving/blob/master/graph/bfs.py
1. 노드들이 있음. vertexList // vertex는 꼭지점
2. 노드들의 방향(direction) edgeList
3. 인접 목록 adjacencyList
"""

testVertexList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
testEdgeList = [(0, 1), (1, 2), (1, 3), (3, 4), (4, 5), (1, 6)]
graphs = (testVertexList, testEdgeList)

def bfs(graph, start):
    print()
    print("start=", start)
    vertexList, edgeList = graph
    visitedList = []
    queue = [start] #시작점을 넣어둔다

    # 일단 adjacencyList에 배열들의 갯수를 꼭지점(vertex) 갯수만큼 만들어둔다.
    # 배열의 배열인 셈인데 나중에 첫 배열에는 0 꼭지점이 가리키는 꼭지점들이 쌓이게 된다.
    # 마찬가지로 두번째 배열에는 1 꼭지점이 가리키는 꼭지점들을 쌓는다
    # vertex는 ABCDEFG 7개로 해뒀으니 총 7개의 배열을 가지게 된다. 근데 알파벳은 여기선 별 의미 없겠다. 그냥 개수가 의미
    adjacencyList = [[] for vertex in vertexList]
    print("adjacencyList1", adjacencyList)

    #adjacencyList 채우기
    #이제 꼭지점들이 다른 꼭지점들을 가리키는 정보를 담은 edgeList를 가지고 adjancencyList를 채운다.
    #예를 들어 edge가 (0,1)이면 adjancencyList의 0번째 배열에 1을 추가하라는 것 = 0 꼭지점이 가리키는 꼭지점 정보들 저장
    #최종적으로 첫배열에는 0꼭지가 가리키는 꼭지들, 두번째 배열에는 1꼭지가 가리키는 꼭지들
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])
    print("adjacencyList2", adjacencyList)


    #bfs: Breadth First Search
    # http://programbasic.tistory.com/521

    while(queue):
        current = queue.pop()
        for neighber in adjacencyList[current]:
            print("current:", current, "neighber:", neighber)
            if not neighber in visitedList:
                queue.insert(0, neighber)
        visitedList.append(current)
    print(visitedList)
    return visitedList

print("start = 0", bfs(graphs, 0))
print("start = 1", bfs(graphs, 1))
print("start = 2", bfs(graphs, 2))
print("start = 3", bfs(graphs, 3))

