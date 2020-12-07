# !/usr/bin/env python3

# encoding: utf-8
import requests
import json
import sys

host = "127.0.0.1"
port = 8500

# consul中微服务名称
serviceNames = ""


def get_service():
    url = 'http://' + host + ':' + str(port) + '/v1/agent/services'
    data = requests.get(url).json()
    jsonStr = json.dumps(data)
    print('json ' + jsonStr)
    keys = []
    for k in data:
        serviceName = data[k]['Service']
        if serviceName in serviceNames:
            print(data[k]['Service'])
            print(data[k]['ID'])
            keys.append(k)
    return keys


def del_service(keys):
    url = 'http://' + host + ':' + str(port) + '/v1/agent/service/deregister/'
    for sid in keys:
        requests.put(url + sid)
        print('删除 ' + sid)


# python3 main.py 127.0.0.1 application-yierbao-sweb
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("请输入：python3 ", sys.argv[0], "[ip] [service-name1,service-name2...]")
    else:
        host = sys.argv[1]
        serviceNames = sys.argv[2]
        keys = get_service()
        del_service(keys)
