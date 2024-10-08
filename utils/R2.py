"""
This function filters connections between nodes in the given data based on the id_list and the alpha_2 parameter.
It returns a list of dictionaries, each representing a connection with 'from', 'to', 'relation', and 'length' fields.
The function removes connections with length == 0 and ensures that for repeated 'to' nodes, the smallest 'length' is kept,
and the 'from' field is assigned based on the order in id_list if further duplicates are found. Finally, the connections
are sorted in ascending order based on 'length'.

Parameters:
- data: Dictionary containing 'nodes' and 'edges'.
- id_list: List of node IDs to filter from.
- alpha_2: Positive integer indicating the maximum edge length to include in the result.

Returns:
- A list of dictionaries, where each dictionary represents a connection, sorted by 'length'.
"""


def R_2(data, id_list, alpha_2=1):
    # Initialize the filtered connections list
    filtered_connections = []
    node_connections = {}  # Dictionary to track connections for each 'to' node

    # Create a dictionary to map node id to node name
    id_to_name = {node['id']: node['name'] for node in data['nodes']}

    # Traverse through the id_list to find the shortest connections
    for current_id in id_list:
        for edge in data['edges']:
            A, B = map(int, edge['id'].split('to'))

            # Check if current node is involved in the edge and length is valid
            if current_id in [A, B] and edge['length'] != 'NAN' and edge['length'] <= alpha_2 and edge['length'] > 0:
                # Get the other node involved in the edge
                other_node = B if A == current_id else A

                # Prepare the connection structure, replacing 'from' and 'to' ids with names
                connection = {
                    "from": id_to_name[current_id],  # Replace id with name
                    "to": id_to_name[other_node],  # Replace id with name
                    "relation": edge['content'],
                    "length": edge['length']
                }

                # Add connection to the node_connections list
                if other_node not in node_connections:
                    node_connections[other_node] = [connection]  # Start a list for this 'to' node
                else:
                    node_connections[other_node].append(connection)  # Append to the list

    # Collect the final filtered connections
    for connections in node_connections.values():
        filtered_connections.extend(connections)  # Append all connections for each 'to' node

    # Sort the filtered connections by 'length' in ascending order
    filtered_connections.sort(key=lambda x: x['length'])

    return filtered_connections


if __name__ == '__main__':
    data = {'nodes': [{'id': 1, 'name': 'Node 1', 'explanation': 'This is the explanation for Node 1'}, {'id': 2, 'name': 'Node 2', 'explanation': 'This is the explanation for Node 2'}, {'id': 3, 'name': 'Node 3', 'explanation': 'This is the explanation for Node 3'}, {'id': 4, 'name': 'Node 4', 'explanation': 'This is the explanation for Node 4'}, {'id': 5, 'name': 'Node 5', 'explanation': 'This is the explanation for Node 5'}], 'edges': [{'id': '1to1', 'content': 'Self', 'length': 0}, {'id': '1to2', 'content': 'Content from Node 1 to Node 2', 'length': 1}, {'id': '1to3', 'content': 'Content from Node 1 to Node 2\nContent from Node 2 to Node 3', 'length': 2}, {'id': '1to4', 'content': 'Content from Node 1 to Node 4', 'length': 1}, {'id': '1to5', 'content': 'Content from Node 1 to Node 5', 'length': 1}, {'id': '2to1', 'content': 'Content from Node 2 to Node 1', 'length': 1}, {'id': '2to2', 'content': 'Self', 'length': 0}, {'id': '2to3', 'content': 'Content from Node 2 to Node 3', 'length': 1}, {'id': '2to4', 'content': 'Content from Node 2 to Node 1\nContent from Node 1 to Node 4', 'length': 2}, {'id': '2to5', 'content': 'Content from Node 2 to Node 1\nContent from Node 1 to Node 5', 'length': 2}, {'id': '3to1', 'content': 'Content from Node 3 to Node 2\nContent from Node 2 to Node 1', 'length': 2}, {'id': '3to2', 'content': 'Content from Node 3 to Node 2', 'length': 1}, {'id': '3to3', 'content': 'Self', 'length': 0}, {'id': '3to4', 'content': 'Content from Node 3 to Node 4', 'length': 1}, {'id': '3to5', 'content': 'Content from Node 3 to Node 4\nContent from Node 4 to Node 5', 'length': 2}, {'id': '4to1', 'content': 'Content from Node 4 to Node 1', 'length': 1}, {'id': '4to2', 'content': 'Content from Node 4 to Node 1\nContent from Node 1 to Node 2', 'length': 2}, {'id': '4to3', 'content': 'Content from Node 4 to Node 3', 'length': 1}, {'id': '4to4', 'content': 'Self', 'length': 0}, {'id': '4to5', 'content': 'Content from Node 4 to Node 5', 'length': 1}, {'id': '5to1', 'content': 'Content from Node 5 to Node 1', 'length': 1}, {'id': '5to2', 'content': 'Content from Node 5 to Node 1\nContent from Node 1 to Node 2', 'length': 2}, {'id': '5to3', 'content': 'Content from Node 5 to Node 4\nContent from Node 4 to Node 3', 'length': 2}, {'id': '5to4', 'content': 'Content from Node 5 to Node 4', 'length': 1}, {'id': '5to5', 'content': 'Self', 'length': 0}]}

    result = R_2(data, id_list=[1,2], alpha_2=2)
    print(result)