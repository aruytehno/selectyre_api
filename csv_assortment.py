import csv


# Write CSV file
def write_csv(file_name, data):
    with open(file_name, "wt") as fp:
        writer = csv.writer(fp, delimiter=",")
        # writer.writerow(["your", "header", "foo"])  # Записать заголовки
        writer.writerows(data)


# Read CSV file
def read_csv(file_name):
    with open(file_name) as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        # next(reader, None)  # Пропустить заголовки
        data_read = [row for row in reader]
    return data_read
