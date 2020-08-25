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
