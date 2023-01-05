import csv

def open_db():
    with open('spr_tel.csv', 'r',encoding="utf-8") as file:  
        db = csv.reader(file)
        for row in db:
            print(row)
    return db
