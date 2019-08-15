import pandas as pd
import csv

def data_table():
    data_df = pd.read_csv("static/data/health.csv")
    data = data_df.rename(columns={'All_persons': 'Total Expense', 'Male': 'Male ******', 'Female': 'Female ******',
        'Less_than_high_school': '< High School', 'High_school': "High School",
        'Some_college': 'Some College', 
        "Less_than_18": "Still in School",
        "Excellent_health": "Excellent Health",
        "VG_health": "Very Good Health",
         "Good_health": "Good Health",
         "Fair_health": "Fair Health", "Poor_health": "Poor Health"})
    data.set_index("Year", inplace=True)
    pd.set_option('display.max_colwidth', 40000)
    
    data = data.applymap('{:,}'.format)
    

    data_html1 = data.to_html().replace('\n', '').replace('<th>', '<th style="text-align: center">')
    data_html = data_html1.replace('<tr>', '<tr align = "right">')
   
    return data_html

def perperson_table():
    per_person_df = pd.read_csv("static/data/per_person.csv")
    per_person = per_person_df.rename(columns={'Per_person': 'Total per Person', 'per_Male': "Male ****",
                   'per_Female': "Female ******",
                    'per_Less_than_high_school': '< High School', 'per_High_school': "High Schhol",
                      'per_Some_college': 'Some College',
                       "per_Less_than_18": "Still in School",
                        "per_Excellent_health": "Excellent Health",
                      "per_VG_health": "Very Good Health", 
                      "per_Good_health": "Good Health", "per_Fair_health": "Fair Health",
                      "per_Poor_health": "Poor Health"})
    per_person.set_index("Year", inplace=True)
    
    person_html = per_person.to_html().replace('\n', '', ).replace('<th>', '<th style="text-align: center">').replace('<tr>', '<tr align="center">')
    # person_html = person_html1.replace('<th>', '<th style="text-align: center">').replace('<tr>', '<tr align="center">')
    return person_html