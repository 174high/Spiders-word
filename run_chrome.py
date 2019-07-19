import os,subprocess
import _thread
import time


def stop_chrome():

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
                if( res[i].isnumeric() & (res[i] !=0 ) ):
                    subprocess.check_output(["taskkill","/pid",res[i],"/f"], shell=True)    
            else:
                break 
            i=i+1

def run_cmd( threadName, delay):

    subprocess.call('"C:\Program Files (x86)\Google\Chrome\Application\chrome" --headless --disable-gpu  --remote-debugging-port=9235', shell=True)

def run_chrome():

    try:
        _thread.start_new_thread(run_cmd,("Thread-2", 4, ) )
    except:
        print ("Error: can't run thread")
    
    print("continue ....")

if __name__ == "__main__":

    stop_chrome()
#    run_chrome()    


#    while 1:
#        pass




