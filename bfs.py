graph = {
     'a':['b','c'],
     'b':['a','d'],
     'c':['a','e'],
     'd':['b','e'],
     'e':['c','d','f'],
     'f':['e']
}

start = input("enter start node ").lower() 
visited = [start]
queue = [start]

print("BFS Traversal:", end=" ")

while queue:
    node = queue.pop(0)
    print(node,end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.append(neighbor)
            queue.append(neighbor)

