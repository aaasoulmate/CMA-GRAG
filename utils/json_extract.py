"""
This script defines a function `extract_json_from_string` that extracts and parses 
JSON objects embedded within text. It is especially useful when the JSON data 
is enclosed in triple backticks (```), such as in documentation or formatted text. 

- If the input contains triple backticks, the function extracts the portion between 
  them and attempts to parse it as JSON.
- If no backticks are found, it tries to parse the entire string as JSON.
- If parsing fails, the function returns an error message indicating invalid JSON.

The script also includes an example usage where a string contains a JSON object 
formatted with backticks, demonstrating how the function works.
"""

import re
import json

def clean_and_extract_json(text):
    """
    Cleans the input string by removing comments and extra commas, then extracts and parses the JSON.

    Parameters:
    text (str): The input string containing JSON within code blocks.

    Returns:
    dict: The cleaned and parsed JSON as a dictionary, or None if extraction or parsing fails.
    """
    # Step 1: Remove single-line comments (// comments)
    text_no_comments = re.sub(r'//.*', '', text)
    
    # Step 2: Remove any trailing commas before closing braces/brackets
    text_no_trailing_commas = re.sub(r',\s*([\]}])', r'\1', text_no_comments)
    
    # Step 3: Remove extra commas in arrays/objects
    text_cleaned = re.sub(r',\s*(\]|\})', r'\1', text_no_trailing_commas)

    # Step 4: Extract JSON content from the cleaned text
    pattern = r'```json\s*(.*?)\s*```'
    match = re.search(pattern, text_cleaned, re.DOTALL)
    
    if match:
        json_content = match.group(1).strip()
        try:
            # Step 5: Parse the JSON string into a dictionary
            json_data = json.loads(json_content)
            return json_data
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON: {e}")
            return None
    else:
        return None

if __name__ == '__main__':
    # Example usage:
    data = 'Certainly! Here is an example of a JSON object where a dictionary contains a list, and that list contains dictionaries:\n\n```json\n{\n  "parentDictionary": {\n    "info": "This is the parent dictionary containing a list of dictionaries",\n    "listOfDictionaries": [\n      {\n        "id": 1,\n        "name": "Alice",\n        "age": 30\n      },\n      {\n        "id": 2,\n        "name": "Bob",\n        "age": 25\n      },\n      {\n        "id": 3,\n        "name": "Charlie",\n        "age": 35\n      }\n    ]\n  }\n}\n```\n\nIn this JSON structure:\n\n- The `parentDictionary` is a dictionary that contains a key-value pair for `info` and another for `listOfDictionaries`.\n- `listOfDictionaries` is a list that contains three dictionaries, each with `id`, `name`, and `age` keys.'
    print(clean_and_extract_json(data))
