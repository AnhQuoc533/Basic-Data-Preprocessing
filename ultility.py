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
