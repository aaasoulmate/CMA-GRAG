"""
This .py file defines two functions, Wfun and Dfun, for traversing a graph represented in a JSON structure.

- Wfun: Performs a breadth-first search (BFS) from a given node to find all connected nodes within a certain depth, returning their IDs and explanations.
- Dfun: Performs a BFS from a given node to find the edge content of connections within a certain depth, returning the starting node, the edge content, and the connected node.

The graph consists of nodes and edges, with nodes represented by their IDs and explanations, and edges represented by the connection between nodes and their content. The graph is treated as undirected, meaning edges are traversable in both directions.

The input data is passed as a JSON object, and the graph is built using adjacency lists within each function.
"""

from collections import deque

# Define Wfun function
def Wfun(data, node_id, alpha):
    """
    Performs a breadth-first search from a given node to find all connected nodes 
    within a certain depth (alpha), returning their IDs and explanations.
    
    Parameters:
    - data: JSON structure containing nodes and edges
    - node_id: ID of the starting node
    - alpha: Maximum depth for the BFS traversal
    """
    # Build node and graph structure
    nodes = {node['id']: node for node in data['nodes']}
    graph = {}
    for edge in data['edges']:
        node_ids = edge['id'].split('to')
        if len(node_ids) != 2:
            continue
        n1, n2 = int(node_ids[0]), int(node_ids[1])
        graph.setdefault(n1, []).append(n2)
        graph.setdefault(n2, []).append(n1)  # Assume undirected graph

    # BFS to find connected nodes
    visited = {node_id: 0}  # Track visited nodes with their depths
    queue = deque([node_id])  # Queue for BFS
    result = []

    while queue:
        current = queue.popleft()  # Get current node
        depth = visited[current]
        if depth > alpha:  # Stop if depth exceeds alpha
            continue
        node_info = nodes[current]  # Get node info
        result.append((current, node_info['explanation']))  # Store (id, explanation)
        for neighbor in graph.get(current, []):  # Explore neighbors
            if neighbor not in visited or visited[neighbor] > depth + 1:
                visited[neighbor] = depth + 1  # Update depth
                queue.append(neighbor)  # Add to queue for further exploration
    return result

# Define Dfun function
def Dfun(data, node_id, alpha):
    """
    Performs a breadth-first search from a given node to find the edge content 
    of connections within a certain depth (alpha), returning the starting node, 
    the edge content, and the connected node.
    
    Parameters:
    - data: JSON structure containing nodes and edges
    - node_id: ID of the starting node
    - alpha: Maximum depth for the BFS traversal
    """
    # Build node and edge structure
    nodes = {node['id']: node for node in data['nodes']}
    edges = {}
    graph = {}
    for edge in data['edges']:
        node_ids = edge['id'].split('to')
        if len(node_ids) != 2:
            continue
        n1, n2 = int(node_ids[0]), int(node_ids[1])
        content = edge['content']
        edges[(n1, n2)] = content
        edges[(n2, n1)] = content  # Assume undirected graph
        graph.setdefault(n1, []).append(n2)
        graph.setdefault(n2, []).append(n1)

    # BFS to find connected nodes and edge content
    visited = {node_id: 0}  # Track visited nodes with their depths
    queue = deque([node_id])  # Queue for BFS
    result = []

    while queue:
        current = queue.popleft()  # Get current node
        depth = visited[current]
        if depth > alpha - 1:  # Stop if depth exceeds alpha-1
            continue
        for neighbor in graph.get(current, []):  # Explore neighbors
            if neighbor not in visited or visited[neighbor] > depth + 1:
                visited[neighbor] = depth + 1  # Update depth
                queue.append(neighbor)  # Add to queue
                edge_content = edges.get((current, neighbor))  # Get edge content
                if edge_content:
                    result.append((node_id, edge_content, neighbor))
    return result

if __name__ == '__main__':
    # Sample data
    data = {
        "nodes": [
            {"id": 1, "name": "Node 1", "explanation": "This is the explanation for Node 1"},
            {"id": 2, "name": "Node 2", "explanation": "This is the explanation for Node 2"},
            {"id": 3, "name": "Node 3", "explanation": "This is the explanation for Node 3"},
            {"id": 4, "name": "Node 4", "explanation": "This is the explanation for Node 4"},
            {"id": 15, "name": "Node 5", "explanation": "This is the explanation for Node 5"}
        ],
        "edges": [
            {"id": "1to2", "content": "Content from Node 1 to Node 2"},
            {"id": "2to3", "content": "Content from Node 2 to Node 3"},
            {"id": "3to4", "content": "Content from Node 3 to Node 4"},
            {"id": "4to5", "content": "Content from Node 4 to Node 5"},
            {"id": "1to15", "content": "Content from Node 1 to Node 5"}
        ]
    }

    # Test Wfun function
    alpha_1 = 1
    node_id = 1
    wfun_result = Wfun(data, node_id, alpha_1)
    print("Wfun Result:")
    for item in wfun_result:
        print(f"Node ID: {item[0]}, Explanation: {item[1]}")
    
    # Test Dfun function
    alpha_2 = 1
    dfun_result = Dfun(data, node_id, alpha_2)
    print("\nDfun Result:")
    for item in dfun_result:
        print(f"({item[0]}, '{item[1]}', {item[2]})")
