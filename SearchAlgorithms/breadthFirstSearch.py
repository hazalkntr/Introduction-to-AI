graph = {
    'S' : ['A','C'],
    'A' : ['D', 'B'],
    'C' : ['E','G'],
    'D' : ['F','H'],
    'B' : [],
    'E' : ['I'],
    'G' : [],
    'F' : [],
    'H' : [],
    'I' : []
}

def bfs(visited, queue, graph, node, desired):
    visited.append(node)
    queue.append(node)
    
    while queue:
        popped= queue.pop(0)
        print('popped: ', popped)
        
        for adj in graph[popped]:
            if adj not in visited:
                queue.append(adj)
                visited.append(adj)
                
                if adj==desired:
                    print('Found !!')
                    return visited
                    

    return visited
    
    
    
visited=[]
queue=[]
print("breadth first search:")
visited=bfs(visited, queue, graph, 'S', 'I')
print(visited)