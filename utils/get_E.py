"""
This function generates a directed graph from the input data `E_0`,
finds the shortest paths between all node pairs, and generates a new `edges` structure.
For each node pair (A, B):
- If A == B, the content is 'Self' and length is 0.
- If a path exists between A and B, the content is the concatenation of the edges along the shortest path and length is the length of shortest path set - 1.
- If no path exists, the content is 'None' and length is 'NAN'.
"""

import itertools
import networkx as nx
import json

def get_E(E_0):
    # Create a directed graph
    G = nx.DiGraph()

    # Add all nodes to the graph (even if there are no edges)
    for node in E_0['nodes']:
        G.add_node(node['id'])

    # Add edges from E_0 to the graph
    edge_content_map = {}
    for edge in E_0['edges']:
        # Get the ids of nodes A and B as integers
        A, B = map(int, edge['id'].split('to'))
        # Add the directed edge and store the content
        G.add_edge(A, B)
        edge_content_map[(A, B)] = edge['content']

    nodes = E_0['nodes']  # nodes remain unchanged
    edges = []  # store the new edges

    # Get the range of node IDs directly from the data
    node_ids = [node['id'] for node in E_0['nodes']]

    # Iterate through all node pairs (A, B), including A == B
    for A, B in itertools.product(node_ids, repeat=2):  # Iterate using actual node IDs
        if A == B:
            # Self-loop case
            edges.append({"id": f"{A}to{B}", "content": "Self", "length": 0})
        elif nx.has_path(G, A, B):
            # If there is a path from A to B, find the shortest path and build the content
            path = nx.shortest_path(G, A, B)
            path_length = len(path) - 1  # number of edges
            content_list = []
            # Build the content for the path
            for i in range(len(path) - 1):
                start_node = path[i]
                end_node = path[i + 1]
                edge_content = edge_content_map[(start_node, end_node)]  # ensure correct direction
                content_list.append(edge_content)
            content = "\n".join(content_list)  # join with newline
            edges.append({"id": f"{A}to{B}", "content": content, "length": path_length})
        else:
            # If no path exists between A and B
            edges.append({"id": f"{A}to{B}", "content": "None", "length": "NAN"})

    # Return nodes unchanged, and the new edges
    return {
        "nodes": nodes,
        "edges": edges
    }


if __name__ == '__main__':
    # example:
    E_0 = {
    "nodes": [
        {
            "id": 1,
            "name": "India",
            "explanation": "India's health indicators have improved but still lag behind peer nations."
        },
        {
            "id": 2,
            "name": "Health Workers Density",
            "explanation": "India has an estimated active health workers density of doctors and nurses/midwives of 5.0 and 6.0 respectively for 10,000 persons."
        },
        {
            "id": 3,
            "name": "WHO Threshold",
            "explanation": "WHO recommends a threshold of 44.5 doctors, nurses, and midwives per 10,000 population."
        },
        {
            "id": 4,
            "name": "Skewed Divide",
            "explanation": "The issue in India is compounded by the skewed inter-state, urban-rural, and public-private sector divide."
        },
        {
            "id": 5,
            "name": "Universal Health Coverage",
            "explanation": "Addressing the paucity of skilled personnel is essential for India to achieve universal health coverage."
        },
        {
            "id": 6,
            "name": "Sustainable Development Goals (SDGs)",
            "explanation": "Accelerating progress toward universal health coverage aligns with India's sustainable development goals."
        },
        {
            "id": 7,
            "name": "Federal Health Budget",
            "explanation": "The recent increase in the federal health budget offers an opportunity to improve health workforce capacity."
        },
        {
            "id": 8,
            "name": "READ Approach",
            "explanation": "The READ approach is utilized for systematic document analysis in health policy research, consisting of readying materials, extracting data, and analyzing findings."
        },
        {
            "id": 9,
            "name": "Public Health Sector",
            "explanation": "Government-funded health sector in India is chronically underfunded, with healthcare expenditure of 1.28% of GDP."
        },
        {
            "id": 10,
            "name": "Private Health Sector",
            "explanation": "The private health sector is the dominant provider of healthcare in India, perceived to provide quality care."
        },
        {
            "id": 11,
            "name": "Medical Tourism",
            "explanation": "World-class health facilities enable India to become a leading destination for medical tourism."
        },
        {
            "id": 12,
            "name": "National Medical Council",
            "explanation": "India's National Medical Council aims to improve the regulation of health professionals and medical education."
        },
        {
            "id": 13,
            "name": "Accredited Social Health Activists (ASHA)",
            "explanation": "ASHAs are female community health workers serving to increase outreach for Auxiliary Nurse Midwives."
        },
        {
            "id": 14,
            "name": "Auxiliary Nurse Midwives (ANM)",
            "explanation": "ANMs are government employees providing primary healthcare services."
        },
        {
            "id": 15,
            "name": "Ayushman Bharat",
            "explanation": "Ayushman Bharat is a publicly financed health insurance scheme for the poor in India."
        },
        {
            "id": 16,
            "name": "Digital Technologies",
            "explanation": "Digital technology is being used to enhance healthcare delivery in India, such as through telemedicine."
        },
        {
            "id": 17,
            "name": "Violence against Healthcare Personnel",
            "explanation": "Increasing violence against healthcare personnel in India is a worrisome trend."
        },
        {
            "id": 18,
            "name": "Out-Of-Pocket (OOP) Expenditure",
            "explanation": "The private health sector consumes 5.1% of GDP, financed by OOP expenditure."
        },
        {
            "id": 19,
            "name": "Health Insurance Coverage",
            "explanation": "At best, 37% of the population had health insurance coverage in India by 2018."
        },
        {
            "id": 20,
            "name": "National Health Mission (NHM)",
            "explanation": "The NHM aims to increase healthcare services but lacks focus on quality."
        }
    ],
    "edges": [
        {
            "id": "1to2",
            "content": "India has an estimated active health workers density much lower than WHO recommended thresholds."
        },
        {
            "id": "2to1",
            "content": "India has an estimated active health workers density much lower than WHO recommended thresholds."
        },
        {
            "id": "2to3",
            "content": "India's health workers density is much lower than the WHO threshold."
        },
        {
            "id": "3to2",
            "content": "India's health workers density is much lower than the WHO threshold."
        },
        {
            "id": "1to5",
            "content": "Addressing the paucity of skilled personnel is essential for India to achieve universal health coverage."
        },
        {
            "id": "5to1",
            "content": "Addressing the paucity of skilled personnel is essential for India to achieve universal health coverage."
        },
        {
            "id": "1to6",
            "content": "Achieving universal health coverage aligns with India's sustainable development goals."
        },
        {
            "id": "6to1",
            "content": "Achieving universal health coverage aligns with India's sustainable development goals."
        },
        {
            "id": "7to8",
            "content": "The recent increase in the federal health budget offers an opportunity to use the READ approach for analysis."
        },
        {
            "id": "8to7",
            "content": "The recent increase in the federal health budget offers an opportunity to use the READ approach for analysis."
        },
        {
            "id": "9to10",
            "content": "The private health sector has become dominant due to the underfunding of the public sector."
        },
        {
            "id": "10to9",
            "content": "The private health sector has become dominant due to the underfunding of the public sector."
        },
        {
            "id": "10to11",
            "content": "World-class health facilities enable India to become a leading destination for medical tourism in the private sector."
        },
        {
            "id": "11to10",
            "content": "World-class health facilities enable India to become a leading destination for medical tourism in the private sector."
        },
        {
            "id": "13to14",
            "content": "ASHAs serve to increase the reach of Auxiliary Nurse Midwives."
        },
        {
            "id": "14to13",
            "content": "ASHAs serve to increase the reach of Auxiliary Nurse Midwives."
        },
        {
            "id": "16to15",
            "content": "Digital technology is used to enhance healthcare access in schemes like Ayushman Bharat."
        },
        {
            "id": "15to16",
            "content": "Digital technology is used to enhance healthcare access in schemes like Ayushman Bharat."
        },
        {
            "id": "1to17",
            "content": "Increasing violence against healthcare personnel is a challenge in India."
        },
        {
            "id": "17to1",
            "content": "Increasing violence against healthcare personnel is a challenge in India."
        },
        {
            "id": "10to18",
            "content": "The private health sector is financed by Out-Of-Pocket expenditure."
        },
        {
            "id": "18to10",
            "content": "The private health sector is financed by Out-Of-Pocket expenditure."
        },
        {
            "id": "1to19",
            "content": "At best, 37% of the Indian population had health insurance coverage in 2018."
        },
        {
            "id": "19to1",
            "content": "At best, 37% of the Indian population had health insurance coverage in 2018."
        },
        {
            "id": "9to20",
            "content": "The NHM has not improved healthcare quality despite efforts to increase services."
        },
        {
            "id": "20to9",
            "content": "The NHM has not improved healthcare quality despite efforts to increase services."
        }
    ]
}

    result = get_E(E_0)
    print(result)
