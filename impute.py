from utility import *


def mode(lst):
    return max(set(lst), key=lst.count)


def mean(lst):
    return sum(lst) / len(lst)


def median(lst):
    quotient, remainder = divmod(len(lst), 2)

    if remainder:
        return sorted(lst)[quotient]
    return sum(sorted(lst)[quotient - 1:quotient + 1]) / 2

def add_args(arg_parser):
    arg_parser.add_argument('-m', '--method', required=True,
                            choices=['mean', 'median', 'mode'], help='Choose a imputation method.')
    arg_parser.add_argument('-a', '--attributes', nargs='+', type=str, help='Select attribute(s) to impute.')
    arg_parser.add_argument('-o', '--output', metavar='FILENAME', type=str, help='Save the data into a file.')


def impute(data: MyData, method, attributes: set):
    if method == 'mode':
        if attributes.issubset(data.get_attributes_by_type('nominal')):
            for attribute in attributes:
                index = data.attributes.index(attribute)
                value = mode([samples[index] for samples in data.samples if samples[index] != 'nan'])

                for samples in data.samples:
                    if samples[index] == 'nan':
                        samples[index] = value
        else:
            raise ValueError('Selected attributes do not exist or are not nominal.')

    elif method in {'mean', 'median'}:
        if attributes.issubset(data.get_attributes_by_type('numeric')):
            for attribute in attributes:
                index = data.attributes.index(attribute)

                if method == 'mean':
                    value = mean([float(samples[index]) for samples in data.samples if samples[index] != 'nan'])
                else:
                    value = median([float(samples[index]) for samples in data.samples if samples[index] != 'nan'])
                value = str(int(value)) if value == int(value) else str(value)

                for samples in data.samples:
                    if samples[index] == 'nan':
                        samples[index] = value
        else:
            raise ValueError('Selected attributes do not exist or are not numeric.')


if __name__ == '__main__':
    parser = create_parser()
    add_args(parser)
    args = parser.parse_args()

    my_data = MyData(args.input)
    impute(my_data, args.method, set(args.attributes))
    if args.output:
        my_data.save_data(args.output)
