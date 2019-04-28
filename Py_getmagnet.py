
import pyperclip
import time
import re

key =(r"ed2k://.*\|/",\
    r"(thunder://.+?)",\
    r"magnet:[?]xt=urn:btih:([a-fA-F0-9]{40})",\
    ".*([a-fA-F0-9]{40})",\
    r"magnet:[?]xt=urn:btih:([a-fA-F0-9]{32})",\
    ".*([a-zA-Z2-7]{32})",\
    # "http.+?hash\=([a-zA-Z0-9]{43})",\
    # "http.+?/magnet/detail/hash/([a-fA-F0-9]{40})",\
    )

pyperclip.copy("")
while 1:
    time.sleep(0.5)
    txt=pyperclip.paste() 
    
    if txt!="":
        # print(txt)
        for i in key:
            keyre=re.compile(i,re.I|re.M)
            if keyre.findall(txt):
                mag=keyre.findall(txt)
                # print(isinstance(mag))
                # if type(mag)== 'list' :
                # print(i)
                # print(mag)
                wf = open("tb.txt","a")
                for m in mag:
                    if len(m) == 40 or 32:
                        wf.writelines('magnet:?xt=urn:btih:'+m+ '\n')
                        # print('magnet:?xt=urn:btih:'+m)
                    # elif len(m) == 43:
                    #     wf.writelines('magnet:?xt=urn:btih:'+m[3,42])
                    #     print('magnet:?xt=urn:btih:'+m[3,42])
                    else :
                        wf.writelines(m+ '\n')
                        # print(m)
                

                wf.close()
                pyperclip.copy("")
                break 
 
