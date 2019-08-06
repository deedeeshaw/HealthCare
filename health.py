import requests
from config import api

base_url="https://nutridigm-api-dev.azurewebsites.net"
consume="/api/v1/nutridigm/topitemstoconsume?"
avoid="/api/v1/nutridigm/topitemstoavoid?"

problemId = 6

query_consume=base_url + consume + f'subscriptionId={api}&problemId={problemId}&api_key={api}'

query_avoid=base_url + avoid + f'subscriptionId={api}&problemId={problemId}&api_key={api}'

def food():
    consume_food = requests.get(query_consume).json()
    avoid_food= requests.get(query_avoid).json()
    print(consume_food)
    print(avoid_food)
    return consume_food, avoid_food

# def avoid_food():
#     avoid_food= requests.get(query_avoid).json()
#     print(avoid_food)
#     return avoid_food