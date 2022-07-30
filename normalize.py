from utility import *


def add_args(arg_parser):
    arg_parser.add_argument('-m', '--method', required=True,
                            choices=['min-max', 'z-score'], help='Choose a normalization method.')
    arg_parser.add_argument('-a', '--attributes', nargs='+', type=str, help='Select numeric attribute(s) to normalize.')
    arg_parser.add_argument('-o', '--output', metavar='FILENAME', type=str, help='Save the data into a file.')


def min_max_scaling(data: MyData, attribute: str):
    """Scale all values in the numeric attribute into a range of [0,1].
    Missing values are ignored.

    :param data: the dataset.
    :param attribute: name of a numeric attribute in the dataset whose values are to be scaled.
    """
    
    index = data.attributes.index(attribute)
    temp = [float(samples[index]) for samples in data.samples if samples[index] != 'nan']
    min_val = min(temp)
    max_val = max(temp)

    for samples in data.samples:
        if samples[index] != 'nan':
            samples[index] = str((float(samples[index]) - min_val) / (max_val - min_val))


def standardize(data: MyData, attribute: str):
    """Standardize all values in the numeric attribute by replacing the values with their Z-scores.
    Missing values are ignored.

    :param data: the dataset.
    :param attribute: name of a numeric attribute in the dataset whose values are to be standardized.
    """
    
    index = data.attributes.index(attribute)
    temp = [float(samples[index]) for samples in data.samples if samples[index] != 'nan']

    mean = sum(temp) / len(temp)
    variance = sum((val - mean)**2 for val in temp) / len(temp)
    std = variance ** (1/2)

    for samples in data.samples:
        if samples[index] != 'nan':
            samples[index] = (float(samples[index]) - mean) / std
            samples[index] = str(samples[index])


def normalize(data: MyData, method: str, attributes: set):
    """Normalize all values in the numeric attributes of the dataset using z-score or min-max method.

    :param data: the dataset.
    :param method: name of normalization method to be used.
    :param attributes: a set of numeric attributes whose values are to be normalized.
    """

    if not len(attributes):
        return
    if not attributes.issubset(data.get_attributes_by_type('numeric')):
        raise ValueError('Selected attributes do not exist or are not numeric.')

    if method == 'min-max':
        for attribute in attributes:
            min_max_scaling(data, attribute)
    elif method == 'z-score':
        for attribute in attributes:
            standardize(data, attribute)
    else:
        raise ValueError('Invalid normalization method.')


if __name__ == '__main__':
    parser = create_parser()
    add_args(parser)
    args = parser.parse_args()

    my_data = MyData(args.input)
    try:
        normalize(my_data, args.method, set(args.attributes))

        if args.output:
            my_data.save_data(args.output)
    except Exception as e:
        print(e)
