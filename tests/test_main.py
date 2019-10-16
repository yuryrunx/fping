# -*- coding: utf-8 -*-
import os
import unittest

import sys
sys.path.append("..")
from fping import FPing


class TestFPing(unittest.TestCase):

    def test_run(self):
        """ ###### Test of hosts. [tests_host] must be compare with [result_host] ###### """
        fp = FPing()
        tests_hosts = ['127.0.0.1', '11.0.0.1']
        result_host = (['127.0.0.1'], ['11.0.0.1'])
        self.assertEqual(result_host, fp.run(tests_hosts))


if __name__ == '__main__':
    """ python test_main.py -v """
    unittest.main()



