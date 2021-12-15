import csv 

def read_csv(path):
    dct = {}

    with open(path) as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for i in csvreader:
            dct.update({i[0]: i[1]})

        return dct 


if __name__ == '__main__':
    print(read_csv('123.csv'))
