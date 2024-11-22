import requests

url = 'https://github.com/search?q=推荐算法 language:Python&type=repositories&l=Python'

proxies = {
    'http': '127.0.0.1:7890',
    'https': '127.0.0.1:7890'
}

response = requests.get(url, proxies=proxies)

# print(response.text)

with open('test.html', 'w', encoding='utf-8') as f:
    f.write(response.text)