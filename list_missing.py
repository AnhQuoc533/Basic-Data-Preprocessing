from utility import *


def list_incomplete_attributes(data: MyData):
    """
    Print a list of attributes having missing values.

    :param data: the dataset.
    """

    for index in range(len(data.attributes)):
        for sample in data.samples:
            if sample[index] == 'nan':
                print(data.attributes[index])
                break


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    list_incomplete_attributes(MyData(args.input))
