#coding:utf-8

import requests

server_ip = "localhost"

def TestPlugin():
    print("first-demo")
    url = "http://{}:8000/demo/test".format(server_ip)
    r = requests.get(url)
    print(r.status_code)
    print(r.text)

    print("second-demo")
    url = "http://{}:8000/product/test".format(server_ip)
    r = requests.get(url)
    print(r.status_code)
    print(r.text)

    print("third-demo")
    headers = {"X-Hello":"admin"}
    url = "http://{}:8000/product/test".format(server_ip)
    r = requests.get(url, headers=headers)
    print(r.status_code)
    print(r.text)

if __name__=="__main__":
    TestPlugin()

