#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'

import unittest

class TestMy(unittest.TestCase):

    def setUp(self):
        print('数据库链接成功！')

    def test_key(self):
        print('test_key')
        self.assertEqual(1,1)
        # self.assertEqual(1,2)

    def test_true(self):
        print('test_true')
        self.assertTrue(isinstance({'a':1,'b':8},dict))

    def tearDown(self):
        print('数据库关闭！')

if __name__=='__main__':
    unittest.main()