# data = 'https://catalog.roblox.com/v2/search/items/details?Keyword=chicken&Subcategory=12&SortType=0&SortAggregation=5&Limit=10'

# print(data)

# import requests

# def get_chicken_items():
#   url = "https://catalog.roblox.com/v2/search/items/details?Keyword=chicken&Subcategory=12&SortType=0&SortAggregation=5&Limit=10"
#   response = requests.get(url)
#   if response.status_code == 200:
#     data = response.json()
#     return data
#   else:
#     return None

# if __name__ == "__main__":
#   data = get_chicken_items()
#   for item in data:
#     print(item["Name"])

import requests

response = requests.get('https://catalog.roblox.com/v2/search/items/details?Keyword=y2k&Subcategory=12&SortType=0&SortAggregation=5&Limit=10')
print(response.text) # 76.105.187.182
