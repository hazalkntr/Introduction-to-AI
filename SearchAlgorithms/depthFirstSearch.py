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

def dfs(visited, graph, node, desired):
    
    if node not in visited:
        visited.append(node)
        print('appended: ', node)
            
        if node==desired:
            print('Found !!')
            return visited
        
        for adj in graph[node]:
            dfs(visited, graph, adj, desired)
            
    return visited
            
visited=[]
print('depth first search:')
visited=dfs(visited, graph, 'S', 'G')
print(visited)            