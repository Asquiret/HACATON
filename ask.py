import requests
import json

# API Configuration
LKEY = "sk-P_K5kEpuT9Suh3Ot5P1Evul2TjQ-Vme1aN8jefGUt54"

def ask_bot(question, url):
    # Request payload configuration
    payload = {
        "output_type": "chat",
        "input_type": "chat",
        "input_value": question
    }

    # Request headers
    headers = {
        "Content-Type": "application/json",
        "x-api-key": LKEY  # Authentication key from environment variable
    }

    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    a = json.loads(response.text)
    answer = a["outputs"][0]["outputs"][0]["results"]["message"]["data"]["text"]
    return(answer)
