from utility import *


def list_incomplete_attributes(data: MyData):
    """
    ...

    :param data: ...
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
