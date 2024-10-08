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
  - `embedding.py`: Embeds a sentence or passage into 1024-dimension vectors and also compute the relevance using cosine-similarity measure.
  - `get_E.py`: Gets the edges set $\mathsf{E}$ beyond just the initial edges set $\mathsf{E}_0$.
  - `json.extract.py`: Extracts data in JSON format from a given string input.
  - `R1.py`: Retrieves nodes and also add length for references.
  - `R2.py`: Retrieves completer relatons and also add length for references.
  - `R.py`: Retrieves nodes and complete relations based on `R1` and `R2`.
- **main.ipynb**: Contains the main code to demonstrate the effectiveness of the framework.
- **requirements.txt**: all the necessary libaries for our project.
