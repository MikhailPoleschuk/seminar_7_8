def what_do():
    print('Добро пожаловать в наш справочник, что вы хотите с ним сделать:')
    print('1. Найти  контакт')
    print('2. Добавить контакт')
    print('3. Удалить контакт')
    print('4. Изменить контакт')

    to_do = int(input("-->"))
    return to_do


def find_input():
    who = input("Введите что ищем-->")
    return who


def add_input():
    soname = input("Фамилия-->")
    name = input("Имя-->")
    tel = input("tel-->")
    list_data = [soname, name, tel]
    return list_data
