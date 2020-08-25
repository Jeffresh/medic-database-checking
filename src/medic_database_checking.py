import re
import string

letter_UP = string.ascii_uppercase
digits = string.digits
rows = {letter: row for (row, letter) in enumerate(letter_UP[:13])}
rows.update({'X': 13})


class Letter:
    LETTERS = string.ascii_lowercase

    def __eq__(self, other):
        return other in Letter.LETTERS


letter_column = Letter()
columns = [letter_column, ','] + [str(i) for i in range(10)] + ['C', 'S']


def generate_table(values):
    table = [["X"] * 14 for _ in range(14)]
    for key, value in values.items():
        for index in value:
            table[index[0]][index[1]] = key
    return table


def get_data(file_path):
    with open(file_path) as medic_database:
        data = medic_database.readlines()
    return data


def check_entries(data, transition_table):
    for entry in data:
        row = 'A'
        entry = ''.join(entry.split())
        for symbol in entry:
            row = transition_table[rows[row]][columns.index(symbol)]

        if row == 'M':
            print(entry, ' ---> ACCEPTED')
        else:
            print(entry, ' ---> REJECTED')


def print_table(table):
    print('   ', *[[n] for n in range(14)], sep='  ')
    for n, row in enumerate(table):
        print([n], row)


if __name__ == '__main__':
    path = 'data/doctors_list'
    data_entries = get_data(path)

    table_values = {'B': [[0, 0], [1, 0]], 'C': [[1, 1]], 'D': [[2, 0], [3, 0]], 'E': [[3, 1]],
                    'F': [[4, 0], [5, 0]], 'G': [[5, 1]], 'H': [[4, 4], [6, 4]], 'I': [[7, 10], [7, 11]],
                    'J': [[8, 1]], 'K': [[9, 0], [10, 0]], 'L': [[10, 1]], 'M': [[11, 12], [11, 13]]}

    transition_table = generate_table(table_values)
    print_table(transition_table)

    check_entries(data_entries, transition_table)

    re.compile(r'([a - z] +,)([a - z] +, )([a - z] +, )?(2[8 - 9] | [3 - 9][0 - 9]),[CD]')

