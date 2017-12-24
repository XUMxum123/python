# -*- coding: UTF-8 -*-

import os
import re
import sys
import time
import string
import subprocess

class ADBClass:

	TAG = "ADBClass" + ": "
	ptalog_path = "\\ptalog\\"
	ptalog_suffix = ".txt"

	def __init__(self):
		print(self.TAG + "ADBClass init")

	def getRootDirectory(self):
		return os.getcwd()

	# current year-month-date-hour-minute-second
	def getCurrentYMDHMS(self):
		return time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())

	def getPtalogStoreFile(self):
		ptalogFile = self.getRootDirectory() + self.ptalog_path + str(self.getCurrentYMDHMS()) \
						+ self.ptalog_suffix
		return ptalogFile

	def executeCommand_adb_devices(self):
		command_adb_devices = "adb devices"
		print(self.TAG + "execute command => " + command_adb_devices)
		try:
				pi = subprocess.Popen(command_adb_devices, shell=True, stdout=subprocess.PIPE)
				return pi.stdout.read()
		except Exception as e:
				print(e)

	def executeCommand_adb_devices_output(self):
		command_adb_devices = "adb devices"
		print(self.TAG + "execute command => " + command_adb_devices)
		try:
				pi = subprocess.check_output(command_adb_devices)
				return pi
		except Exception as e:
				print(e)

	def executeCommand_adb_system_info(self):
		command_adb_system_info = "adb shell cat /system/build.prop"
		print(self.TAG + "execute command => " + command_adb_system_info)
		try:
				pi = subprocess.check_output(command_adb_system_info)
				return pi
		except Exception as e:
				print(e)

	def executeCommand_adb_logcat_c(self):
		command_adb_logcat_c = "adb logcat -c"
		print(self.TAG + "execute command => " + command_adb_logcat_c)
		try:
				pi = subprocess.Popen(command_adb_logcat_c, shell=True, stdout=subprocess.PIPE)
				return pi
		except Exception as e:
				print(e)

	# support single field to filter
	def executeCommand_adb_logcat_s(self, filter):
		command_adb_logcat_s = "adb logcat -s " + filter
		print(self.TAG + "execute command => " + command_adb_logcat_s)
		pi = subprocess.Popen(command_adb_logcat_s, shell=True, stdout=subprocess.PIPE)
		return pi

	# according to time, grab adb log, deviceSerialNumber is 
	# @parameter : deviceSerialNumber, now not use it
	def executeCommand_grab_adb_log_v_time(self, deviceSerialNumber):
		command_grab_adb_log_v_time = "adb logcat -v time>" + self.getPtalogStoreFile()
		print(self.TAG + "execute command => " + command_grab_adb_log_v_time)
		# if many devices, use deviceSerialNumber select device
		# adb -s deviceSerialNumber logcat -v time> + self.getPtalogStoreFile()
		try:
				pi = subprocess.Popen(command_grab_adb_log_v_time, shell=True, stdout=subprocess.PIPE)
				return pi
		except Exception as e:
				print(e)

	def executeCommand_adb_kill_server(self):
		command_adb_kill_server = "adb kill-server"
		print(self.TAG + "execute command => " + command_adb_kill_server)
		try:
				pi = subprocess.Popen(command_adb_kill_server, shell=True, stdout=subprocess.PIPE)
				return pi
		except Exception as e:
				print(e)

	def executeCommand_adb_start_server(self):
		command_adb_start_server = "adb start-server"
		print(self.TAG + "execute command => " + command_adb_start_server)
		try:
				pi = subprocess.Popen(command_adb_start_server, shell=True, stdout=subprocess.PIPE)
				return pi
		except Exception as e:
				print(e)

	def startGrabAdbLog(self):
		deviceSerialNumber = self.getDeviceSerialNumber()
		if deviceSerialNumber == "":
			print(self.TAG + "not find devices, safe exit python script")
			sys.exit(1)
		else:
				print(self.TAG + "deviceSerialNumber: " + deviceSerialNumber)
		# clear adb log cache
		self.executeCommand_adb_logcat_c()
		print(self.TAG + "wait 5 seconds, than start grad adb log")
		time.sleep(5)
		self.executeCommand_grab_adb_log_v_time(deviceSerialNumber)

	def stopGrabAdbLog(self):
		print(self.TAG + "wait 10 seconds, than stop grab adb log")
		time.sleep(10)    
		self.executeCommand_adb_kill_server()  
		print(self.TAG + "wait 5 seconds, than start server")
		time.sleep(5) 
		self.executeCommand_adb_start_server() 
		print(self.TAG + "sleep 5 seconds, than adb devices")
		time.sleep(5) 
		deviceSerialNumber = self.getDeviceSerialNumber()
		if deviceSerialNumber == "":
			print(self.TAG + "not find devices, safe exit python script")
			sys.exit(1)
		else:
			print(self.TAG + "deviceSerialNumber: " + deviceSerialNumber)
		
	# return the last find phone serial number
	def getDeviceSerialNumber(self):
		deviceSerialNumber = ""
		devicesOutput = self.executeCommand_adb_devices_output()
		devicesOutputLen = len(devicesOutput)
		# if not find any device, adb_devices_output length is 29, otherwise more than 29
		if devicesOutputLen <= 29:
			print(self.TAG + "not find any devices: " + str(devicesOutputLen) + " , than safe exit python script")
			return str(deviceSerialNumber)
			sys.exit(1)
		deviceInfo = devicesOutput.split("\r\n")
		len_deviceInfo = len(deviceInfo)
		if deviceInfo[1] == "":
			print(self.TAG + "not find any devices")
			return str(deviceSerialNumber)
		elif deviceInfo[1] != "":
			print(self.TAG + "find devices count: " + str(len_deviceInfo - 3))
			for i in range(1, (len_deviceInfo - 2)):
				dev = deviceInfo[i].split("\t")
				if len(dev) > 0:
					deviceSerialNumber = dev[0]
					print(self.TAG + "device " + str(i) + " serial number: " + str(deviceSerialNumber))
					return str(deviceSerialNumber)
				else:
					print(self.TAG + "deviceInfo " + str(i) + " len is 0")
					return str(deviceSerialNumber)
		else:
			print(self.TAG + "deviceInfo none")
			return str(deviceSerialNumber)

	def connectDevice(self):
		try:  
			deviceInfo = self.executeCommand_adb_devices_output().split("\r\n")  
			if deviceInfo[1] == "":
				return False
			else:
				return True
		except Exception as e:  
			print(self.TAG + "Device Connect Fail: " + e) 

	def getAndroidVersion(self):  
		try:  
				if self.connectDevice():      
						sysInfo = self.executeCommand_adb_system_info()  
						androidVersion = re.findall("version.release=(\d\.\d)*",sysInfo , re.S)[0]  
						return androidVersion  
				else:  
						return "Connect Fail,Please reconnect Device..."  
		except Exception as e:  
				print (self.TAG + "Get Android Version: " + e)

	def getDeviceName(self):    
		try:  
				if self.connectDevice():   
						deviceInfo = subprocess.check_output('adb devices -l')  
						deviceName=re.findall(r'device product:(.*)\smodel',deviceInfo,re.S)[0]  
						return deviceName  
				else:  
						return "Connect Fail,Please reconnect Device..."  
		except Exception as e:  
				print (self.TAG + "Get Device Name: " + e)