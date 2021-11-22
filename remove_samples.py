from utility import *


def add_args(arg_parser):
    arg_parser.add_argument('-t', '--threshold', required=True, type=float,
                            help='Choose a threshold for missing value rate, from 0 to 100.')
    arg_parser.add_argument('-o', '--output', metavar='FILENAME', type=str, help='Save the data into a file.')


def remove_sample(data: MyData, threshold: float):
    """
    Remove samples in the dataset whose amount of missing values exceeds the threshold.

    :param data: the dataset.
    :param threshold: the percentage of missing values allowed, (0 - 100).
    """

    if threshold < 0 or threshold > 100:
        raise ValueError('Threshold value must be in the range 0 - 100.')
    limit = int(len(data.attributes) * threshold/100)

    for i in reversed(range(data.n)):
        if data.samples[i].count('nan') > limit:
            del data.samples[i]

    data.n = len(data.samples)


if __name__ == '__main__':
    parser = create_parser()
    add_args(parser)
    args = parser.parse_args()

    my_data = MyData(args.input)
    try:
        remove_sample(my_data, args.threshold)

        if args.output:
            my_data.save_data(args.output)
    except Exception as e:
        print(e)
