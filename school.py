#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    school = {
        '1A': 30,
        '1Б': 28,
        '2A': 29,
        '2Б': 29,
        '2В': 29,
        '3A': 30,
        '3Б': 29,
        '4A': 28,
        '4Б': 29,
        '4В': 25,
        '5А': 27,
        '5Б': 25,
        '6А': 29,
        '6Б': 27,
        '6В': 23,
        '7А': 32,
        '8А': 30,
        '8Б': 19,
        '9А': 29,
        '9Б': 27,
        '9В': 21,
        '10А': 22,
        '10Б': 15,
        '11А': 17,
        '11Б': 16
    }

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            class_num = input("Введите число и букву класса: ")
            pupils = int(input("Кол-во человек? "))
            school[class_num] = pupils

        elif command == "list":
            for item in school:
                print(f"Класс {item}, учеников {school[item]}")

        elif command == 'delete':
            while True:
                del_class = input("Введите удаляемый класс(для выхода exit): ")

                if del_class == 'exit':
                    break

                elif del_class in school:
                    school.pop(del_class)

                else:
                    print("Введённого класса не существует")

        elif command == 'count':
            count = 0
            for i, item in enumerate(school):
                count += school[item]
            print(count)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить класс;")
            print("list - вывести список школьных классов;")
            print("delete - удалить школьный класс;")
            print("count - удалить школьный класс;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)