#encoding:utf-8
import sys
filename="RawFile.htm"
from urllib import  unquote,splitquery
import json
with open(filename,"r") as f:
    req=f.readlines()
    print req
    head={}
    data={}
    line1=req[0]
    if "POST" in line1:
        line1=req[-1]
        param=unquote(line1.strip())
        print param
        data=dict(map(lambda i:i.split("=",1),param.split("&")))
    
    else:
        qstr=splitquery(line1.split(" ")[1])[1]
        if qstr:
            param=unquote(qstr)
            data=dict(map(lambda i:i.split("=",1) if "=" in i else [i,""],param.split("&")))
        
    with open(filename,"a") as f1:
        f1.write("\n")
        f1.write(json.dumps(data,indent=1))
        f1.write("\n")
    for line in req[1:]:
        if  line.startswith("Cookie"):
            continue
        if  line.startswith("Content-Length"):
            continue 
        if  line.startswith("Connection"):
            continue    
        if  not line.strip():
            break
        temp=line.strip().replace(" ","").split(":",1)
        print temp
        head[temp[0]]=temp[1]
        
    with open(filename,"a") as f2:
        f2.write(json.dumps(head,indent=1))
