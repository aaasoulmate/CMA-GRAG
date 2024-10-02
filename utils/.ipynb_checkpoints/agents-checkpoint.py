"""
In this implementation, we use the GLM-4 family of Large Language Models as our pre-trained baseline chat models.
The available LLMs are as follows:
glm_4_list = ["glm-4", "glm-4-plus", "glm-4-long", "glm-4-0520", "glm-4-flash"]
Note: The API key for GLM is not provided here. You can obtain one by visiting:
https://www.bigmodel.cn/usercenter/apikeys
And the agents are composed of a given LLM from this list and a task from prompts.
"""

from zhipuai import ZhipuAI

# Initialize the API client with your key
api_key = "531e9c858c9d4dc1d9295dbf0cdf20e5.zjSejRW3PHh8015f"

class Agent:
    def __init__(self, api_key, model_name="glm-4", system_content=""):
        """
        Initializes the GLM4LLMs class with the provided API key, model name, and system content.
        
        Parameters:
        - api_key: str : Your API key for accessing the GLM-4 models.
        - model_name: str : The name of the GLM-4 model you want to use.
        - system_content: str : The system prompt content that defines the agent's role.
        """
        self.client = ZhipuAI(api_key=api_key)
        self.model_name = model_name
        self.system_content = system_content

    def get_response(self, user_content):
        """
        Generates a response using the specified GLM-4 model and system content.

        Parameters:
        - user_content: str : The content provided by the user.

        Returns:
        A dictionary with the response content or an error message.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": self.system_content},
                    {"role": "user", "content": user_content}
                ]
            )

            result = {
                "response_content": response.choices[0].message.content
            }
            return result
        except Exception as e:
            return {"error": str(e)}

# Usage example
if __name__ == "__main__":
    agent = Agent(api_key=api_key, model_name="glm-4-flash", system_content="You are an expert familiar with every city around the world.")
    user_input = "Introduce HK in around 50 words."
    
    # Fetch the response from the model
    response = agent.get_response(user_content=user_input)
    
    # Print the model's response
    print(response)
