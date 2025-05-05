import ast
import json
import logging
import re
from typing import Union


def sanitize_json(raw_json: str) -> str:
    """
    Cleans raw JSON by removing characters that could break the structure.
    For example, removes unmatched closing parentheses.
    """
    # Remove extra unmatched closing parentheses
    stack = []
    clean_content = []

    for char in raw_json:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                continue  # Skip unmatched closing parentheses
        clean_content.append(char)

    # Remove any dangling commas before a closing brace or bracket
    clean_json = ''.join(clean_content)
    clean_json = re.sub(r',\s*([\}\]])', r'\1', clean_json)

    return clean_json


def try_to_extract_dict_from_json_openai(
    raw_output: str,
) -> Union[list[dict[str, str]], str]:
    pattern = r'```json\s*\n(?P<json>([\s\S]*?))\n```'
    matches = re.finditer(pattern, raw_output, re.MULTILINE)

    dict_output = ""
    for match in matches:
        json_content = match.group('json')
        try:
            dict_output = json.loads(json_content)

            return dict_output
        except json.JSONDecodeError as e:
            logging.debug("Invalid JSON:", e)
        except ValueError as e:
            logging.debug("ValueError:", e)

            return raw_output
    else:
        try:
            dict_output = ast.literal_eval(raw_output.strip("```json"))
        except SyntaxError as e:
            logging.debug(f"Got Syntax Error: {e} for output: {raw_output[:30]}; Sanitizing...")
            raw_output = sanitize_json(raw_output)
            try:
                dict_output = ast.literal_eval(raw_output.strip("```json"))
            except SyntaxError as e:
                logging.debug(f"Got another Syntax Error: {e} for output: {raw_output[:30]}; Returning raw output.")
                return raw_output
        except ValueError as e:
            logging.debug(f"Got Value Error: {e} for output: {raw_output[:30]}; Returning raw output.")

            return raw_output

    return dict_output
