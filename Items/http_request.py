#!/usr/bin/env python
#-*-coding:utf-8-*-
#--author:amy
#接口测试第一阶段作业
#1.根据提供的注册登录接口，完成注册登录接口的请求，至少每个接口有5条用例，每个接口至少有一条正向用例
#2.要求如下：1）http请求类，（可以根据传递的method-get/post完成不同的请求），要求有返回值
#2）测试用例的数据存储在excel中，编写一个从excel中读取的测试类，包含的函数能够读取测试数据，并能够写回测试结果，要求
#有返回值，3）新建一个run.py文件在这里面完成excel数据的读取以及完成用例的执行并写回测试结果到excel里，
# 至此完成接口自动化测试第一步
import requests
class HttpRequest:
    '''该类完成http的get/post的请求，并返回结果'''
    def http_quest(self,method,url,param):
        '''根据请求方法来决定发起get or post请求
        method：get post的请求方式
        url：发送请求的接口地址
        param：随接口发送的请求参数以字典的格式传递
        rtype：有返回值，返回结果是响应报文
        '''
        if method.upper()=='GET':
            try:
             resp=requests.get(url,params=param)
            except Exception as e:
                print('get请求出错了:{}'.format(e))
        elif method.upper()=='POST':
            try:
             resp=requests.post(url,data=param)
            except Exception as e:
                print('post请求出错了:{}'.format(e))
        else:
            print('不支持该种方式')
            resp=None
        return resp.json()
if __name__ == '__main__':
    url='http://47.107.168.87:8080/futureloan/mvc/api/member/register'
    param={'mobilephone':'13675186891','pwd':'123456','regname':'lemon'}
    method='post'
    resp=HttpRequest().http_quest(method,url,param)#HttpRequest()实例化参数
    print(resp)
    # print(resp.headers)
