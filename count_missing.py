from utility import *


def count_incomplete_samples(data: MyData):
    """Return the number of samples with missing values in a dataset.

    :param data: the dataset.
    :return: an integer representing the number of samples with missing values.
    """

    count = 0
    for sample in data.samples:
        if 'nan' in sample:
            count += 1
    return count


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    print(count_incomplete_samples(MyData(args.input)))
