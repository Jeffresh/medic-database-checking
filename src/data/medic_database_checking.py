import string

letter_UP = string.ascii_uppercase
digits = string.digits
rows = {letter: row for (row, letter) in enumerate(letter_UP[:11])}
rows.update({'X': 11})


def get_data(file_path):
    with open(file_path) as medic_database:
        data = medic_database.readlines()
    return data


def check_entries():
    pass


if __name__ == '__main__':
    path = '../data/doctors_list'
    data_entries = get_data(path)
    # for entry in data_entries:
    #     print(entry)

