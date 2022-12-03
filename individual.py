#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    products = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            prod = input("Введите название товара: ")
            shop = input("Введите название магазина: ")
            cost = float(input("Введите стоимость товара: "))
            product  = {
                'product': prod,
                'shop': shop,
                'cost': cost
            }

            products.append(product)
            if len(products) > 1:
                products.sort(key=lambda item: item.get('shop', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20
            )
            print(line)
            print(
                '| {:^25} | {:^15} | {:^14} |'.format(
                    "Товар",
                    "Магазин",
                    "Стоимость"
                )
            )
            print(line)

            for product in products:
                print(
                    '| {:^25} | {:^15} | {:^14} |'.format(
                        product.get('product', ''),
                        product.get('shop',''),
                        product.get('cost','')
                    )
                )
            print(line)

        elif command == 'select':
            sel_shop = input("Введите магазин: ")

            n = 0
            for product in products:
                if product.get('shop', '') == sel_shop:
                    print(
                        '| {:^25} | {:^15} | {:^14} |'.format(
                            product.get('product', ''),
                            product.get('shop', ''),
                            product.get('cost', '')
                        )
                    )
                    n += 1
            if n == 0:
                print("Магазин не найден!")

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить информацию о товаре;")
            print("list - вывести список товаров;")
            print("select - запросить товары из одного магазина;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)

