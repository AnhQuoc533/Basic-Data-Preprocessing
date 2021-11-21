from utility import *


def count_incomplete_samples(data: MyData):
    """
    ...

    :param data: ...
    :return: ...
    """

    count = 0
    for sample in data.samples:
        for value in sample:
            if value == 'nan':
                count += 1
                break
    return count


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    print(count_incomplete_samples(MyData(args.input)))
