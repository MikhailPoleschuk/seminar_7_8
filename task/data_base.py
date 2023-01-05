def write_(a,znak,b):
    
    file_path = r'db.txt'
    with open(file_path, 'w') as f_data:
        f_data.writelines(f'{a}|{znak}|{b}')


def read_():
    file_path = r'db.txt'
    with open(file_path, 'r') as f_data:
        string = f_data.readline()
        
    return string
