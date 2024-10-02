import re
import json

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

def extract_json_from_string(input_string):
    """
    Extracts a JSON object from a given input string that may contain text with a JSON section
    surrounded by triple backticks (```). If the string contains a section between triple backticks,
    it attempts to extract and parse that section as JSON. If no backticks are found, it attempts
    to parse the entire string as JSON.
    """
    if '```' in input_string:
        # Extract the part between ``` and remove 'json' markers
        result = input_string.split('```', 2)[1].replace("json", '')
        try:
            # Parse the extracted part as JSON
            graph_data = json.loads(result)
            return graph_data
        except json.JSONDecodeError:
            return "Invalid JSON format."
    else:
        # Try to parse the whole string as JSON
        try:
            graph_data = json.loads(input_string)
            return graph_data
        except json.JSONDecodeError:
            return "Invalid JSON format."

if __name__ == '__main__':
    # Example usage:
    data = 'Certainly! Here is an example of a JSON object where a dictionary contains a list, and that list contains dictionaries:\n\n```json\n{\n  "parentDictionary": {\n    "info": "This is the parent dictionary containing a list of dictionaries",\n    "listOfDictionaries": [\n      {\n        "id": 1,\n        "name": "Alice",\n        "age": 30\n      },\n      {\n        "id": 2,\n        "name": "Bob",\n        "age": 25\n      },\n      {\n        "id": 3,\n        "name": "Charlie",\n        "age": 35\n      }\n    ]\n  }\n}\n```\n\nIn this JSON structure:\n\n- The `parentDictionary` is a dictionary that contains a key-value pair for `info` and another for `listOfDictionaries`.\n- `listOfDictionaries` is a list that contains three dictionaries, each with `id`, `name`, and `age` keys.'
    print(extract_json_from_string(data))
