from utility import *


def list_incomplete_attributes(data: MyData):
    for j in range(len(data.attributes)):
        for i in range(data.n):
            if data.samples[i][j] != data.samples[i][j]:
                print(data.attributes[j])
                break


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    list_incomplete_attributes(MyData(args.input))
