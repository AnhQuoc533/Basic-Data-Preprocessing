import argparse
DESC = "Data Preprocessing\n" \
       "This program accepts a CSV file, with comma being the delimiter, as input. In the file, the first row " \
       "contains the names of the columns of the dataset (attributes) and the following rows contains the data " \
       "(samples). Depending on the command, the program can output the results to the screen or save to a file."


class DataPreprocess:
    def __init__(self, attributes: list, samples: list):
        self.attributes = attributes
        self.samples = samples
        self.n = len(samples)

    def list_incomplete_attributes(self):
        for j in range(len(self.attributes)):
            for i in range(self.n):
                if self.samples[i][j] != self.samples[i][j]:
                    print(self.attributes[j])
                    break

    def save_data(self, filename):
        with open(filename, 'w') as f:
            f.write(','.join(self.attributes))
            f.write('\n')

            for sample in self.samples:
                sample = [str(element) if element == element else '' for element in sample]
                f.write(','.join(sample))
                f.write('\n')

def mode(lst):
    return max(set(lst), key=lst.count)

def mean(lst):
    x = list(filter(('nan').__ne__, lst))
    return sum([float(i) for i in lst])/len(lst)

def median(lst):
    lst = list(filter(('nan').__ne__, lst))
    lst = [float(i) for i in lst]
    quotient, remainder = divmod(len(lst), 2)
    if remainder:
        return sorted(lst)[quotient]
    return float(sum(sorted(lst)[quotient - 1:quotient + 1]) / 2)

def minsuprow(lst, sup):
    to_be_del = []
    for count, value in enumerate(lst):
        if value.count('nan')/len(value) > sup:
            to_be_del.append(count)
    to_be_del = sorted(to_be_del, reverse=True)
    for i in to_be_del:
        lst.pop(i)
    return lst

def minsupcol(lst, sup):
    to_be_del = []
    for i in range(len(lst[0])):
        temp = [row[i] for row in lst]
        if temp.count('nan')/len(lst[0]) > sup:
            to_be_del.append(i)
    to_be_del = sorted(to_be_del, reverse=True)
    for i in to_be_del:
        for j in lst:
            j.pop(i)
    return lst

def minmax(lst):
    lst = [float(i) for i in lst]
    lst = [(i-min(lst))/(max(lst)-min(lst)) for i in lst]
    return lst

def zscore(lst):
    val = list(filter(('nan').__ne__, lst))
    val = [float(i) for i in val]
    mean = sum(val)/len(val)
    std = (sum([(i-mean)**2 for i in val])/len(val))**1/2
    lst = [(float(i)-mean)/std for i in lst]
    return lst

def create_parser():
    parser = argparse.ArgumentParser(description=DESC)
    parser.add_argument('input', type=str)
    parser.add_argument('-l', '--list', action='store_true', help='List all attributes having missing values.')
    parser.add_argument('-o', '--output', type=str, help='Save the data into a file.')

    return parser


def execute_commands(data: DataPreprocess, args, /):
    if args.list:
        data.list_incomplete_attributes()
    if args.output:
        data.save_data(args.output)
    pass
