def find_all_topological_sorts(graph):
    n = len(graph)
    
    # Calculate in-degrees
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    # Helper function for DFS
    def dfs(path, visited, all_orders, in_degree):
        if len(path) == n:
            all_orders.append(list(path))  # Store a copy of the current path
            return
        
        # Find all nodes with zero in-degree
        zero_in_degree_nodes = [node for node in graph if in_degree[node] == 0 and not visited[node]]
        
        for node in zero_in_degree_nodes:
            # Mark node as visited and add it to the current path
            visited[node] = True
            path.append(node)
            
            # Decrease the in-degree of all its neighbors
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
            
            # Recursive DFS call
            dfs(path, visited, all_orders, in_degree)
            
            # Backtrack: unmark the node and remove it from the path
            visited[node] = False
            path.pop()
            
            # Restore the in-degrees of all its neighbors
            for neighbor in graph[node]:
                in_degree[neighbor] += 1
    
    all_orders = []
    visited = {node: False for node in graph}
    dfs([], visited, all_orders, in_degree)
    
    return all_orders

# Define the graph
graph = {
    'a': ['b', 'e'],
    'b': ['c', 'f', 'g'],
    'c': ['d', 'g'],
    'd': ['h'],
    'e': ['f'],
    'f': ['g'],
    'g': ['h'],
    'h': []
}

# Find and print all valid topological sorts
all_topological_sorts = find_all_topological_sorts(graph)
print("Number of valid topological orderings:", len(all_topological_sorts))
for order in all_topological_sorts:
    print(order)

