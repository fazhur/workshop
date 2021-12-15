import csv 

def read_csv(path):
    dct = {}

    with open(path) as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for i in csvreader:
            dct.update({i[0]: i[1]})

        return dct 


def write_csv(path, dct):
    with open(path) as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=["Task", "Deadline"])
        csvwriter.writeheader()
        csvwriter.writerows(dct)


if __name__ == '__main__':
    dct = read_csv('123.csv')
    print(dct)
    write_csv("123.csv", dct)
