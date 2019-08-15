# HealthCare
Medical Expenditure Panel Survey (MEPS) (https://meps.ahrq.gov/mepstrends/home/index.html) is the only national data source measuring how Americans use and pay for medical care, health insurance, and out-of-pocket spending. Annual surveys of individuals and families, as well as their health care providers, provide data on health status, the use of medical services, charges, insurance coverage, and satisfaction with care. 

For this project I used the total expenditure in millions and number of people in thousands from the year 2002 to 2016 in the following categories: Gender (male, female), Education (some college, high school, leass than high school, still in school), Percieved health status (excellent, ver good health, good health, fair health and poor health).

I transformed the data using MySQL and Pandas, and loaded the transformed data into csv and json files. 

Using Python and an API from https://nutridigm-api-dev.azurewebsites.net/swagger/ui/index#/ I automated the process of obtain foods that are safe to consume and foods that should be avoided for certain health conditions. 

Using python, pandas, javascript, and tableau the data is visualized and presented on a Bootstrap designed web page by means of flask.