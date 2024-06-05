import unittest
from unittest.mock import MagicMock, patch

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from data_reader import DataReader

class TestDataReader(unittest.TestCase):
    def test_init(self):
        dr = DataReader(None,"someip.json")
        self.assertEqual(dr.data,0)
        self.assertEqual(dr.ip,"127.0.0.1")
        self.assertEqual(dr.port,10101)
    def test_prepere_lookup_table(self):
        dr = DataReader(None,"someip.json")
        data = {(515, 32769): 'PC_APP/servoStatusEvent',
                (514, 32769): 'PC_APP/newTempEvent_1'}
        self.assertEqual(dr.lookup_table, data)