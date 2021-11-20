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
        attr = []
        for j in range(len(self.attributes)):
            for i in range(self.n):
                if self.samples[i][j] != self.samples[i][j]:
                    attr.append(self.attributes[j])
                    break
        return attr

    def count_incomplete_samples(self):
        count = 0
        for sample in self.samples:
            for element in sample:
                if element != element:
                    count += 1
                    break
        return count

    def save_data(self, filename):
        with open(filename, 'w') as f:
            f.write(','.join(self.attributes))
            f.write('\n')

            for sample in self.samples:
                sample = [str(element) if element == element else '' for element in sample]
                f.write(','.join(sample))
                f.write('\n')


def create_parser():
    parser = argparse.ArgumentParser(description=DESC)
    parser.add_argument('input', type=str, metavar='INPUT')
    parser.add_argument('-l', '--list', action='store_true', help='List all attributes having missing values.')
    parser.add_argument('-c', '--count', action='store_true', help='Count all samples having missing values.')
    parser.add_argument('-i', '--impute', choices=['mean', 'median', 'mode'], help='Replace missing values.')
    parser.add_argument('-o', '--output', metavar='FILENAME', type=str, help='Save the data into a file.')

    return parser


def execute_commands(data: DataPreprocess, args, /):
    if args.list:
        print('List of attributes with missing values: ', data.list_incomplete_attributes())
    if args.count:
        print('Number of samples with missing values: ', data.count_incomplete_samples())
    if args.output:
        data.save_data(args.output)
    pass
