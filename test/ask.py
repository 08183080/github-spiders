import requests

url = 'https://huggingface.co/spaces/Aniun/semantic_github'

response = requests.post(url, data='你好')

print(response.text)