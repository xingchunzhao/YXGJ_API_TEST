#coding=utf-8
'''
Created on 2020年12月18日

@author: zhaoxc
'''
from YXGJ_API.TestCase import TestLogin, TestHpgl
'''
改文件为TestCase收集文件
'''

from YXGJ_API.TestCase.TestLogin import  YXGJ_Login
from YXGJ_API.TestCase.TestHpgl import  YXGJ_Dhsh
from YXGJ_API.TestCase.TestZmjjtb import YXGJ_Zmjjtb

class YXGJ_API_TestCaseList():
    
    '''
    TestCaselist返回函数
    返回所有的TestCase
    '''
    @staticmethod
    def TestCaseList():
        allTestCaseName = {
            YXGJ_Login.YXGJ_login_TestCase,
            YXGJ_Dhsh.YXGJ_Dhsh_TestCase,
            YXGJ_Zmjjtb.YXGJ_Zmjjtb_TestCase
            }
    
        return allTestCaseName

if __name__ == '__main__':
    test = YXGJ_API_TestCaseList.TestCaseList()
    print test