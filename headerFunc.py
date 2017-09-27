import requests





def headerDetect(header):
    result = []
    if header["Server"]:
        result.append(header["Server"])
    if header["X-Powered-By"]:
        result.append(header["X-Powered-By"])
    print(result)
    return result