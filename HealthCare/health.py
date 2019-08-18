
import csv
from flask import request

#######################################################################
# FUNCTION TO CREATE THE DROPDOWN MENU OF PROBLEMS
######################################################################
def problem_dd():
    problem_list = []
    with open('static/data/health_problem.csv') as problem_file:
        problem = csv.reader(problem_file, delimiter=',')

        for row in problem:
            problem_list.append({'prob_id':row[0], 'prob_desc': row[1]})
        return problem_list




















# base_url="https://nutridigm-api-dev.azurewebsites.net"
# consume="/api/v1/nutridigm/topitemstoconsume?"
# avoid="/api/v1/nutridigm/topitemstoavoid?"

# problemId = 6

# query_consume=base_url + consume + f'subscriptionId={api}&problemId={problemId}&api_key={api}'

# query_avoid=base_url + avoid + f'subscriptionId={api}&problemId={problemId}&api_key={api}'

# def food():
#     consume_food = requests.get(query_consume).json()
#     avoid_food= requests.get(query_avoid).json()
#     print(consume_food)
#     print(avoid_food)
#     return consume_food, avoid_food

# def avoid_food():
#     avoid_food= requests.get(query_avoid).json()
#     print(avoid_food)
#     return avoid_food