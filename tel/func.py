import csv



def find(str):

    with open('spr_tel.csv', 'r', encoding="utf-8") as file:
        db = csv.reader(file)

        found = 0
        for item in db:
            
            if str in item:
                print(item)
                found = 1

        if (found == 0):
            print('not found')


def add(list_data):
    
    with open('spr_tel.csv', 'a', encoding="utf-8",newline='') as file:
        writer_object= csv.writer(file)
        writer_object.writerow(list_data)
        file.close()    

    return print("Write OK")
