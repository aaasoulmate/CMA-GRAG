"""
This script utilizes the embedding-3 model to embed a document into a 1024-dimensional vector representation. 
For further details on the embedding model, refer to: https://www.bigmodel.cn/dev/api/vector/embedding-3.
Additionally, cosine similarity is employed to compute the relevance between two document embeddings.
"""

import numpy as np
from zhipuai import ZhipuAI
from numpy.linalg import norm

# Initialize the ZhipuAI client
client = ZhipuAI(api_key="YOUR_API_KEY_HERE")

def get_embedding(input_text: str):
    """
    This function generates a 1024-dimensional embedding vector for a given input text using the embedding-3 model.
    
    Parameters:
    input_text (str): The text to be embedded.
    
    Returns:
    list: A 1024-dimensional embedding vector.
    """
    response = client.embeddings.create(
        model="embedding-3", 
        input=[input_text],
        dimensions=1024
    )
    return response.data[0].embedding

def cosine_similarity(vec1, vec2):
    """
    This function calculates the cosine similarity between two vectors.
    
    Parameters:
    vec1 (list): The first vector.
    vec2 (list): The second vector.
    
    Returns:
    float: A cosine similarity value between -1 and 1.
    """
    return np.dot(vec1, vec2) / (norm(vec1) * norm(vec2))

if __name__ == "__main__":
    # Example usage
    input_1 = "I love my mother"
    input_2 = "Mom said I should work hard"
    
    # Retrieve vector representations of the input texts
    vector_1 = get_embedding(input_1)
    vector_2 = get_embedding(input_2)
    
    # Calculate cosine similarity between the two vectors
    similarity = cosine_similarity(vector_1, vector_2)
    
    print(f"Cosine Similarity: {similarity}")
