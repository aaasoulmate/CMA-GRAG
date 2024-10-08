"""
This function filters nodes from the provided data based on the given id_list and the alpha_1 parameter.
It searches for edges with a length less than or equal to alpha_1 and returns nodes connected to the input IDs.
If the same node is found via multiple connections, it keeps the connection with the smallest length.
The final result is sorted by length in ascending order.

We choose R_1^{(1)} as the retrieval function of our framework.

Parameters:
- data: Dictionary containing 'nodes' and 'edges'.
- id_list: List of node IDs to filter from.
- alpha_1: Positive integer indicating the maximum edge length to include in the result.

Returns:
- A list of nodes with the smallest edge lengths, sorted in ascending order by length.
"""


def R_1(data, id_list, alpha_1=1):
    # Initialize the filtered nodes list
    filtered_nodes = []
    node_lengths = {}  # Dictionary to track the shortest length for each node

    # Convert the id_list into a set for quick lookup
    id_set = set(id_list)

    # Traverse through the id_list to find the shortest connections
    for current_id in id_list:
        for edge in data['edges']:
            A, B = map(int, edge['id'].split('to'))

            # Check if current node is involved in the edge and length is valid
            if current_id in [A, B] and edge['length'] != 'NAN' and edge['length'] <= alpha_1:
                # Get the other node involved in the edge
                other_node = B if A == current_id else A

                # Find the node and update its length if necessary
                node_other = next((node for node in data['nodes'] if node['id'] == other_node), None)
                if node_other:
                    # If this node has not been added, or if the new length is smaller
                    if other_node not in node_lengths or edge['length'] < node_lengths[other_node]:
                        node_lengths[other_node] = edge['length']
                        node_with_length = {
                            "id": node_other['id'],
                            "name": node_other['name'],
                            "explanation": node_other['explanation'],
                            "length": edge['length']
                        }
                        # Check if this node is already in filtered_nodes, replace it if needed
                        filtered_nodes = [
                            node for node in filtered_nodes if node['id'] != node_with_length['id']
                        ]
                        filtered_nodes.append(node_with_length)

    # Sort the filtered nodes by 'length' in ascending order
    filtered_nodes.sort(key=lambda x: x['length'])

    return filtered_nodes


if __name__ == '__main__':
    data = {'nodes': [{'id': 1, 'name': 'Node 1', 'explanation': 'This is the explanation for Node 1'}, {'id': 2, 'name': 'Node 2', 'explanation': 'This is the explanation for Node 2'}, {'id': 3, 'name': 'Node 3', 'explanation': 'This is the explanation for Node 3'}, {'id': 4, 'name': 'Node 4', 'explanation': 'This is the explanation for Node 4'}, {'id': 5, 'name': 'Node 5', 'explanation': 'This is the explanation for Node 5'}], 'edges': [{'id': '1to1', 'content': 'Self', 'length': 0}, {'id': '1to2', 'content': 'Content from Node 1 to Node 2', 'length': 1}, {'id': '1to3', 'content': 'Content from Node 1 to Node 2\nContent from Node 2 to Node 3', 'length': 2}, {'id': '1to4', 'content': 'Content from Node 1 to Node 4', 'length': 1}, {'id': '1to5', 'content': 'Content from Node 1 to Node 5', 'length': 1}, {'id': '2to1', 'content': 'Content from Node 2 to Node 1', 'length': 1}, {'id': '2to2', 'content': 'Self', 'length': 0}, {'id': '2to3', 'content': 'Content from Node 2 to Node 3', 'length': 1}, {'id': '2to4', 'content': 'Content from Node 2 to Node 1\nContent from Node 1 to Node 4', 'length': 2}, {'id': '2to5', 'content': 'Content from Node 2 to Node 1\nContent from Node 1 to Node 5', 'length': 2}, {'id': '3to1', 'content': 'Content from Node 3 to Node 2\nContent from Node 2 to Node 1', 'length': 2}, {'id': '3to2', 'content': 'Content from Node 3 to Node 2', 'length': 1}, {'id': '3to3', 'content': 'Self', 'length': 0}, {'id': '3to4', 'content': 'Content from Node 3 to Node 4', 'length': 1}, {'id': '3to5', 'content': 'Content from Node 3 to Node 4\nContent from Node 4 to Node 5', 'length': 2}, {'id': '4to1', 'content': 'Content from Node 4 to Node 1', 'length': 1}, {'id': '4to2', 'content': 'Content from Node 4 to Node 1\nContent from Node 1 to Node 2', 'length': 2}, {'id': '4to3', 'content': 'Content from Node 4 to Node 3', 'length': 1}, {'id': '4to4', 'content': 'Self', 'length': 0}, {'id': '4to5', 'content': 'Content from Node 4 to Node 5', 'length': 1}, {'id': '5to1', 'content': 'Content from Node 5 to Node 1', 'length': 1}, {'id': '5to2', 'content': 'Content from Node 5 to Node 1\nContent from Node 1 to Node 2', 'length': 2}, {'id': '5to3', 'content': 'Content from Node 5 to Node 4\nContent from Node 4 to Node 3', 'length': 2}, {'id': '5to4', 'content': 'Content from Node 5 to Node 4', 'length': 1}, {'id': '5to5', 'content': 'Self', 'length': 0}]}

    # Test with multiple IDs
    result = R_1(data, [1], alpha_1=2)
    print(result)
