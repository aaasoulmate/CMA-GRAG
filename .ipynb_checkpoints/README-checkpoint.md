# CMA/GRAG

This repository aims to introduce a framework, called Collaborative Multi-Agents based on GraphRAG (CMA/GRAG). By using this framework, people can build a Questions-Answering system with deep knowledge comprehension and relevance.

## The structure of this GitHub repository:

- **datasets**: Stores the external databases.
- **KG**: Contains the knowledge graph corresponding to the datasets.
- **prompts**: Stores the task designs for six agents:
  - **agent 1, 2, 3**: Extract concepts, provide one hint per round, and explain the capabilities assessed by the question.
  - **agent 4**: Clarifies the received question and generates additional questions for further thought.
  - **fusion**: Integrates responses from different agents into an organized and coherent answer.
  - **graph**: Constructs a knowledge graph based on the external database.
  - Each agent's task is composed of a tool, planning, and an example for reference.
- **utils**: 
  - `chat.py`: Utilizes the 'GLM-4' family of models as the pretrained baseline LLMs.
  - `json.extract.py`: Extracts data in JSON format from a given string input.
  - `kg_functions.py`: Provides two functions to operate within a $\text{KG}$-space.
- **main.py**: Contains the main code to demonstrate the effectiveness of the framework.
