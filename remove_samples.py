from utility import *


def add_args(arg_parser):
    arg_parser.add_argument('-t', '--threshold', required=True, type=int,
                            help='Choose a threshold for missing value rate, from 0 to 100.')
    arg_parser.add_argument('-o', '--output', metavar='FILENAME', type=str, help='Save the data into a file.')


def remove_sample(data: MyData, threshold: int):
    """
    Remove attributes with missing value rate over a certain threshold.

    """

    if threshold < 0 or threshold > 100:
        raise ValueError('Threshold value must be in the range 0 - 100.')
    limit = int(data.n * threshold/100)

    for i in reversed(range(data.n)):
        if data.samples[i].count('nan') > limit:
            del data.samples[i]

    data.n = len(data.samples)


if __name__ == '__main__':
    parser = create_parser()
    add_args(parser)
    args = parser.parse_args()

    my_data = MyData(args.input)
    remove_sample(my_data, args.threshold)

    if args.output:
        my_data.save_data(args.output)
