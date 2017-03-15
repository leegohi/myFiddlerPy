#encoding:utf-8
import sys,json
filename=sys.argv[1]
with open(filename,"r") as f:
    headers_dic={}
    i=0
    headstr=f.read()
    lines=headstr.split("\n")
    for line in lines[1:-1]:
        if ":" in line:
            nl=line.strip()
            hk,hv=nl.split(":",1)
            headers_dic[hk]=hv
    print headers_dic
    data_dic={}
    for ditem in lines[-1].split("&"):
        k,v=ditem.split("=")
        data_dic[k]=v
    with open("headers.txt","w") as f1:
        f1.write(json.dumps(headers_dic,indent=2))
    with open("data.txt","w") as f1:
        f1.write(json.dumps(data_dic,indent=2))
