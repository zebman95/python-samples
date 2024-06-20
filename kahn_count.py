def count_all_topological_sorts(graph):
    # Calculate in-degrees
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    # List to store the current path and all paths
    current_path = []
    all_orders = []
    
    # Helper function to perform backtracking using Kahn's algorithm
    def kahn_backtrack(current_path, in_degree):
        zero_in_degree_nodes = [node for node in in_degree if in_degree[node] == 0]
        
        # If no nodes with zero in-degree, check if the current path is a complete topological sort
        if not zero_in_degree_nodes:
            if len(current_path) == len(graph):
                all_orders.append(current_path.copy())
            return
        
        for node in zero_in_degree_nodes:
            # Include this node in the current path
            current_path.append(node)
            
            # Temporarily reduce the in-degree of its neighbors
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
            
            # Remove the node from the in-degree map to prevent revisiting
            in_degree.pop(node)
            
            # Recursive call
            kahn_backtrack(current_path, in_degree)
            
            # Backtrack: restore the in-degrees and remove the node from the current path
            for neighbor in graph[node]:
                in_degree[neighbor] += 1
            in_degree[node] = 0
            current_path.pop()
    
    kahn_backtrack(current_path, in_degree)
    
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

# Count all valid topological sorts
all_topological_sorts = count_all_topological_sorts(graph)
print("Number of valid topological orderings:", len(all_topological_sorts))
for order in all_topological_sorts:
    print(order)

