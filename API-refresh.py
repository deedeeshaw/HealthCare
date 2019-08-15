#############################################################
# IMPORT DEFICIENCIES
#############################################################
import csv
from config import api
import pandas as pd
import requests

#############################################################
# REFRESH DROP DOWN LIST
#############################################################

def problem_dd():
    problem_list = []
    with open('static/data/problem.csv') as problem_file:
        problem = csv.reader(problem_file, delimiter=',')
#       skip header row
        next(problem, None)
        for row in problem:
            problem_list.append({'prob_id':row[0], 'prob_desc': row[1]})
        return problem_list


#############################################################
# RUN API TO REFRESH DATA FILES 
#############################################################
base_url="https://nutridigm-api-dev.azurewebsites.net"
consume_url="/api/v1/nutridigm/topitemstoconsume?"
avoid_url="/api/v1/nutridigm/topitemstoavoid?"
def problem_df():
       problem_list = []
    with open('static/data/problem.csv') as problem_file:
        problem = csv.reader(problem_file, delimiter=',')
#       skip header row
        next(problem, None)
        for row in problem:
            problem_list.append({'prob_id':row[0], 'prob_desc': row[1]})
# Create Data Frame
        problem_df = pd.DataFrame()

# Iterrate over the list problem_list
        x = 1

        for problem in problem_list:
                problemId=problem['prob_id']
                query_consume=base_url + consume_url + f'subscriptionId={api}&problemId={problemId}&api_key={api}'
                query_avoid=base_url + avoid_url + f'subscriptionId={api}&problemId={problemId}&api_key={api}'
    
        # Get the food data from nudrigim.org
                c_food = requests.get(query_consume).json()
                a_food = requests.get(query_avoid).json()
    
                if x!=1:
                        for c in c_food:
                                consume_food = c
    
                        for a in a_food:
                                avoid_food = a
    
    
                                problem_df.loc[x, "ID"]= problem['prob_id']
                                problem_df.loc[x, "Health Problem"]=problem['prob_desc']
                                problem_df.loc[x, "Consume"] = consume_food
                                problem_df.loc[x, "Avoid"] = avoid_food
    
                else:
                                 problem_df.loc[x, "ID"]= problem['prob_id']
                                 problem_df.loc[x, "Health Problem"]=problem['prob_desc']
                                 problem_df.loc[x, "Consume"] = c_food
                                 problem_df.loc[x, "Avoid"] = a_food

        x +=1
        
        # Export the data into a json
        return problem_df.to_json("static/data/health_problem.json", orient='records')

        # Export the data into a csx
        # problem_df.set_index("ID", inplace=True)
        # return problem_df.to_csv("static/data/health_problem.csv")

