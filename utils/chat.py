"""
In this implementation, we use the GLM-4 family of Large Language Models as our pre-trained baseline chat models.
The available LLMs are as follows:
glm_4_list = ["glm-4", "glm-4-plus", "glm-4-long", "glm-4-0520", "glm-4-flash"]
Note: The API key for GLM is not provided here. You can obtain one by visiting:
https://www.bigmodel.cn/usercenter/apikeys
"""

from zhipuai import ZhipuAI

# Initialize the API client with your key
api_key = "YOUR_API_KEY_HERE"

class GLM4LLMs:
    def __init__(self, api_key, model_name="glm-4"):
        """
        Initializes the GLM4LLMs class with the provided API key and model name.
        
        Parameters:
        - api_key: str : Your API key for accessing the GLM-4 models.
        - model_name: str : The name of the GLM-4 model you want to use.
        """
        self.client = ZhipuAI(api_key=api_key)
        self.model_name = model_name

    def get_response(self, user_content, system_content=""):
        """
        Generates a response using the specified GLM-4 model.

        Parameters:
        - user_content: str : The content provided by the user.
        - system_content: str : The optional system prompt content.

        Returns:
        A dictionary with the response content or an error message.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": system_content},
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
    llm = GLM4LLMs(api_key=api_key, model_name="glm-4-flash")
    system_prompt = ""
    user_input = "Introduce HK in around 50 words."
    
    # Fetch the response from the model
    response = llm.get_response(user_content=user_input, system_content=system_prompt)
    
    # Print the model's response
    print(response)
