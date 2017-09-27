#coding:utf-8
from urllib.parse import urlparse
import requests
import sys
from optparse import OptionParser
import os
import commonFunc
import config
import hack



if __name__ == "__main__":
    #获取参数，参数列表如下：
    #filename  url存放文件
    #url       指定url
    #storepath log日志存放文件夹
    # for i in sys.argv:
    #     if i !="-h" and i!= "-f" and i!="-u" and i!="main.py":
    #         sys.argv = ["main.py","-h"]
    #         #提示用法
    #     else:
    #         pass
    (options , args ) = commonFunc.addOption()


    #检测log文件目录是否存在，若不存在，则创建
    if(os.path.exists(str(options.storepath))):
        config.LogPath = options.storepath
    else:
        os.mkdir(str(options.storepath))
        config.LogPath = options.storepath

    baseUrl = []


    #处理指定的url，若未指定，则读取url文件中的url
    #ps:处理方法仍有瑕疵
    if(options.url):
        Result = commonFunc.urlParse(options.url)
        baseUrl.append(Result)
    else:
        f = open(str(options.filename))
        for url in f:
            Result = commonFunc.urlParse(options.url)
            baseUrl.append(url)
    for url in baseUrl:

        #针对url进行扫描
        commonFunc.spiderInit(url,config.timeout)
