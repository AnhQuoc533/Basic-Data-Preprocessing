from utility import *


def remove_clone(data: MyData):
    """Remove duplicate samples in the dataset.

    :param data: the dataset.
    """

    new_data = []
    for sample in data.samples:
        if sample not in new_data:
            new_data.append(sample)

    data.samples = new_data
    data.n = len(data.samples)


if __name__ == '__main__':
    parser = create_parser()
    parser.add_argument('-o', '--output', metavar='FILENAME', type=str, help='Save the data into a file.')
    args = parser.parse_args()

    my_data = MyData(args.input)
    remove_clone(my_data)

    if args.output:
        try:
            my_data.save_data(args.output)
        except Exception as e:
            print(e)
