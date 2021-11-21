from utility import *


def add_args(arg_parser):
    arg_parser.add_argument('-m', '--method', required=True,
                            choices=['min-max', 'z-score'], help='Choose a normalization method.')
    arg_parser.add_argument('-a', '--attributes', nargs='+', type=str, help='Select numeric attribute(s) to normalize.')
    arg_parser.add_argument('-o', '--output', metavar='FILENAME', type=str, help='Save the data into a file.')


def normalize(data: MyData, method: str, attributes: set):
    if not len(attributes):
        return
    if not attributes.issubset(data.get_attributes_by_type('numeric')):
        raise ValueError('Selected attributes do not exist or are not numeric.')

    if method == 'min-max':
        for attribute in attributes:
            index = data.attributes.index(attribute)
            temp = [float(samples[index]) for samples in data.samples if samples[index] != 'nan']
            min_val = min(temp)
            max_val = max(temp)

            for samples in data.samples:
                if samples[index] != 'nan':
                    samples[index] = (float(samples[index]) - min_val) / (max_val - min_val)
                    samples[index] = str(samples[index])

    elif method == 'z-score':
        for attribute in attributes:
            index = data.attributes.index(attribute)
            temp = [float(samples[index]) for samples in data.samples if samples[index] != 'nan']

            mean = sum(temp) / len(temp)
            variance = sum([(val-mean)**2 for val in temp]) / len(temp)
            std = variance**(1/2)

            for samples in data.samples:
                if samples[index] != 'nan':
                    samples[index] = (float(samples[index]) - mean) / std
                    samples[index] = str(samples[index])

    else:
        raise ValueError('Invalid normalization method.')


if __name__ == '__main__':
    parser = create_parser()
    add_args(parser)
    args = parser.parse_args()

    my_data = MyData(args.input)
    normalize(my_data, args.method, set(args.attributes))

    if args.output:
        my_data.save_data(args.output)
