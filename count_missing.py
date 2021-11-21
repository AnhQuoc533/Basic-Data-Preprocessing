from utility import *


def count_incomplete_samples(data: MyData):
    count = 0
    for sample in data.samples:
        for element in sample:
            if element == 'nan':
                count += 1
                break
    return count


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    print(count_incomplete_samples(MyData(args.input)))
