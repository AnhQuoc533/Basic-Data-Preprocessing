from utility import *


def remove_nan(lst):
    return [i for i in lst if i == i]


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
    return arg_parser


def impute(data: MyData, arg):
    pass


def save_data(data: MyData, filename):
    with open(filename, 'w') as f:
        f.write(','.join(data.attributes))
        f.write('\n')

        for sample in data.samples:
            sample = [str(element) for element in sample]
            f.write(','.join(sample))
            f.write('\n')


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    my_data = MyData(args.input)
    impute(my_data, args)
    if args.output:
        save_data(my_data, args.output)
