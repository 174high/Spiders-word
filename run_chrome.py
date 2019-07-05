#!/usr/bin/python3

import os,subprocess
import _thread
import time

cmd='netstat -ano|findstr 9235'
data=None

try:

    result=subprocess.check_output(cmd, shell=True)
    print(result)
    print("type=",type(result))
    print(result.decode(encoding='utf-8'))
    data=result.decode(encoding='utf-8')

except BaseException:
    print("error")

if data!=None:

    res=data.split()

    print(res)

    for tcp in range(len(res)):

        print(tcp)

    i=0

    while 1:

        i=i+4

        print("i=",i)
        if i<len(res):
            if (res[i] ==0) or (not res[i].isnumeric()) :
                break;
            subprocess.check_output(["taskkill","/pid",res[i],"/f"], shell=True)    
        else:
            break 

def run_chrome( threadName, delay):

    print("continue ....")

    subprocess.call('"C:\Program Files (x86)\Google\Chrome\Application\chrome" --headless --disable-gpu  --remote-debugging-port=9235', shell=True)

    print("continue ....")

def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))


try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( run_chrome, ("Thread-2", 4, ) )
except:
   print ("Error: can't run thread")

while 1:
   pass



#subprocess.call('"C:\Program Files (x86)\Google\Chrome\Application\chrome" --headless --disable-gpu  --remote-debugging-port=9235', shell=True)

#os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome" --headless --disable-gpu --remote-debugging-port=9222 ')


#os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome")


#os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome",'--headless --disable-gpu --remote-debugging-port=9222')

