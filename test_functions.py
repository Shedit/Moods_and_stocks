import unittest 
import pytest

from functions import *


import pandas as pd

class TestGetDataIntraday(unittest.TestCase):
    def test_import_contains_pandas_dataframe_type_and_not_None(self):
        """
        Test that the function ensures that it imports form the api
        """
        data = {'First Column Name':  ['First value', 'Second value'],
        'Second Column Name': ['First value', 'Second value']
        }

        df = pd.DataFrame(data, columns = ['First Column Name','Second Column Name'])
        import_data = get_data_intraday()
        self.assertEqual(type(import_data), type(df))
        self.assertIsNotNone(import_data)
class TestGetDataQuote(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        print('called setup')
        self.import_data = get_data_quote()
        
    def test_import_contains_values(self):
        """
        Test that the APIcall obtains values
        """
        self.assertIsNotNone(self.import_data)

    def test_import_contains_price(self):

        keys = list(self.import_data[0])
        self.assertEqual(keys[4], '05. price')        
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
