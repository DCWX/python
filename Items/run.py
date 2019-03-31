#!/usr/bin/env python
#-*-coding:utf-8-*-
#--author:amy
from Items.do_excel import DoExcel
from Items.http_request import HttpRequest#---读取数据所在的模块
#完成用例的测试
#1.读取到数据
test_data = DoExcel('test_api.xlsx', 'test_case').read_data()
#2.执行测试--根据key取值
# 'Params': "{'mobilephone':'13675186891','pwd':'123456'}",
# 'ExpectedResult': "{'staus':'1','code':'1001','data':'None',msg':'成功'}"
for case in test_data:
    method=case['Method']
    url=case['Url']
    param=eval(case['Params'])
    #发起测试
    print('---正在测试{}模块里的第{}条测试用例:{}'.format(case['Module'],case['CaseId'],case['Title']))
    resp=HttpRequest().http_quest(method,url,param)
    print('实际测试结果:{}'.format(resp))#http发起请求拿到实际返回值,用json方式转成字典
    # print(type(resp))
    # print(case['ExpectedResult'])
    # 我的预期结果
    expect=eval(case['ExpectedResult'])
    estatus=expect["status"]
    ecode=expect["code"]
    emsg=expect["msg"]
    # 系统的结果
    rstatus=resp["status"]
    rcode=resp["code"]
    rmsg=resp["msg"]
    #对比预期结果和实际结果
    if estatus==rstatus and ecode==rcode and emsg==rmsg:
        TestResult='Pass'
        print("实际结果{}与预期结果{}一致".format(resp, expect))
    else:
        TestResult='Failed'
        print("实际结果{}与预期结果{}不一致".format(resp,expect))
    print('该条用例的测试结果:{}'.format(TestResult))

    #需要写回实际结果/测试结论
    t=DoExcel('test_api.xlsx', 'test_case')
    t.write_back(case['CaseId']+1,8,str(resp))#excel里只能写入字符串，不能用json格式
    t.write_back(case['CaseId']+1,9,TestResult)


