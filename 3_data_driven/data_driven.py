"""Модуль для генерации тестовых данных"""

import pandas

def data_generator(names, cities):
    """Генерируем комбинации данных"""
    for name in names:
        for city in cities:
            for card in '+-':
                for account in "+-":
                    for mortgage in '+-':
                        yield f"{name} {city} {card} {account} {mortgage}\n"

def read_results():
    """Чтение файла с результатами"""
    file_read = open('results.txt', 'r')
    for line in file_read:
        print(line.split(' '))

if __name__ == "__main__":
    DATA_FRAME = pandas.read_csv('data2.csv', encoding="windows-1251",
                                 dtype={'ФИО': str, 'Город': str})
    DATA_FRAME['ФИО'] = DATA_FRAME['ФИО'].str[:-1] # перемещен невалидный символ

    FILE_WRITE = open('results.txt', 'w')# открытие файла с исходными данными
    for data in data_generator(DATA_FRAME['ФИО'].unique(), DATA_FRAME['Город'].unique()):
        FILE_WRITE.write(data)
