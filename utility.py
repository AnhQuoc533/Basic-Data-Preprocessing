import pandas as pd
import argparse
DESC = "This program accepts a CSV file, with comma being the delimiter, as input. In the file, the first row " \
       "contains the names of the columns of the dataset (attributes) and the following rows contains the data " \
       "(samples)."


def create_parser():
    parser = argparse.ArgumentParser(description=DESC)
    parser.add_argument('input', type=str, metavar='INPUT')
    return parser


class MyData:
    def __init__(self, csv_filename: str):
        df = pd.read_csv(csv_filename)
        self.attributes = list(df.columns)
        self.samples = df.values.astype(str).tolist()
        self.n = len(self.samples)
        self.dtypes = self._get_dtypes()

    def _get_dtypes(self):
        dtypes = dict.fromkeys(self.attributes, 'unknown')

        for index, attribute in enumerate(self.attributes):
            for sample in self.samples:
                if sample[index] != 'nan':
                    dtypes[attribute] = 'numeric' if self.isfloat(sample[index]) else 'nominal'
                    break
        return dtypes

    @staticmethod
    def isfloat(num: str):
        try:
            num = float(num)
            return True
        except ValueError:
            return False

    def get_attributes_by_type(self, d_type: str):
        """
        ...

        :param d_type: ...
        :return: ...
        """

        return {attribute for attribute in self.attributes if self.dtypes[attribute] == d_type}

    def save_data(self, filename: str):
        """
        ...

        :param filename: ...
        """

        with open(filename, 'w') as f:
            f.write(','.join(self.attributes))
            f.write('\n')

            for sample in self.samples:
                sample = [element if element != 'nan' else '' for element in sample]
                f.write(','.join(sample))
                f.write('\n')


def hasLessOrEqualPriority(a, b):
    if b == '(':
        return False
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    try:
        if precedence[a] <= precedence[b]:
            return True
        else:
            return False
    except KeyError:
        return False


def toPostfix(infix):
    stack = []
    postfix = []
    term = ''
    for c in infix:
        if c not in '+-/*()':
            term += c
        else:
            postfix.append(term)
            term = ''
            if c == '(':
                stack.append(c)
            elif c == ')':
                operator = stack.pop()
                while stack and operator != '(':
                    postfix += operator
                    operator = stack.pop()
            else:
                while stack and hasLessOrEqualPriority(c, stack[-1]):
                    postfix += stack.pop()
                stack.append(c)
    postfix.append(term)
    while stack:
        postfix += stack.pop()
    postfix = list(filter(('').__ne__, postfix))
    return postfix


def eval(lab, lst, pf):
    stack = []
    for term in pf:
        if '+' in term:
            a = stack.pop()
            b = stack.pop()
            temp = [j + i for i, j in zip(a,b)]
            stack.append(temp)
        elif '-' in term:
            a = stack.pop()
            b = stack.pop()
            temp = [j - i for i, j in zip(a, b)]
            stack.append(temp)
        elif '*' in term:
            a = stack.pop()
            b = stack.pop()
            temp = [i * j for i, j in zip(a, b)]
            stack.append(temp)
        elif '/' in term:
            a = stack.pop()
            b = stack.pop()
            temp = [j / i for i, j in zip(a, b)]
            stack.append(temp)
        else:
            stack.append([row[lab.index(term)] for row in lst])
    return stack.pop()
