from funcia_scv import *

if __name__ == '__main__':
    arry_comand = ['save_file', 'new_fail', 'open_file', 'delit_file']
    print("Команды программы: ", arry_comand)
    while True:
        str1 = input('Введите команду: ')

        if str1 == 'exit':
            print("Exit")
            break
        elif str1 == arry_comand[0]:
            print("Выполнилась команда: ", seve_file(str1))
        elif str1 == arry_comand[1]:
            print("Выполнилась команда: ", new_file(str1))
        elif str1 == arry_comand[2]:
            print("Выполнилась команда: ", open_file(str1))
        else:
            print("Выполнилась команда: ", delit_stroka(str1))