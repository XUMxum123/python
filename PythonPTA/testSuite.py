#Created on 2017/12/21
#@author: meng.xu
#@email: meng.xu@tpv-tech.com

# -*- coding: utf-8 -*-
from uiautomator import device as d
from PTAClass import *
from ADBClass import *
import unittest
import string
import subprocess
import random
import time
import sys

TAG = "testSuite" + ": "
loopLength = 3

print(TAG + "********************************start*********************************")



adbClass = ADBClass()
deviceSerialNumber = adbClass.getDeviceSerialNumber()
if deviceSerialNumber == "":
        sys.exit(1)
ptaClass = PTAClass(d, deviceSerialNumber)

ptaClass.pta_media_browser()

print(TAG + "safe exit python script")
sys.exit(1)

adbClass.startGrabAdbLog()
print(TAG + "<===...... process is start ......===>")
loopRange = range(loopLength)
for i in loopRange:
        if i == 0:
                print(TAG + "first time sleep 5 seconds")
                print(TAG + str(i + 1) + " times execute")
                time.sleep(5)
                #sys.stdout.flush()
                ptaClass.pta_watch_tv(str(i + 1))  
        else: 
                print(TAG + "from second time, every execute should be wait 10 seconds")
                #sys.stdout.flush()
                time.sleep(10)     
                print(TAG + str(i + 1) + " times execute")
                ptaClass.pta_watch_tv(str(i + 1))
print(TAG + "<===...... process is stop ......===>") 
adbClass.stopGrabAdbLog()


print(TAG + "*********************************end**********************************")
