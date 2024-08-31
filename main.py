import requests

#ambik data dari stock market
r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2024-8-1&to=2024-8-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')
content = r.json()
#ambik content dari API
print(type(content))
print(content ['articles'][0]['title'])
print(content ['articles'][0]['description'])

#ambik data dari news united states Title=united%20states&
i = requests.get('https://newsapi.org/v2/everything?qInTitle=united%20states&from=2024-8-1&to=2024-8-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')
content_i = i.json()
#ambik content dari API
print(type(content))
print(content_i ['articles'][0]['title'])
print(content_i ['articles'][0]['description'])