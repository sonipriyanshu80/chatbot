graph ={
    'a':['b','c'],
    'b':['d','e'],
    'c':['a','f'],
    'd':['b'],
    'e':['b','f'],
    'f':['c','e']
}
start = input("Enter the starting node:").lower()
visited = []
stack = [start]

print ("DFS Traversal:", end=" ")

while stack:
    node = stack.pop()
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        
    for neighbor in reversed (graph[node]):
        if neighbor not in visited:
            stack.append(neighbor)
