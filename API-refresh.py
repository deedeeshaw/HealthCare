import csv
from config import api
import pandas as pd
import requests

def problem_dd():
    problem_list = []
    with open('static/data/problem.csv') as problem_file:
        problem = csv.reader(problem_file, delimiter=',')
#       skip header row
        next(problem, None)
        for row in problem:
            problem_list.append({'prob_id':row[0], 'prob_desc': row[1]})
        return problem_list
