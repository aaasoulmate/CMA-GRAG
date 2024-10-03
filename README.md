# CMA/GRAG

This repository aims to introduce a framework, called Collaborative Multi-Agents based on GraphRAG (CMA/GRAG). By using this framework, people can build a Questions-Answering system with deep knowledge comprehension and relevance.

## The structure of this GitHub repository:

- **datasets**: Stores the external databases.
- **knowledge_graph**: Contains the knowledge graph in `JSON` format corresponding to the datasets.
- **prompts**: Stores the task designs for six agents:
  - **agent 1, 2, 3**: Extract concepts, provide one hint per round, and explain the capabilities assessed by the question.
  - **agent 4**: Clarifies the received question and generates additional questions for further thought.
  - **fusion**: Integrates responses from different agents into an organized and coherent answer.
  - **graph**: Constructs a knowledge graph based on the external database.
  - Each agent's task is composed of a tool, planning, and an example for reference.
- **utils**: 
  - `agents.py`: Builds a class of agents utilizing the 'GLM-4' family of models as the pretrained baseline LLMs. Agent = LLM + system_content here.
  - `embedding.py`: Embed a sentence or passage into 1024-dimension vectors and also compute the relevance using cosine-similarity measure.
  - `json.extract.py`: Extracts data in JSON format from a given string input.
  - `kg_functions.py`: Provides two functions to operate within a $\text{KG}$-space.
  - `retrieval.py`: Retrieve nodes and edges to augment user's query.
- **main.ipynb**: Contains the main code to demonstrate the effectiveness of the framework.
- **requirements.txt**: all the necessary libaries for our project.
