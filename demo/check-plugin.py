#coding:utf-8                                                                                                                                                                                

import sys 
import json
import requests

server_ip = "localhost"

def GetPlugins(plugin):
    url = "http://{}:8001".format(server_ip)
    r = requests.get(url)
    if r.status_code != 200:
        print(r.status_code, r.text)
        return
    response = json.loads(r.text)
    plugins = response.get("plugins",{}).get("available_on_server",{}).keys()
    print("{}".format(plugins))
    print("{} in plugins:{}".format(plugin, plugin in plugins))
    print("GetPlugings:{}".format(len(plugins)))

if __name__=="__main__":
    plugin = "demo"
    if len(sys.argv) > 1:
        plugin = sys.argv[1]
    GetPlugins(plugin)
