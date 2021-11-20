from utility import *


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    data = DataPreprocess(df)

    execute_commands(data, args)
