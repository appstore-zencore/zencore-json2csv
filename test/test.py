import os
import unittest

class Test(unittest.TestCase):
    def test01(self):
        os.system("json2csv -f t1.json")

    def test02(self):
        os.system("json2csv -f t2.json -k f1,f2,f3")

    def test03(self):
        os.system("json2csv -f t3.json -p data.list")
