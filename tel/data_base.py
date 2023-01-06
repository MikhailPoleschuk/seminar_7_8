import csv

def read_db():
    with open('spr_tel.csv', 'r',encoding="utf-8") as file:  
        db = csv.DictReader(file)
        for row in db:
            print(row['last_name'],row['tel'])
    return db

# def read_pandas():

#     import pandas #could not be resolved  
#     df = pandas.read_csv('spr_tel.csv')   
#     print(type(df))


