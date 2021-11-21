import pandas as pd
import argparse
DESC = "This program accepts a CSV file, with comma being the delimiter, as input. In the file, the first row " \
       "contains the names of the columns of the dataset (attributes) and the following rows contains the data " \
       "(samples)."


class MyData:
    def __init__(self, csv_filename: str):
        df = pd.read_csv(csv_filename)
        self.attributes = list(df.columns)
        self.samples = df.values.astype(str).tolist()
        self.n = len(self.samples)
        self.dtypes = self.get_dtypes()

    def get_dtypes(self):
        dtypes = dict.fromkeys(self.attributes, 'unknown')
        for j in range(len(self.attributes)):
            for i in range(self.n):
                if self.samples[i][j] != 'nan':
                    dtypes[self.attributes[j]] = 'numeric' if self.isfloat(self.samples[i][j]) else 'nominal'
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
        attribute_set = set()
        for attribute in self.attributes:
            if self.dtypes[attribute] == d_type:
                attribute_set.add(attribute)
        return attribute_set

    def save_data(self, filename):
        with open(filename, 'w') as f:
            f.write(','.join(self.attributes))
            f.write('\n')

            for sample in self.samples:
                sample = [element if element != 'nan' else '' for element in sample]
                f.write(','.join(sample))
                f.write('\n')


def minsuprow(lst, sup):
    to_be_del = []
    for count, value in enumerate(lst):
        if value.count('nan')/len(value) > sup:
            to_be_del.append(count)
    to_be_del = sorted(to_be_del, reverse=True)
    for i in to_be_del:
        lst.pop(i)
    return lst


def minsupcol(lst, sup):
    to_be_del = []
    for i in range(len(lst[0])):
        temp = [row[i] for row in lst]
        if temp.count('nan')/len(lst[0]) > sup:
            to_be_del.append(i)
    to_be_del = sorted(to_be_del, reverse=True)
    for i in to_be_del:
        for j in lst:
            j.pop(i)
    return lst

def minmax(lst):
    lst = [float(i) for i in lst]
    lst = [(i-min(lst))/(max(lst)-min(lst)) for i in lst]
    return lst

def zscore(lst):
    val = [i for i in lst if i == i]
    val = [float(i) for i in val]
    mean = sum(val)/len(val)
    std = (sum([(i-mean)**2 for i in val])/len(val))**1/2
    lst = [(float(i)-mean)/std for i in lst]
    return lst

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
        if c not in {'+', '-', '*', '/', '(', ')'}:
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
    term = ''
    while stack:
        postfix += stack.pop()
    postfix = list(filter(('').__ne__, postfix))
    return postfix

def eval(lab, lst, pf):
    stack = []
    res = []
    for term in pf:
        print(*stack, sep='\n', end='\n\n')
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
    return stack[-1]

def create_parser():
    parser = argparse.ArgumentParser(description=DESC)
    parser.add_argument('input', type=str, metavar='INPUT')
    return parser
