import pandas as pd
from utility import *


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    data = pd.read_csv(args.input)
    data = DataPreprocess(list(data.columns), data.values.tolist())

    execute_commands(data, args)
