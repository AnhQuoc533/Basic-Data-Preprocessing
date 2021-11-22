from utility import *


def mode(lst):
    """
    Return the single most common data point from discrete or nominal data.
    The mode (when it exists) is the most typical value and serves as a measure of central location.

    :param lst: sequence of data.
    :return: the mode of the sequence.
    """

    return max(set(lst), key=lst.count)


def mean(lst):
    """
    Return the sample arithmetic mean of numeric data which can be a sequence or iterable.

    :param lst: sequence of data.
    :return: the mean of the sequence.
    """

    return sum(lst) / len(lst)


def median(lst):
    """
    Return the median (middle value) of numeric data, using the common "mean of middle two" method.

    :param lst: sequence of data.
    :return: the median of the sequence.
    """

    quotient, remainder = divmod(len(lst), 2)
    if remainder:
        return sorted(lst)[quotient]
    return sum(sorted(lst)[quotient - 1:quotient + 1]) / 2


def add_args(arg_parser):
    arg_parser.add_argument('-m', '--method', required=True,
                            choices=['mean', 'median', 'mode'], help='Choose a imputation method.')
    arg_parser.add_argument('-a', '--attributes', nargs='+', type=str, help='Select attribute(s) to impute.')
    arg_parser.add_argument('-o', '--output', metavar='FILENAME', type=str, help='Save the data into a file.')


def impute(data: MyData, method: str, attributes: set):
    """
    Impute missing values in attributes of the dataset using the method mean or median (for numeric attributes),
    or mode (for nominal attributes).

    :param data: the dataset.
    :param method: name of imputation method to be used.
    :param attributes: a set of attributes whose missing values are to be filled in.
    """

    if not len(attributes):
        return

    if method == 'mode':
        if attributes.issubset(data.get_attributes_by_type('nominal')):
            for attribute in attributes:
                index = data.attributes.index(attribute)
                value = mode([samples[index] for samples in data.samples if samples[index] != 'nan'])

                for samples in data.samples:
                    if samples[index] == 'nan':
                        samples[index] = value
        else:
            raise ValueError('Selected attributes do not exist or are not nominal.')

    elif method in {'mean', 'median'}:
        if attributes.issubset(data.get_attributes_by_type('numeric')):
            for attribute in attributes:
                index = data.attributes.index(attribute)

                if method == 'mean':
                    value = mean([float(samples[index]) for samples in data.samples if samples[index] != 'nan'])
                else:
                    value = median([float(samples[index]) for samples in data.samples if samples[index] != 'nan'])
                value = str(int(value)) if value == int(value) else str(value)

                for samples in data.samples:
                    if samples[index] == 'nan':
                        samples[index] = value
        else:
            raise ValueError('Selected attributes do not exist or are not numeric.')

    else:
        raise ValueError('Invalid imputation method.')


if __name__ == '__main__':
    parser = create_parser()
    add_args(parser)
    args = parser.parse_args()

    my_data = MyData(args.input)
    impute(my_data, args.method, set(args.attributes))

    if args.output:
        my_data.save_data(args.output)
