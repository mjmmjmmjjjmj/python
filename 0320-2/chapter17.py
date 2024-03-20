# import requests
from matplotlib import pyplot as plt
import json
# u = 'https://api.github.com/search/repositories?q=language:python+sort:stars'

names = []
stars = []

# res = requests.get(u)
# print(type(res.json()))

with open ('repositories.json', 'r', encoding='utf-8') as f :
    res = json.load(f)
    print(len(res['items']), type(res['items']))
    for item in res ['items']:
        names.append(item['name'])
        stars.append(item['stargazers_count'])

plt.bar(names,stars)
plt.xticks(rotation=45)
plt.show()
