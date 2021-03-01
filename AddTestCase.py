#coding=utf-8
'''
Created on 2020年12月18日

@author: zhaoxc
'''
import TestCaseList
import re
from _mysql import result

'''
用了执行测试用例和生成测试报告
'''

class YXGJ_API_AddTestCase():
    '''
    找到对应case方法,执行
    dir()内置函数获取方法名
    b = getattr()内置函数获取方法属性
    b()执行方法,等到返回值
    '''
    @staticmethod
    def DO_TestCase(test_classname):

        #获取类下面的所有方法dir(test_classname)
#         print dir(test_classname)
        allMethod = dir(test_classname)
#         print type(allMethod)
        test = r'test_'
        t = test_classname()
        method_list = []
        method = []

        for i in range(len(allMethod)):

            if(re.match(test, allMethod[i])):
                 method.append(allMethod[i])

                 b = getattr(t, allMethod[i],None)
#                  print type(b)
#                  b = getattr(t, m,None)
                 flags = b()
#                  print b
#                  print flags
 
                 method.append(flags)
#                  print method 
#                  print len(result)  
                 method_list.append(method)
                 method = []
#                  print flags
#         print "method_list"
#         print method_list
#         print len(method_list)
        #返回所有的接口名称
        return method_list

    
    '''
    获取TestCaseList文件下的类名
    调用DO_TestCase执行测试用例
    返回所有的测试用例结果result_list
    '''
    @staticmethod
    def YXGJ_API_AddTestCase():
        tests = TestCaseList.YXGJ_API_TestCaseList.TestCaseList()
#         print tests
#         print tests
        result_list = []
        for test_classname in tests:
#         print type(test)
           result =  YXGJ_API_AddTestCase.DO_TestCase(test_classname)
#            print result
#            result_list.append(result)
           result_list.extend(result)
#         print "result_list"
#         print result_list
#         print len(result_list)
#         print result_list[0]
#         print result_list[1]
#         print result_list[2]
        return result_list

                
if __name__ == '__main__':
    YXGJ_API_AddTestCase.YXGJ_API_AddTestCase()
