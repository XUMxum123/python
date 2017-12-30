#Created on 2017/12/21
#@author: meng.xu
#@email: meng.xu@tpv-tech.com

# -*- coding: utf-8 -*-
from uiautomator import device as d
from PTAClass import *
from ADBClass import *
from PythonLogClass import *
import unittest
import string
import subprocess
import random
import time
import sys

TAG = " testSuite" + ": "
reload(sys)
sys.setdefaultencoding("utf-8") 
def getCurrentTime():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - long(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    return time_stamp

def getCurrentYMDHMS():
        return time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    
loopLength = 3
fileName = getCurrentYMDHMS()

print(getCurrentTime() + TAG + "***start***")

# start instance PythonLogClass/ADBClass/PTAClass
pythonLogClass = PythonLogClass(fileName)
adbClass = ADBClass(fileName)
deviceSerialNumber = adbClass.getDeviceSerialNumber()
if deviceSerialNumber == "":
        sys.exit(1)
ptaClass = PTAClass(d, deviceSerialNumber)
# end instance

###############################################################################

adbClass.startGrabAdbLog()
pythonLogClass.startGrabPythonLog()

loopRange = range(loopLength)
for i in loopRange:
    print(getCurrentTime() + TAG + "execute times: " + str(i + 1))
    if i == 0:
        print(getCurrentTime() + TAG + "first time sleep 5 seconds")
        time.sleep(5)
        ptaClass.pta_media_browser()
    else:
        print(getCurrentTime() + TAG + "from second time, every execute should be wait 10 seconds")
        time.sleep(10)
        ptaClass.pta_media_browser()

pythonLogClass.stopGrabPythonLog()
adbClass.stopGrabAdbLog()

print(getCurrentTime() + TAG + "safe exit python script")
sys.exit(1)

###############################################################################

adbClass.startGrabAdbLog()
print(getCurrentTime() + TAG + "<===...... process is start ......===>")
loopRange = range(loopLength)
for i in loopRange:
        if i == 0:
                print(getCurrentTime() + TAG + "first time sleep 5 seconds")
                print(getCurrentTime() + TAG + str(i + 1) + " times execute")
                time.sleep(5)
                #sys.stdout.flush()
                ptaClass.pta_watch_tv(str(i + 1))  
        else: 
                print(getCurrentTime() + TAG + "from second time, every execute should be wait 10 seconds")
                #sys.stdout.flush()
                time.sleep(10)     
                print(getCurrentTime() + TAG + str(i + 1) + " times execute")
                ptaClass.pta_watch_tv(str(i + 1))
print(getCurrentTime() + TAG + "<===...... process is stop ......===>") 
adbClass.stopGrabAdbLog()

print(getCurrentTime() + TAG + "***end***")
