website_list=['facebook.com','www.facebook.com']
from datetime import datetime as dt
import time
while(True):
    if(dt(dt.now().year,dt.now().month,dt.now().day,10)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,13)):
        print('study time')
        with open('C:\\Users\\sabyasachi\\Desktop\\Python\\WebsiteBlocker\\hosts','r+') as hostFile:
            hostContent= hostFile.read()
            for website in website_list:
                if(website in hostContent):
                    pass
                else:
                    hostFile.write('\n'+'127.0.0.1'+' '+website+'\n')
    else:
        with open('C:\\Users\\sabyasachi\\Desktop\\Python\\WebsiteBlocker\\hosts','r+') as hostFile:
            print('enjoy time')
            hostContent= hostFile.readlines()
            hostFile.seek(0)
            for hostLine in hostContent:
                if not any(websiteLine in hostLine for websiteLine in website_list):
                    hostFile.write(hostLine)
            hostFile.truncate()
    time.sleep(5)
