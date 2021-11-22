from utility import *


def add_args(arg_parser):
    arg_parser.add_argument('expression', type=str, help='Input expression of numeric attributes.')
    arg_parser.add_argument('-o', '--output', metavar='FILENAME', type=str, help='Save the data into a file.')


def get_variables(expression: str):
    """
    Return a set of variables extracted from the given expression.

    :param expression: a math expression.
    :return: a set of variables.
    """

    signs = {'+', '-', '*', '/', '(', ')'}
    variables = set()
    var = ''

    for char in expression:
        if char not in signs:
            var += char

        elif var:
            if not MyData.isfloat(var):
                variables.add(var)
            var = ''

    if var and not MyData.isfloat(var):
        variables.add(var)

    return variables


def eval_attributes(data: MyData, expression: str):
    """
    Calculate the math expression of numeric attributes and
    add a new attribute (a new column) to the dataset, whose name is the input expression.
    Each value in the new attribute is the result of the calculation of corresponding values in ????

    :param data: the dataset.
    :param expression: the math expression of numeric attributes.
    """

    attributes = get_variables(expression)
    if not attributes.issubset(data.get_attributes_by_type('numeric')):
        raise ValueError('Attributes in the expression do not exist or are not numeric.')

    indices = [(attribute, data.attributes.index(attribute)) for attribute in attributes]
    map_dict = {}

    for sample in data.samples:
        for attribute, index in indices:
            map_dict[attribute] = float(sample[index])

        value = eval(expression, {"__builtins__": None}, map_dict)
        sample.append(str(value))

    data.attributes.append(expression)


if __name__ == '__main__':
    parser = create_parser()
    add_args(parser)
    args = parser.parse_args()

    my_data = MyData(args.input)
    try:
        eval_attributes(my_data, args.expression)

        if args.output:
            my_data.save_data(args.output)
    except Exception as e:
        print(e)
