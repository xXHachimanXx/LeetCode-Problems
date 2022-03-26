# docs: https://docs.google.com/document/d/1mkb83sHrXUhwyjFkqzQfyOAxfrBB0IBkZLddTVRuGdY/edit
def findCenter(graph):
    dict = {}
    
    for edge in graph:
        dict[edge[0]] = 0
        dict[edge[1]] = 0

    for edge in graph:

        dict[edge[0]] += 1
        dict[edge[1]] += 1
        if dict[edge[0]] > 1:
            return edge[0]

        
        
        if dict[edge[1]] > 1:
            return edge[1]
        
    return 1

assert findCenter([[1,2],[2,3],[4,2]]) == 2
assert findCenter([[1,2],[5,1],[1,3],[1,4]]) == 1
        