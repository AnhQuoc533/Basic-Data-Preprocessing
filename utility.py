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
    def __init__(self, csv_filename: str, sep=',', use_default_na=True, add_na_values=None):
        try:
            df = pd.read_csv(csv_filename, sep=sep, keep_default_na=use_default_na, na_values=add_na_values)
            self.attributes = list(df.columns)
            self.samples = df.values.astype(str).tolist()
            self.n = len(self.samples)
            self.dtypes = self.__get_dtypes()
        except FileNotFoundError as e:
            print(e)
            exit()

    def __get_dtypes(self):
        dtypes = dict.fromkeys(self.attributes, 'unknown')

        for index, attribute in enumerate(self.attributes):
            for sample in self.samples:
                if sample[index] != 'nan':
                    dtypes[attribute] = 'numeric' if self.isfloat(sample[index]) else 'nominal'
                    break
        return dtypes

    @staticmethod
    def isfloat(string: str):
        """Return True if the string is a float number, False otherwise.

        :param string: the string to be asserted.
        :return: a boolean.
        """

        try:
            _ = float(string)
            return True
        except ValueError:
            return False

    def get_attributes_by_type(self, d_type: str):
        """Return a set of attributes of specified data type (numeric or nominal).

        :param d_type: the name of data type.
        :return: a set of attributes.
        """

        return {attribute for attribute in self.attributes if self.dtypes[attribute] == d_type}

    def save_data(self, csv_filename: str, sep=',', na_repr=''):
        """Save the dataset into the file.

        :param csv_filename: the name or the path of the .csv file to be saved to.
        :param sep: field delimiter for the .csv file.
        :param na_repr: missing data representation.
        """

        with open(csv_filename, 'w') as f:
            f.write(sep.join(self.attributes))
            f.write('\n')

            for sample in self.samples:
                sample = [element if element != 'nan' else na_repr for element in sample]
                f.write(sep.join(sample))
                f.write('\n')
