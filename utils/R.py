"""
Retrieve the nodes and complete relations based on R1 and R2 which are defined elsewhere
"""

from utils.R1 import *
from utils.R2 import *

def R(data, id_list, alpha_1, alpha_2):
    result1 = R_1(data, id_list, alpha_1)
    result2 = R_2(data, id_list, alpha_2)
    result = {"nodes_retrieved": result1,
              "relations_retrieved": result2}
    return result


if __name__ == '__main__':
    data = {'nodes': [{'id': 1, 'name': 'Node 1', 'explanation': 'This is the explanation for Node 1'}, {'id': 2, 'name': 'Node 2', 'explanation': 'This is the explanation for Node 2'}, {'id': 3, 'name': 'Node 3', 'explanation': 'This is the explanation for Node 3'}, {'id': 4, 'name': 'Node 4', 'explanation': 'This is the explanation for Node 4'}, {'id': 5, 'name': 'Node 5', 'explanation': 'This is the explanation for Node 5'}], 'edges': [{'id': '1to1', 'content': 'Self', 'length': 0}, {'id': '1to2', 'content': 'Content from Node 1 to Node 2', 'length': 1}, {'id': '1to3', 'content': 'Content from Node 1 to Node 2\nContent from Node 2 to Node 3', 'length': 2}, {'id': '1to4', 'content': 'Content from Node 1 to Node 4', 'length': 1}, {'id': '1to5', 'content': 'Content from Node 1 to Node 5', 'length': 1}, {'id': '2to1', 'content': 'Content from Node 2 to Node 1', 'length': 1}, {'id': '2to2', 'content': 'Self', 'length': 0}, {'id': '2to3', 'content': 'Content from Node 2 to Node 3', 'length': 1}, {'id': '2to4', 'content': 'Content from Node 2 to Node 1\nContent from Node 1 to Node 4', 'length': 2}, {'id': '2to5', 'content': 'Content from Node 2 to Node 1\nContent from Node 1 to Node 5', 'length': 2}, {'id': '3to1', 'content': 'Content from Node 3 to Node 2\nContent from Node 2 to Node 1', 'length': 2}, {'id': '3to2', 'content': 'Content from Node 3 to Node 2', 'length': 1}, {'id': '3to3', 'content': 'Self', 'length': 0}, {'id': '3to4', 'content': 'Content from Node 3 to Node 4', 'length': 1}, {'id': '3to5', 'content': 'Content from Node 3 to Node 4\nContent from Node 4 to Node 5', 'length': 2}, {'id': '4to1', 'content': 'Content from Node 4 to Node 1', 'length': 1}, {'id': '4to2', 'content': 'Content from Node 4 to Node 1\nContent from Node 1 to Node 2', 'length': 2}, {'id': '4to3', 'content': 'Content from Node 4 to Node 3', 'length': 1}, {'id': '4to4', 'content': 'Self', 'length': 0}, {'id': '4to5', 'content': 'Content from Node 4 to Node 5', 'length': 1}, {'id': '5to1', 'content': 'Content from Node 5 to Node 1', 'length': 1}, {'id': '5to2', 'content': 'Content from Node 5 to Node 1\nContent from Node 1 to Node 2', 'length': 2}, {'id': '5to3', 'content': 'Content from Node 5 to Node 4\nContent from Node 4 to Node 3', 'length': 2}, {'id': '5to4', 'content': 'Content from Node 5 to Node 4', 'length': 1}, {'id': '5to5', 'content': 'Self', 'length': 0}]}
    id_list = [1, 3]
    alpha_1 = 1
    alpha_2 = 2
    result = R(data, id_list, alpha_1, alpha_2)
    print(result)