"""
This module defines functions to handle embeddings and knowledge graphs, 
including finding and sorting nodes based on similarity, extracting relationships, 
and performing multi-step reasoning over a knowledge graph. The main function `R` combines 
the first step of node extraction and the second step of relation extraction based on embeddings.

Functions:
- find_nodes: Finds and sorts nodes based on cosine similarity with a query.
- extract_by_id: Extracts a node from a list of nodes by its ID.
- extract_name_by_id: Extracts the name of a node by its ID.
- sort: Sorts a list of nodes based on their similarity score.
- R_1: Implements the first step of reasoning over the knowledge graph.
- R_2: Implements the second step of reasoning to extract relations.
- R: Combines R_1 and R_2 to extract both nodes and relations.
"""

from .embedding import *
from .kg_functions import *

def find_nodes(query, beta_1, data):
    """
    This function finds nodes in the knowledge graph that are most similar to the query.

    Parameters:
    query (str): The query term.
    beta_1 (int): The number of top concepts to retrieve.
    data (dict): The input data containing nodes in JSON format.

    Returns:
    tuple: A sorted list of all nodes with similarity scores, and a list of top beta_1 nodes.
    """
    concepts = data['nodes']
    conceptsAddsimi = concepts
    # Calculate similarity for each concept
    for i in range(len(concepts)):
        similarity_score = cosine_similarity(get_embedding(query), get_embedding(concepts[i]['name']))
        conceptsAddsimi[i]["similarity_score"] = similarity_score
    sorted_data = sorted(conceptsAddsimi, key=lambda x: x['similarity_score'], reverse=True)
    # Extract the top beta_1 items
    top_items = sorted_data[:beta_1]
    return sorted_data, top_items

def extract_by_id(data, target_id):
    """
    Extracts a node by its ID from a list of nodes.

    Parameters:
    data (list): A list of nodes.
    target_id (str): The ID of the node to extract.

    Returns:
    dict: The node matching the target ID, or None if no match is found.
    """
    for item in data:
        if item['id'] == target_id:
            return item
    return None

def extract_name_by_id(data, target_id):
    """
    Extracts the name of a node by its ID.

    Parameters:
    data (list): A list of nodes.
    target_id (str): The ID of the node whose name is to be extracted.

    Returns:
    str: The name of the node matching the target ID, or None if no match is found.
    """
    for item in data:
        if item['id'] == target_id:
            return item['name']
    return None

def sort(data):
    """
    Sorts a list of nodes based on their similarity score in descending order.

    Parameters:
    data (list): A list of nodes.

    Returns:
    list: A sorted list of nodes.
    """
    return sorted(data, key=lambda x: x['similarity_score'], reverse=True)

def R_1(extracted_json, query, alpha_1, beta_1):
    """
    Performs the first step of reasoning, which involves finding nodes related to a query 
    and retrieving further connected nodes up to a certain distance (alpha_1).

    Parameters:
    extracted_json (dict): The input knowledge graph in JSON format.
    query (str): The query term.
    alpha_1 (int): The maximum length of connections to explore.
    beta_1 (int): The number of top concepts to retrieve.

    Returns:
    tuple: A list of all nodes, a list of extracted concepts based on similarity, 
    and a list of connected nodes.
    """
    result_list = []
    total_concepts, extracted_concepts = find_nodes(query, beta_1, extracted_json)
    for i in range(len(extracted_concepts)):
        re1 = Wfun(extracted_json, extracted_concepts[i]["id"], alpha_1)
        for j in range(len(re1)):
            re2 = extract_by_id(total_concepts, re1[j][0])
            if re2 not in result_list:
                result_list.append(re2)
    return total_concepts, extracted_concepts, result_list

def R_2(extracted_json, res_r1, alpha_2):
    """
    Performs the second step of reasoning, which involves extracting relationships between nodes.

    Parameters:
    extracted_json (dict): The input knowledge graph in JSON format.
    res_r1 (tuple): The result from the first step (R_1), containing nodes and their connections.
    alpha_2 (int): The maximum length of connections to explore for relationships.

    Returns:
    list: A list of extracted relationships between nodes.
    """
    result_list = []
    total_concepts = res_r1[0]  # Assuming res_r1[0] is total_concepts
    res_r1_list = res_r1[2]  # Assuming res_r1[2] contains the list of nodes
    
    for i in range(len(res_r1_list)):
        id = res_r1_list[i]["id"]  # Correctly access the dictionary in the list
        
        re1 = Dfun(extracted_json, id, alpha_2)  # Retrieve the related list from Dfun
        
        for j in range(len(re1)):
            re2 = {
                "from": extract_name_by_id(total_concepts, re1[j][0]),
                "to": extract_name_by_id(total_concepts, re1[j][2]),
                "relation": re1[j][1]
            }
            if re2 not in result_list:  # Ensure no duplicates are added
                result_list.append(re2)
    
    return result_list

def R(query, extracted_json, alpha_1, alpha_2, beta_1):
    """
    Combines R_1 and R_2 to extract both concepts and relationships for a query.

    Parameters:
    query (str): The query term.
    extracted_json (dict): The input knowledge graph in JSON format.
    alpha_1 (int): The maximum length of connections to explore for nodes.
    alpha_2 (int): The maximum length of connections to explore for relationships.
    beta_1 (int): The number of top concepts to retrieve.

    Returns:
    dict: A dictionary containing the sorted concepts with similarity scores and the extracted relationships.
    """
    part1 = R_1(extracted_json, query, alpha_1, beta_1)
    part2 = R_2(extracted_json, part1, alpha_2)
    return {
        "concepts_id/name/explanation_and_similarity_sorted": part1[2],  # Improved key name
        "complete_relations": part2
    }
