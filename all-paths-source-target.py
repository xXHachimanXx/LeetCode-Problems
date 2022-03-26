from collections import deque


def allPathsSourceTarget(graph):
    paths = []
    end = len(graph)-1
    
    def find_all_paths_rec(start, path):
        if start == end:
            paths.append(list(path))
        
        for v in graph[start]: 
            path.append(v)
            find_all_paths_rec(v, path)
            path.pop()

    
    path = deque([0]) # path starts from 0
    find_all_paths_rec(0, path)

    return paths

assert allPathsSourceTarget([[1,2],[3],[3],[]]) == [[0,1,3],[0,2,3]]
assert allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]) == [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]