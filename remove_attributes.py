from utility import *


def add_args(arg_parser):
    arg_parser.add_argument('-t', '--threshold', required=True, type=int,
                            help='Choose a threshold for missing value rate, from 0 to 100.')
    arg_parser.add_argument('-o', '--output', metavar='FILENAME', type=str, help='Save the data into a file.')


def remove_attr(data: MyData, threshold: int):
    """
    ...

    :param data: ...
    :param threshold: ...
    """

    if threshold < 0 or threshold > 100:
        raise ValueError('Threshold value must be in the range 0 - 100.')
    limit = int(data.n * threshold/100)

    for index in reversed(range(len(data.attributes))):
        if len([sample[index] for sample in data.samples if sample[index] == 'nan']) > limit:
            for sample in data.samples:
                del sample[index]

            del data.attributes[index]


if __name__ == '__main__':
    parser = create_parser()
    add_args(parser)
    args = parser.parse_args()

    my_data = MyData(args.input)
    remove_attr(my_data, args.threshold)

    if args.output:
        my_data.save_data(args.output)
