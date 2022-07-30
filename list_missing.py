from utility import *


def list_incomplete_attributes(data: MyData):
    """Print a list of attributes with missing values.

    :param data: the dataset.
    """

    # for i in range(len(data.attributes)):
    #     for sample in data.samples:
    #         if sample[i] == 'nan':
    #             print(data.attributes[i])
    #             break

    for i, column in enumerate(zip(*data.samples)):
        if 'nan' in column:
            print(data.attributes[i])


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    list_incomplete_attributes(MyData(args.input))
