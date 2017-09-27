import urllib
import requests
import random
import re
import config
import headerFunc
from optparse import OptionParser
from urllib.parse import urlparse
#存放常见功能

def addOption():#命令行参数获取
    usage = "%prog [-f] [-u] [-p] "
    parser = OptionParser(usage=usage,version="1.0")
    parser.add_option("-f",
                      "--file",
                      dest="filename",
                      help="Choose the url file",
                      type="string"
                      )
    parser.add_option("-u",
                      "--url",
                      dest="url",
                      help="Specify the url",
                      type="string"
                      )
    parser.add_option("-p",
                      "--path",
                      dest="storepath",
                      help="The path where log file stores",
                      type="string"
                      )
    (options,args) = parser.parse_args()
    return (options,args)


def LogData(data):#扫描结果存储
    LogPath = config.LogPath+"/Log.txt"
    f = open(LogPath,"w")
    f.write("Front  Framework:"+data["FrontFramework"])
    f.write("Server Language :"+data["ServerLanguage"])
    f.close()


def urlParse(url):#处理url结构
    if "http://" not in url:
        addResult = "http://" + url
        parseResult = urlparse(str(addResult))
        Result = str("http://" + parseResult.netloc)
    else:
        parseResult = urlparse(str(url))
        Result = str(parseResult.scheme + "://" + parseResult.netloc)
    return Result


def spiderInit(url,timeout):#对url检测
    
    UA = random.choice(config.user_agent_list)  #随机ua
    headers = {'User-Agent': UA}  #构造成一个完整的User-Agent
    (result) = requests.get(url=url,timeout=timeout,headers=headers)
    (responseHeader,content,status_code) = (result.headers,result.content,result.status_code)
    try:
        whatweb_result = headerFunc.headerDetect(url)
        print (whatweb_result)
    except:
        print("whatweb异常")
        pass
    print (type(whatweb_result))


