#Created on 2017/12/21
#@author: meng.xu
#@email: meng.xu@tpv-tech.com

# -*- coding: utf-8 -*-
import time
import sys
import random

class PTAClass:

	TAG = "PTAClass" + ": "
	availableChannelItem = []
	click_interval_time = 2
	wait_time = 10;
	PLAY_LISTS = "Playlists"
	LOCAL_SERVER = "LocalServer"
	REMOTE_SERVER = "RemoteServer"
	NONE_SERVER = "NoneServer"

	def __init__(self, d, deviceSerialNumber):
		self.d = d
		self.deviceSerialNumber = deviceSerialNumber
		print(self.TAG + "PTAClass init")

	def available_channel_item(self, channelGrid):
		channelItem = []
		firstChannelItem = channelGrid.child(className = "android.widget.RelativeLayout", index = 1)
		if firstChannelItem.exists:
			print(self.TAG + "firstChannelItem add")
			channelItem.append(firstChannelItem)
		else:
			print(self.TAG + "not any channel to select, please check")
			sys.exit(1)

		secondChannelItem = channelGrid.child(className = "android.widget.RelativeLayout", index = 2)
		if secondChannelItem.exists:
			print(self.TAG + "secondChannelItem add")
			channelItem.append(secondChannelItem)

		thirdChannelItem = channelGrid.child(className = "android.widget.RelativeLayout", index = 3)
		if thirdChannelItem.exists:
			print(self.TAG + "thirdChannelItem add")
			channelItem.append(thirdChannelItem)

		fourChannelItem = channelGrid.child(className = "android.widget.RelativeLayout", index = 4)
		if fourChannelItem.exists:
			print(self.TAG + "fourChannelItem add")
			channelItem.append(fourChannelItem)

		fiveChannelItem = channelGrid.child(className = "android.widget.RelativeLayout", index = 5)
		if fiveChannelItem.exists:
			print(self.TAG + "fiveChannelItem add")
			channelItem.append(fiveChannelItem)

		sixChannelItem = channelGrid.child(className = "android.widget.RelativeLayout", index = 6)
		if sixChannelItem.exists:
			print(self.TAG + "sixChannelItem add")
			channelItem.append(sixChannelItem)

		sevenChannelItem = channelGrid.child(className = "android.widget.RelativeLayout", index = 7)
		if sevenChannelItem.exists:
			print(self.TAG + "sevenChannelItem add")
			channelItem.append(sevenChannelItem)

		eightChannelItem = channelGrid.child(className = "android.widget.RelativeLayout", index = 8)
		if eightChannelItem.exists:
			print(self.TAG + "eightChannelItem add")
			channelItem.append(eightChannelItem)

		nineChannelItem = channelGrid.child(className = "android.widget.RelativeLayout", index = 9)
		if nineChannelItem.exists:
			print(self.TAG + "nineChannelItem add")
			channelItem.append(nineChannelItem)

		tenChannelItem = channelGrid.child(className = "android.widget.RelativeLayout", index = 10)
		if tenChannelItem.exists:
			print(self.TAG + "tenChannelItem add")
			channelItem.append(tenChannelItem)

		return channelItem


	def pta_watch_tv(self, position):
		try:
			watchTv = self.d(resourceId = "com.tpvision.philipstvapp.debug:id/header_text", text = "Watch TV")
			if watchTv.exists:
				print(self.TAG + "Watch TV => click")
				watchTv.click()
				time.sleep(self.click_interval_time)
				channels = self.d(resourceId = "com.tpvision.philipstvapp.debug:id/header_text", text = "Channels")
				if channels.exists:
					print(self.TAG + "Channels => click")
					channels.click()
					time.sleep(self.click_interval_time)
					channelGrid = self.d(resourceId = "com.tpvision.philipstvapp.debug:id/channel_grid")
					if channelGrid.exists:
						# first time is acquire
						if len(self.availableChannelItem) == 0:
							self.availableChannelItem = self.available_channel_item(channelGrid)
							time.sleep(self.click_interval_time)
							# after acquire, check whether length is 0
							if len(self.availableChannelItem) == 0:
								print(self.TAG + "no channel item available, safe exit python script")
								sys.exit(1)
								availableChannelItemLen = len(self.availableChannelItem)
								print(self.TAG + "availableChannelItemLen: " + str(availableChannelItemLen))
								choiceChannelItem = random.choice(range(availableChannelItemLen))
								channelItem = self.availableChannelItem[choiceChannelItem]
								channelProgramNameItem = channelItem.child(resourceId = "com.tpvision.philipstvapp.debug:id/channel_program_name")
								currentProgramName = ""
								if channelProgramNameItem.exists:
									currentProgramName = channelProgramNameItem.info["text"]
								else:
									print(self.TAG + "[1]not exist, default value")
									currentProgramName = "No info available."
									print(self.TAG + "click programeName watch is: " + currentProgramName)
									channelItem.click()
									time.sleep(self.click_interval_time)
									watch = self.d(resourceId = "com.tpvision.philipstvapp.debug:id/wa_record", text = "Watch")
									if watch.exists:
										print(self.TAG + "Watch => click")
										watch.click()
										time.sleep(self.click_interval_time)
										print(self.TAG + "wait " + str(self.wait_time) + " seconds")
										time.sleep(self.wait_time)
										cxtProgramNameItem = self.d(resourceId = "com.tpvision.philipstvapp.debug:id/broadcast_cxt_program_name", \
																 	 className = "android.widget.TextView")
										cxtProgramName = ""
										if cxtProgramNameItem.exists:
											cxtProgramName = cxtProgramNameItem.info["text"]
										else:
											print(self.TAG + "[2]not exist, default")
											cxtProgramName = "No info available."
											print(self.TAG + "currentProgramName: " + currentProgramName)
											print(self.TAG + "cxtProgramName: " + cxtProgramName)
											if currentProgramName == cxtProgramName:
												print(self.TAG + "UI update success")
											else:
												print(self.TAG + "UI update fail")
												openRight = self.d(resourceId = "com.tpvision.philipstvapp.debug:id/open_right", \
                                                                    className = "android.widget.Button")
												if openRight.exists:
													print(self.TAG + "open right => click")
													openRight.click()
													time.sleep(self.click_interval_time)
													openLeft = self.d(resourceId = "com.tpvision.philipstvapp.debug:id/open_left", \
                                                                       className = "android.widget.Button")
													if openLeft.exists:
														print(self.TAG + "open left => click")
														openLeft.click()
														time.sleep(self.click_interval_time)
														openLeft_again = openLeft
														if openLeft_again.exists:
															print(self.TAG + "open left button => click again")
															openLeft_again.click()
															time.sleep(self.click_interval_time)
															overlayHeader = self.d(resourceId = "com.tpvision.philipstvapp.debug:id/overlay_header", \
                                                                                         text = "Watch TV")
															if overlayHeader.exists:
																print(self.TAG + "back main screen => click")
																overlayHeader.click()
																time.sleep(self.click_interval_time)
															else:
																print(self.TAG + "not return main screen")
														else:
															print(self.TAG + "not find open left again")
												else:
														print(self.TAG + "not find open left")
									else:
										print(self.TAG + "not find => open right")
							else:
								print(self.TAG + "not find => Watch")
						else:
							print(self.TAG + "not find => id/channel_grid")
					else:
						print(self.TAG + "not find => Channels")
				else:
					print(self.TAG + "not find => Watch TV")
		except Exception as e:
			print(self.TAG + str(e))

	def getServername(self, server):
		serverName = ""
		server_linear = server.child(index = 1, className = "android.widget.LinearLayout") 
		if server_linear.exists:
			#print(self.TAG + "find server_linear")
			server_linear_linear = server_linear.child(index = 0, className = "android.widget.LinearLayout")
			if server_linear_linear.exists:
				#print(self.TAG + "find server_linear_linear")
				server_linear_linear_text = server_linear_linear.child(index = 0, \
													resourceId = "com.tpvision.philipstvapp.debug:id/header_text")
				if server_linear_linear_text.exists:
					#print(self.TAG + "find server_linear_linear_text")
					serverName = server_linear_linear_text.info["text"]
				else:
					print(self.TAG + "not find server_linear_linear_text")
			else:
				print(self.TAG + "not find server_linear_linear")
		else:
			print(self.TAG + "not find server_linear")
		return serverName
	
	def pta_media_browser(self):
		try:
			mediaBrowser = self.d(text = "Media Browser", resourceId = "com.tpvision.philipstvapp.debug:id/header_text")
			if mediaBrowser.exists:
				print(self.TAG + "click => Media Browser")
				mediaBrowser.click()
				time.sleep(self.click_interval_time)
				time.sleep(self.click_interval_time)
				left_panel_app_menu = self.d(index = 1, resourceId = "com.tpvision.philipstvapp.debug:id/left_panel_app_menu", \
											  className = "android.widget.ListView")
				if left_panel_app_menu.exists:
					server = left_panel_app_menu.child(className = "android.widget.LinearLayout")
					#server count not include Playlists
					serverCount = server.info["childCount"]
					self.getAllServerName(serverCount, left_panel_app_menu)
					time.sleep(self.click_interval_time)
					print(self.TAG + "find server count: " + str(serverCount))
					if serverCount > 0:
						#click random server
						randomServer = random.choice(range(serverCount + 1))
						selectServer = left_panel_app_menu.child(index = randomServer, className = "android.widget.LinearLayout")	
						serverName = self.getServername(selectServer)
						print(self.TAG + "server name: " + serverName + " => click")				
						selectServer.child(index = 1, className = "android.widget.LinearLayout")\
									.child(index = 0, className = "android.widget.LinearLayout")\
									.child(index = 0, resourceId = "com.tpvision.philipstvapp.debug:id/header_text")\
									.click()	
						serverType = ""
						if self.PLAY_LISTS == serverName:
							serverType = self.NONE_SERVER
						else:
							serverType = self.getServerType(left_panel_app_menu)							
						print(self.TAG + "server type: " + serverType)
						time.sleep(self.click_interval_time)
					else:
						print(self.TAG + "not find any server, please check it")
				else:
					print(self.TAG + "not find left_panel_app_menu")
			else:
				print(self.TAG + "not find => media browser")
		except Exception as e:
			print(self.TAG + str(e))
			
	# get all server list, include playlists		
	def getAllServerName(self, serverCount, server):
		loop = range(serverCount)
		for i in loop:
			ser = server.child(index = i, className = "android.widget.LinearLayout")
			serverName = self.getServername(ser)
			print(self.TAG + "DMS " + str(i) + " name: " + serverName)
		playlists = server.child(index = serverCount, className = "android.widget.LinearLayout")
		print(self.TAG + "Playlists name: " + self.getServername(playlists))
	
	# LocalServer/RemoteServer
	def getServerType(self, appMenuItem):
		menuChildCount = appMenuItem.info["childCount"]	
		print(appMenuItem.info)
		if menuChildCount == 4:
			return self.REMOTE_SERVER
		elif menuChildCount == 3:
			return self.LOCAL_SERVER
		