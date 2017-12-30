# -*- coding: UTF-8 -*-

import os
import sys
import time

class PythonLogClass:
    
    TAG = " PythonLogClass" + ": "
    pythonlog_path = "\\pythonLog\\"
    pythonlog_suffix = ".txt"
    
    def __init__(self, fileName):
        self.fileName = fileName
        self.sys_stdout = sys.stdout
        print(self.getCurrentTime() + self.TAG + "PythonLogClass init")
     
    def getCurrentTime(self):
        ct = time.time()
        local_time = time.localtime(ct)
        data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
        data_secs = (ct - long(ct)) * 1000
        time_stamp = "%s.%03d" % (data_head, data_secs)
        return time_stamp 
      
    def getRootDirectory(self):
        return os.getcwd() 
    
    def getPythonlogStoreFile(self):
        pythonlogFile = self.getRootDirectory() + self.pythonlog_path + str(self.fileName) \
                        + self.pythonlog_suffix
        return pythonlogFile
        
    def startGrabPythonLog(self):
        pythonlogFilePath = self.getPythonlogStoreFile()
        print(self.getCurrentTime() + self.TAG + "start grab python log file: " + pythonlogFilePath)
        fileOpenWrite = open(pythonlogFilePath, "w")
        sys.stdout = fileOpenWrite
        self.f = fileOpenWrite
        time.sleep(2)
        print(self.getCurrentTime() + self.TAG + "python log store file: " + pythonlogFilePath)
        
    def stopGrabPythonLog(self): 
        time.sleep(2)
        sys.stdout = self.sys_stdout
        self.f.close()  
        print(self.getCurrentTime() + self.TAG + "stop grab python log file: " + self.getPythonlogStoreFile())
        
        
