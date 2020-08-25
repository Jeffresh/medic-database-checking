import string

letter_UP = string.ascii_uppercase
digits = string.digits
rows = {letter: row for (row, letter) in enumerate(letter_UP[:11])}
rows.update({'X': 11})


class Letter:
    LETTERS = string.ascii_lowercase

    def __eq__(self, other):
        return other in Letter.LETTERS


letter_column = Letter()
columns = [letter_column, ","] + [str(i) for i in range(10)] + ['C', 'S']


def generate_table(values):
    transition_table = [["X"] * 14 for _ in range(12)]
    for key, value in values.items():
        for index in value:
            transition_table[index[0]][index[1]] = key
    return transition_table


def get_data(file_path):
    with open(file_path) as medic_database:
        data = medic_database.readlines()
    return data


def check_entries():
    pass


def print_table(table):
    print('   ', *[[n] for n in range(14)], sep='  ')
    for n, row in enumerate(table):
        print([n], row)


if __name__ == '__main__':
    path = '../data/doctors_list'
    data_entries = get_data(path)
    # for entry in data_entries:
    #     print(entry)

    table_values = {'B': [[0, 0], [1, 0]], 'C': [[1, 1]], 'D': [[2, 0], [3, 0]], 'E': [[3, 1]],
              'F': [[4, 0], [5, 0]], 'G': [[5, 1]], 'H': [[4, 4], [6, 4]], 'I': [[7, 10], [7, 11]],
              'J': [[8, 1]], 'K': [[9, 12], [9, 13]]}
    print_table(generate_table(table_values))
