def get_data(file_path):
    with open(file_path) as medic_database:
        data = medic_database.readlines()
    return data


if __name__ == '__main__':
    path = '../data/doctors_list'
    data_entries = get_data(path)
    for entry in data_entries:
        print(entry)
