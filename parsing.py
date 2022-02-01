import csv
with open("D:\Python\prsg_iptel\call-history.csv", encoding='utf-8') as r_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ",")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла
    for row in file_reader:
        if count == 0:
            # Вывод строки, содержащей заголовки для столбцов
            print(f'Файл содержит столбцы: {", ".join(row)}')
        else:
            if row[3]=='Extension':
                row[3]='Исходящий'
            else:
                row[3]='Входящий '
            # Вывод строк
            print(f' Тип вызова: {row[3]}   |   {row[0]} - Номер: {row[1]}               Вызываемый номер: {row[4]}   Время звонка: {row[7]} {row[8]}   ')
        count += 1
    print(f'Всего в файле {count} строк.')
