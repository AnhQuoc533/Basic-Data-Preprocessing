import argparse
DESC = "Data Preprocessing\n" \
       "This program accepts a CSV file, with comma being the delimiter, as input. In the file, the first row " \
       "contains the names of the columns of the dataset (attributes) and the following rows contains the data " \
       "(samples). Depending on the command, the program can output the results to the screen or save to a file."


class MyData:
    def __init__(self, attributes: list, samples: list):
        self.attributes = attributes
        self.samples = samples
        self.n = len(samples)


def create_parser():
    parser = argparse.ArgumentParser(description=DESC)
    parser.add_argument('input', type=str)
    parser.add_argument('-l', '--list', action='store_true', help='List all attributes having missing values.')

    parser.add_argument('-o', '--output', type=str, help='Save the data into a file.')

    return parser


def execute_commands(data: MyData, args, /):
    if args.list:
        list_attributes(data)

    if args.output:
        save_data(data, args.output)
    pass


def list_attributes(data: MyData):
    for j in range(len(data.attributes)):
        for i in range(data.n):
            if data.samples[i][j] != data.samples[i][j]:
                print(data.attributes[j])
                break


def save_data(data: MyData, filename):
    with open(filename, 'w') as f:
        f.write(','.join(data.attributes))
        f.write('\n')

        for sample in data.samples:
            sample = [str(element) if element == element else '' for element in sample]
            f.write(','.join(sample))
            f.write('\n')
