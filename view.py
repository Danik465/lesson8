# отображение данных  прием данных от пользователя
from function import select_table, insert_in_table


def mode(select_mode):
    mode_sel = 'unknown'
    if select_mode == '1':

        print('Какцю запись вы желаете внести в базу ? ')
        print('1) Добавить ученика\n2) Добавить учителя\n3) Добавить родителя\n4) Добавить урок в расписание\n'
              '5) Добавить предмет(дисциплину)\n6) Добавить время урока\n')

        add_db = input('Введите номер программы')
        mode_sel = add_db
        match add_db:
            case '1':
                ent = (
                input('Id:'), input('Name:'), input('Surname:'), input('Patr:'), input('Number:'), input('Contact:'))
                insert_in_table(con, ent, 'puplis')

            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
            case '6':
                pass

    elif select_mode == '2':
        print('Какцю запись вы желаете изменить в базе ? ')
        print('1) Изменить данные ученика\n2) Изменить данные учителя\n3) Изменить данные родителя\n4) Изменить урок в расписании\n')

        update_db = input('Введите номер программы')
        mode_sel = update_db
        match update_db:
            case '1':
                print('1')
            case '2':
                print('2')
            case '3':
                print('3')
            case '4':
                print('4')

    elif select_mode == '3':
        print('Какцю информацию желаете получить ? ')
        print('1) Расписание\n2) Данные учителя\n3) Данные родителя\n4) Данные ученика\n')

        info = input('Введите номер программы')
        mode_sel = info
        match info:
            case '1':
                print('1')
            case '2':
                print('2')
            case '3':
                print('3')
            case '4':
                print('4')
    else:
        print(f'Данных по запросу {select_mode, mode_sel} нет, попробуете повторить действия и выбрать правильную программу.')


def menu():
    print('Добро пожаловать в интерактивную среду управления Школой №111')
    print('\nВозможности системы:\n1) Внести запись в базу\n2) Изменить данные в базе\n3) Получить информацию\n')
    flag = True
    status = 'activ'
    while flag:

        select = input('Выбирите действие: ')
        mode(select)

        status = input('Желаете продолжить ? y/n')
        if status == 'n':
            print('\nБлагодарим за использование нашей системы.\nВсего доброго!')
            flag = False


def main():
    menu()
