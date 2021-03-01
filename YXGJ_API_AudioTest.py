#coding=utf-8
'''
Created on 2020年12月17日

@author: zhaoxc
'''
from fileinput import filename
from YXGJ_API import *
from YXGJ_API.TestConfig import YXGJ_ExcelTemplates
import TestCaseList
import AddTestCase
import time
import sys
from TestCase import *
from time import *
# from YXGJ_API.TestCaseList import YXGJ_API_TestCaseList


'''
营销管家后端接口自动化测试
'''



class YXGJ_API_AudioTest():
    
    '''
    调入AddTestCase类执行所有的测试用例
    对所有的Testcase结果进行处理整理成测试报告
    输出test_Report.html
    YXGJ_API_AudioTest List输出report数据
    YXGJ_API_AudioReport生成测试报告
    '''
    @staticmethod
    def YXGJ_API_AudioTestList():
        ##返回reportlist
        allTestCaseResultLists = AddTestCase.YXGJ_API_AddTestCase.YXGJ_API_AddTestCase()
#         print allTestCaseResultLists
        test_Report = []
#         print len(allTestCaseResultLists)

                
        for testCase in range(len(allTestCaseResultLists)):
            report = []
#             print testCase
#             print len(allTestCaseResultLists)
#             print allTestCaseResultLists[testCase]
            testname = allTestCaseResultLists[testCase][0]
            testresult= []
#             testresult = allTestCaseResultLists[testCase][1] 
            testreason = None
            result = allTestCaseResultLists[testCase][1] 
#             print result
#             print len(result)              
            report.append(testname)
            if(result[0] == "True"):
#                 testresult = result[0]
                testreason = "成功" 
                testresult = allTestCaseResultLists[testCase][1] 
                
            else:
#                 print result
                testresult = ['False']
                testreason = str(result[1])    
#                 print testresult 
#                 print testreason
#             for i in range(len(result)):
#                 if(result[0] == "True"):
#                     testresult = result[0]
#                     testreason = "成功" 
#                 else:
#                     testresult = result[0]
#                     testreason = result[1]  
#             print testreason       
            report.append(testresult)
            report.append(testreason)
            test_Report.append(report)
            
#         print test_Report
        return test_Report
     
                
    '''
     生成报告Report
    '''               
    @staticmethod
    def YXGJ_API_AudioReport():
        
        try:
            begin_time = time()
            rep_list = YXGJ_API_AudioTest.YXGJ_API_AudioTestList()
            YXGJ_ExcelTemplates.YXGJ_ExcelTemplates.WriteExcel(rep_list)
            end_time = time()
            run_time = end_time - begin_time
            print("测试完成,用时" + str(run_time) + "s,具体结果请查看测试报告文档!")
        
        except Exception as e:
            print "函数YXGJ_API_AudioReport:"
            print e
        
        
        
if __name__ == '__main__':
    YXGJ_API_AudioTest.YXGJ_API_AudioReport()