import unittest
from nowstagram import app

class NowstagramTest(unittest.TestCase):
    def setUp(self):
        print 'setup'
    def setUpClass(cls):
        print 'setupclass'
