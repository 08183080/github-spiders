import requests

url = 'https://github.com/search?q=推荐算法 language:Python&type=repositories&l=Python&s=stars&o=desc&p=1'

headers = {'User-Agent':'Mozilla/5.0',
           'Authorization': 'token ef802a122df2e4d29d9b1b868a6fefb14f22b272',
           'Content-Type':'application/json',
           'Accept':'application/json'
          }

proxies = {
    'http': '127.0.0.1:7890',
    'https': '127.0.0.1:7890'
}

response = requests.get(url, proxies=proxies, headers=headers)

# print(response.text)

with open('test.html', 'w', encoding='utf-8') as f:
    f.write(response.text)