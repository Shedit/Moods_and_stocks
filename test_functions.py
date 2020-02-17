import unittest 

from functions import *


import pandas as pd

class TestGetdata(unittest.TestCase):
    def test_import_contains_pandas_dataframe_type(self):
        """
        Test that the function ensures that it imports form the api
        """
        data = {'First Column Name':  ['First value', 'Second value'],
        'Second Column Name': ['First value', 'Second value']
        }

        df = pd.DataFrame(data, columns = ['First Column Name','Second Column Name'])
        import_data = get_data()
        self.assertEqual(type(import_data), type(df))

class TestDiff(unittest.TestCase):
    def test_that_difference_is_done(self):
        """
        Test that ensure it takes the right difference
        """
        data = {'Test Column': [1,2,3,4,5,6,7,8]}
        df = pd.DataFrame(data, columns = ['Test Column'])
        diffdata = diff_data(df)
        self.assertEqual(diffdata, [1,1,1,1,1,1,1])

if __name__ == '__main__':
    unittest.main()
