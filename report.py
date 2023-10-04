import csv
from collections import defaultdict


def open_csv_file(input_path: str) -> list|str:
    """
    The function reads a csv file and saves it in the form of a list consisting of lists
    :param input_path: The path to csv file we are getting information from
    :type: str
    :return: list or str
    """
    try:
        with open(input_path, encoding='utf-8', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            data = list(reader)
            return data[1::]
    except FileNotFoundError:
        return 'Ссылка на файл не корректна. Попробуйте еще раз!'


def command_hierarchy(data: list) -> None:
    """
    The function gets a list with the profiles of each employee in the company
    and displays the department and the branches that they include
    :param data: The list of the profiles of each employee
    :type: list
    :return: None
    """
    departments_branches = defaultdict(set)
    for lst in data:
        departments_branches[lst[1]].add(lst[2])
    print("Иерархия команд:")
    print()
    for department, branches in departments_branches.items():
        print(f"Название департамента:\n{department}")
        print("Отделы, входящие в этот департамент: ", *branches, sep='\n')
        print()


def total_report(data: list) -> list:
    """
    The function gets a list with the profiles of each employee in the company
    and displays the report on each department
    :param data: The list of the profiles of each employee
    :type: list
    :return: list
    """
    salary = defaultdict(list)
    for lst in data:
        salary[lst[1]].append(int(lst[-1]))
    report = []
    for key, value in salary.items():
        line = [
            key, len(value), min(value), max(value), (sum(value) // len(value))
        ]
        report.append(line)
    return report


def summary_report(report: list) -> None:
    """
    The function gets a list with the report on each department and displays it
    :param report: The list the report on each department
    :type: list
    :return: None
    """
    print('Сводный отчёт по департаментам:')
    for lst in report:
        print(f'Департамент: {lst[0]}')
        print(f'Численность: {lst[1]}')
        print('"Вилка" зарплат:')
        print(f'Минимальная зарплата: {lst[2]}')
        print(f'Максимальная зарплата: {lst[3]}')
        print(f'Средняя зарплата: {lst[4]}')
        print('-' * 30)


def close_csv_file(report: list, output_path: str) -> None:
    """
    The function gets the list with the summary report on each department
    and writes it to a csv file
    :param report: The list the report on each department
    :type: list
    :param output_path: The path to csv file we are writing information in
    :type: str
    :return: None
    """
    columns = ['Департамент', 'Численность', 'Минимальная зарплата',
               'Максимальная зарплата', 'Средняя зарплата']
    with open(output_path, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(columns)
        writer.writerows(report)
    print('Ваш отчет сохранен.')


def main() -> None:
    """
    The function gives several options to choose from and performs the specified actions set in them
    :return: None
    """
    options = {0: '0. Выход',
               1: '1. Вывести иерархию команд',
               2: '2. Вывести сводный отчёт по департаментам',
               3: '3. Сохранить сводный отчёт в виде csv-файла'}
    print('Добрый день!', *options.values(), sep='\n')
    var = ''
    if var == 0:
        return None
    while var != 0:
        var = int(input('Выберете опцию(0/1/2/3): '))
        while var not in options:
            try:
                var = int(input('Выберете опцию(0/1/2/3): '))
            except ValueError:
                print('Введите цифру из предложенных.')
        if var == 1:
            data = input('Введите название csv файла, с которым будем работать: ')
            while not data[-4:] == '.csv':
                print('Название файла введено неверно.')
                data = input('Введите название csv файла, с которым будем работать: ')
            command_hierarchy(open_csv_file(data))
        elif var == 2:
            data = input('Введите название csv файла, с которым будем работать: ')
            while not data[-4:] == '.csv':
                print('Название файла введено неверно.')
                data = input('Введите название csv файла, с которым будем работать: ')
            summary_report(total_report(open_csv_file(data)))
        elif var == 3:
            data = input('Введите название csv файла, с которым будем работать: ')
            while not data[-4:] == '.csv':
                print('Название файла введено неверно.')
                data = input('Введите название csv файла, с которым будем работать: ')
            output_path = input('Введите название csv файла в который вы хотите сохранить сводный отчет: ')
            while not output_path[-4:] == '.csv':
                print('Название файла введено неверно.')
                output_path = input('Введите название csv файла в который вы хотите сохранить сводный отчет: ')
            close_csv_file(total_report(open_csv_file(data)), output_path)


if __name__ == '__main__':
    main()

