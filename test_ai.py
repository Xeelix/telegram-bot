import os
import requests

def send_ai_request(prompt):
    api_key = os.getenv('OPENAI_API_KEY')
    base_url = os.getenv('OPENAI_BASE_URL')
    model = os.getenv('OPENAI_MODEL')

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    data = {
        'model': model,
        'messages': [{'role': 'user', 'content': prompt}],
        'temperature': 0.7
    }

    response = requests.post(base_url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code}, {response.text}"

if __name__ == '__main__':
    test_prompt = "who r u"
    result = send_ai_request(test_prompt)
    print(f"Prompt: {test_prompt}")
    print(f"Response: {result}")