import yaml
from conf.setting import FILE_PATH
import unittest
from ddt import ddt, file_data

@ddt
class TestDdtYamlRead(unittest.TestCase):
    @file_data(FILE_PATH['yaml'])
    def test_01_login(self,**kwargs):
        print(kwargs)



if __name__ == '__main__':
    unittest.main()
