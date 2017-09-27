import requests
# import sys
import subprocess



def headerDetect(url):
    result = []
    status,result = subprocess.getstatusoutput("ruby /Users/lichengyu/pentest/WhatWeb-master/whatweb %s"%url)
    # print(result)
    return result