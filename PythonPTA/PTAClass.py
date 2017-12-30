#Created on 2017/12/21
#@author: meng.xu
#@email: meng.xu@tpv-tech.com

# -*- coding: utf-8 -*-
import time
import sys
import random

class PTAClass:

	TAG = " PTAClass" + ": "
	availableChannelItem = []
	one_interval_time = 1
	click_interval_time = 2
	wait_time = 10;
	PLAY_LISTS = "Playlists"
	LOCAL_SERVER = "LocalServer"
	REMOTE_SERVER = "RemoteServer"
	NONE_SERVER = "NoneServer"

	def __init__(self, d, deviceSerialNumber):
		self.d = d
		self.deviceSerialNumber = deviceSerialNumber
		print(self.getCurrentTime() + self.TAG + "PTAClass init")

	def available_channel_item(self, channelGrid):
		channelItem = []
		firstChannelItem = channelGrid.child(className = "android.widget.RelativeLayout", index = 1)
		if firstChannelItem.exists:
			print(self.getCurrentTime() + self.TAG + "firstChannelItem add")
			channelItem.append(firstChannelItem)
		else:
			print(self.getCurrentTime() + self.TAG + "not any channel to select, please check")
			sys.exit(1)

		secondChannelItem = channelGrid.child(className = "android.widget.RelativeLayout", index = 2)
		if secondChannelItem.exists:
			print(self.getCurrentTime() + self.TAG + "secondChannelItem add")
			channelItem.append(secondChannelItem)

		thirdChannelItem = channelGrid.child(className = "android.widget.RelativeLayout", index = 3)
		if thirdChannelItem.exists:
			print(self.getCurrentTime() + self.TAG + "thirdChannelItem add")
			channelItem.append(thirdChannelItem)

		fourChannelItem = channelGrid.child(className = "android.widget.RelativeLayout", index = 4)
		if fourChannelItem.exists:
			print(self.getCurrentTime() + self.TAG + "fourChannelItem add")
			channelItem.append(fourChannelItem)

		fiveChannelItem = channelGrid.child(className = "android.widget.RelativeLayout", index = 5)
		if fiveChannelItem.exists:
			print(self.getCurrentTime() + self.TAG + "fiveChannelItem add")
			channelItem.append(fiveChannelItem)

		sixChannelItem = channelGrid.child(className = "android.widget.RelativeLayout", index = 6)
		if sixChannelItem.exists:
			print(self.getCurrentTime() + self.TAG + "sixChannelItem add")
			channelItem.append(sixChannelItem)

		sevenChannelItem = channelGrid.child(className = "android.widget.RelativeLayout", index = 7)
		if sevenChannelItem.exists:
			print(self.getCurrentTime() + self.TAG + "sevenChannelItem add")
			channelItem.append(sevenChannelItem)

		eightChannelItem = channelGrid.child(className = "android.widget.RelativeLayout", index = 8)
		if eightChannelItem.exists:
			print(self.getCurrentTime() + self.TAG + "eightChannelItem add")
			channelItem.append(eightChannelItem)

		nineChannelItem = channelGrid.child(className = "android.widget.RelativeLayout", index = 9)
		if nineChannelItem.exists:
			print(self.getCurrentTime() + self.TAG + "nineChannelItem add")
			channelItem.append(nineChannelItem)

		tenChannelItem = channelGrid.child(className = "android.widget.RelativeLayout", index = 10)
		if tenChannelItem.exists:
			print(self.getCurrentTime() + self.TAG + "tenChannelItem add")
			channelItem.append(tenChannelItem)

		return channelItem


	def pta_watch_tv(self, position):
		try:
			watchTv = self.d(resourceId = "com.tpvision.philipstvapp.debug:id/header_text", text = "Watch TV")
			if watchTv.exists:
				print(self.getCurrentTime() + self.TAG + "Watch TV => click")
				watchTv.click()
				time.sleep(self.click_interval_time)
				channels = self.d(resourceId = "com.tpvision.philipstvapp.debug:id/header_text", text = "Channels")
				if channels.exists:
					print(self.getCurrentTime() + self.TAG + "Channels => click")
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
								print(self.getCurrentTime() + self.TAG + "no channel item available, safe exit python script")
								sys.exit(1)
								availableChannelItemLen = len(self.availableChannelItem)
								print(self.getCurrentTime() + self.TAG + "availableChannelItemLen: " + str(availableChannelItemLen))
								choiceChannelItem = random.choice(range(availableChannelItemLen))
								channelItem = self.availableChannelItem[choiceChannelItem]
								channelProgramNameItem = channelItem.child(resourceId = "com.tpvision.philipstvapp.debug:id/channel_program_name")
								currentProgramName = ""
								if channelProgramNameItem.exists:
									currentProgramName = channelProgramNameItem.info["text"]
								else:
									print(self.getCurrentTime() + self.TAG + "[1]not exist, default value")
									currentProgramName = "No info available."
									print(self.getCurrentTime() + self.TAG + "click programeName watch is: " + currentProgramName)
									channelItem.click()
									time.sleep(self.click_interval_time)
									watch = self.d(resourceId = "com.tpvision.philipstvapp.debug:id/wa_record", text = "Watch")
									if watch.exists:
										print(self.getCurrentTime() + self.TAG + "Watch => click")
										watch.click()
										time.sleep(self.click_interval_time)
										print(self.getCurrentTime() + self.TAG + "wait " + str(self.wait_time) + " seconds")
										time.sleep(self.wait_time)
										cxtProgramNameItem = self.d(resourceId = "com.tpvision.philipstvapp.debug:id/broadcast_cxt_program_name", \
																 	 className = "android.widget.TextView")
										cxtProgramName = ""
										if cxtProgramNameItem.exists:
											cxtProgramName = cxtProgramNameItem.info["text"]
										else:
											print(self.getCurrentTime() + self.TAG + "[2]not exist, default")
											cxtProgramName = "No info available."
											print(self.getCurrentTime() + self.TAG + "currentProgramName: " + currentProgramName)
											print(self.getCurrentTime() + self.TAG + "cxtProgramName: " + cxtProgramName)
											if currentProgramName == cxtProgramName:
												print(self.getCurrentTime() + self.TAG + "UI update success")
											else:
												print(self.getCurrentTime() + self.TAG + "UI update fail")
												openRight = self.d(resourceId = "com.tpvision.philipstvapp.debug:id/open_right", \
                                                                    className = "android.widget.Button")
												if openRight.exists:
													print(self.getCurrentTime() + self.TAG + "open right => click")
													openRight.click()
													time.sleep(self.click_interval_time)
													openLeft = self.d(resourceId = "com.tpvision.philipstvapp.debug:id/open_left", \
                                                                       className = "android.widget.Button")
													if openLeft.exists:
														print(self.getCurrentTime() + self.TAG + "open left => click")
														openLeft.click()
														time.sleep(self.click_interval_time)
														openLeft_again = openLeft
														if openLeft_again.exists:
															print(self.getCurrentTime() + self.TAG + "open left button => click again")
															openLeft_again.click()
															time.sleep(self.click_interval_time)
															overlayHeader = self.d(resourceId = "com.tpvision.philipstvapp.debug:id/overlay_header", \
                                                                                         text = "Watch TV")
															if overlayHeader.exists:
																print(self.getCurrentTime() + self.TAG + "back main screen => click")
																overlayHeader.click()
																time.sleep(self.click_interval_time)
															else:
																print(self.getCurrentTime() + self.TAG + "not return main screen")
														else:
															print(self.getCurrentTime() + self.TAG + "not find open left again")
												else:
														print(self.getCurrentTime() + self.TAG + "not find open left")
									else:
										print(self.getCurrentTime() + self.TAG + "not find => open right")
							else:
								print(self.getCurrentTime() + self.TAG + "not find => Watch")
						else:
							print(self.getCurrentTime() + self.TAG + "not find => id/channel_grid")
					else:
						print(self.getCurrentTime() + self.TAG + "not find => Channels")
				else:
					print(self.getCurrentTime() + self.TAG + "not find => Watch TV")
		except Exception as e:
			print(self.getCurrentTime() + self.TAG + str(e))

	def getServername(self, server):
		serverName = ""
		server_linear = server.child(index = 1, className = "android.widget.LinearLayout") 
		if server_linear.exists:
			#print(self.getCurrentTime() + self.TAG + "find server_linear")
			server_linear_linear = server_linear.child(index = 0, className = "android.widget.LinearLayout")
			if server_linear_linear.exists:
				#print(self.getCurrentTime() + self.TAG + "find server_linear_linear")
				server_linear_linear_text = server_linear_linear.child(index = 0, \
													resourceId = "com.tpvision.philipstvapp.debug:id/header_text")
				if server_linear_linear_text.exists:
					#print(self.getCurrentTime() + self.TAG + "find server_linear_linear_text")
					serverName = server_linear_linear_text.info["text"]
				else:
					print(self.getCurrentTime() + self.TAG + "not find server_linear_linear_text")
			else:
				print(self.getCurrentTime() + self.TAG + "not find server_linear_linear")
		else:
			print(self.getCurrentTime() + self.TAG + "not find server_linear")
		return serverName
	
	def pta_media_browser(self):
		try:
			mediaBrowser = self.d(text = "Media Browser", resourceId = "com.tpvision.philipstvapp.debug:id/header_text")
			if mediaBrowser.exists:
				print(self.getCurrentTime() + self.TAG + "click => Media Browser")
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
					print(self.getCurrentTime() + self.TAG + "find server count: " + str(serverCount))
					if serverCount > 0:
						#click random server
						lastItem = left_panel_app_menu.child(index = (serverCount - 1), className = "android.widget.LinearLayout")
						lastItemServerName = self.getServername(lastItem)
						print(self.getCurrentTime() + self.TAG + "lastItemServerName: " + lastItemServerName)
						if self.PLAY_LISTS == lastItemServerName:
							randomServerIndex = random.choice(range(serverCount))
						else:
							randomServerIndex = random.choice(range(serverCount + 1))
						print(self.getCurrentTime() + self.TAG + "randomServerIndex: " + str(randomServerIndex))
						# customer randomServerIndex = 0, click first server, local server
						randomServerIndex = 0
						selectServer = left_panel_app_menu.child(index = randomServerIndex, className = "android.widget.LinearLayout")	
						serverName = self.getServername(selectServer)
						print(self.getCurrentTime() + self.TAG + "server name: " + serverName + " => click")				
						self.clickItem(selectServer)	
						serverType = ""
						if self.PLAY_LISTS == serverName:
							serverType = self.NONE_SERVER
						else:
							serverType = self.getServerType(left_panel_app_menu)							
						print(self.getCurrentTime() + self.TAG + "server type: " + serverType)
						time.sleep(self.click_interval_time)
						time.sleep(self.click_interval_time)
						firstItem = left_panel_app_menu.child(index = 0, className = "android.widget.LinearLayout")
						if firstItem.exists:
							musicName = self.getServername(firstItem)
							if "Music" == musicName:
								print(self.getCurrentTime() + self.TAG + "click => " + musicName)
								self.clickItem(firstItem)
								time.sleep(self.click_interval_time)
								time.sleep(self.click_interval_time)
								fourItem = left_panel_app_menu.child(index = 3, className = "android.widget.LinearLayout")
								allMusicName = self.getServername(fourItem)
								if "All Music" == allMusicName:
									print(self.getCurrentTime() + self.TAG + "click => " + allMusicName)
									self.clickItem(fourItem)
									time.sleep(self.click_interval_time)
									time.sleep(self.click_interval_time)
									main_container = self.d(index = 0, resourceId = "com.tpvision.philipstvapp.debug:id/main_container", \
											    	        className = "android.widget.RelativeLayout")\
														 .child(index = 0, className = "android.widget.RelativeLayout")
									if main_container.exists:
										content_list = main_container.child(index = 2, resourceId = "com.tpvision.philipstvapp.debug:id/content_list", \
															                className = "android.widget.ListView")
										if content_list.exists:
											#content_list.scroll.vert.toEnd(steps=100)
											scrollIndex = 28
											print(self.getCurrentTime() + self.TAG + "scroll start")
											self.scrollToIndex(scrollIndex, content_list)
											print(self.getCurrentTime() + self.TAG + "scroll end")
											time.sleep(self.click_interval_time)
											musicItem = content_list.child(text = str(scrollIndex), resourceId = "com.tpvision.philipstvapp.debug:id/menu_item_position", \
					               										className = "android.widget.TextView") \
				           					          			.right(resourceId = "com.tpvision.philipstvapp.debug:id/menu_item_header_text", \
					               		  			   					className = "android.widget.TextView")
											musicItemName = musicItem.info["text"]								
											print(self.getCurrentTime() + self.TAG + "click => music name: " + musicItemName)
											musicItem.click()
											time.sleep(self.click_interval_time)
											print(self.getCurrentTime() + self.TAG + "start the music play")
											local_controls = self.d(resourceId = "com.tpvision.philipstvapp.debug:id/local_controls", \
															        className = "android.widget.LinearLayout")
											if local_controls.exists:											
												local_cc = local_controls.child(index = 0, resourceId = "com.tpvision.philipstvapp.debug:id/local_cc", \
															                    className = "android.widget.AdapterView")
												print(self.getCurrentTime() + self.TAG + "scroll start to Next button")
												local_cc.scroll.horiz.to(text = "Next", resourceId = "com.tpvision.philipstvapp.debug:id/right_cc_name", \
																		 className = "android.widget.TextView")
												print(self.getCurrentTime() + self.TAG + "scroll end to Next button")
												time.sleep(self.one_interval_time)
												print(self.getCurrentTime() + self.TAG + "scroll start to Pause button")
												local_cc.scroll.horiz.to(text = "Pause", resourceId = "com.tpvision.philipstvapp.debug:id/right_cc_name", \
																		 className = "android.widget.TextView")
												print(self.getCurrentTime() + self.TAG + "scroll end to Pause button")
												time.sleep(self.one_interval_time)
												pauseButton = local_cc.child(text = "Pause", resourceId = "com.tpvision.philipstvapp.debug:id/right_cc_name", \
																		 	 className = "android.widget.TextView")\
																	  .up(resourceId = "com.tpvision.philipstvapp.debug:id/right_cc_list")
												print(self.getCurrentTime() + self.TAG + "stop the music play")
												pauseButton.click()
												time.sleep(self.click_interval_time)
												main_panel_background_view = self.d(resourceId = "com.tpvision.philipstvapp.debug:id/main_panel_background_view", \
															                        className = "android.view.View")
												if main_panel_background_view.exists:
													print(self.getCurrentTime() + self.TAG + "back the all music list")
													main_panel_background_view.click()
													time.sleep(self.click_interval_time)
													open_left = self.d(resourceId = "com.tpvision.philipstvapp.debug:id/open_left", \
															           className = "android.widget.Button")
													if open_left.exists:
														print(self.getCurrentTime() + self.TAG + "back the music menu")
														open_left.click()
														time.sleep(self.click_interval_time)
														left_frame = self.d(index = 0, resourceId = "com.tpvision.philipstvapp.debug:id/left_frame", \
															               className = "android.widget.RelativeLayout")
														if left_frame.exists:
															overlay_header_container = left_frame.child(resourceId = "com.tpvision.philipstvapp.debug:id/overlay_header_container", \
															                                            className = "android.widget.LinearLayout")
															if overlay_header_container.exists:
																overlay_header = overlay_header_container.child(resourceId = "com.tpvision.philipstvapp.debug:id/overlay_header", \
															                                                    className = "android.widget.TextView")
																if overlay_header.exists:
																	print(self.getCurrentTime() + self.TAG + "back the music/photos/video menu")
																	overlay_header.click()
																	time.sleep(self.click_interval_time)
																	print(self.getCurrentTime() + self.TAG + "back the dms menu")
																	overlay_header.click()
																	time.sleep(self.click_interval_time)
																	print(self.getCurrentTime() + self.TAG + "back the main menu")
																	overlay_header.click()
																	time.sleep(self.click_interval_time)
																else:
																	print(self.getCurrentTime() + self.TAG + "not find overlay_header")
															else:
																print(self.getCurrentTime() + self.TAG + "not find overlay_header_container")
														else:
															print(self.getCurrentTime() + self.TAG + "not find left_frame")
													else:
														print(self.getCurrentTime() + self.TAG + "not find open_left")
												else:
													print(self.getCurrentTime() + self.TAG + "not find main_panel_background_view")
											else:
												print(self.getCurrentTime() + self.TAG + "not find local_controls")
										else:
											print(self.getCurrentTime() + self.TAG + "not find content_list")
									else:
										print(self.getCurrentTime() + self.TAG + "not find main_container")
									
								else:
									print(self.getCurrentTime() + self.TAG + "not match all music item")
							else:
								print(self.getCurrentTime() + self.TAG + "not match music item")
						else:
							print(self.getCurrentTime() + self.TAG + "not find firstItem")
					else:
						print(self.getCurrentTime() + self.TAG + "not find any server, please check it")
				else:
					print(self.getCurrentTime() + self.TAG + "not find left_panel_app_menu")
			else:
				print(self.getCurrentTime() + self.TAG + "not find => media browser")
		except Exception as e:
			print(self.getCurrentTime() + self.TAG + str(e))
			
	# get all server list, include playlists		
	def getAllServerName(self, serverCount, server):
		loop = range(serverCount)
		serverName = ""
		for i in loop:
			ser = server.child(index = i, className = "android.widget.LinearLayout")
			serverName = self.getServername(ser)
			if self.PLAY_LISTS == serverName:
				print(self.getCurrentTime() + self.TAG + "[1]the last item, Playlists name: "  + serverName)
			else:
				print(self.getCurrentTime() + self.TAG + "DMS " + str(i) + " name: " + serverName)
		if self.PLAY_LISTS == serverName:
			print(self.getCurrentTime() + self.TAG + "last item Playlists name had output")
		else:
			playlists = server.child(index = serverCount, className = "android.widget.LinearLayout")
			playlistsName = self.getServername(playlists)
			print(self.getCurrentTime() + self.TAG + "[2]the last item, Playlists name: " + playlistsName)
			
	# LocalServer/RemoteServer
	# this judge maybe have some error, need further check it
	def getServerType(self, appMenuItem):
		menuChildCount = appMenuItem.info["childCount"]	
		if menuChildCount >= 4:
			return self.REMOTE_SERVER
		elif menuChildCount == 3:
			return self.LOCAL_SERVER
		
	def clickItem(self, item):
		item.child(index = 1, className = "android.widget.LinearLayout")\
			.child(index = 0, className = "android.widget.LinearLayout")\
			.child(index = 0, resourceId = "com.tpvision.philipstvapp.debug:id/header_text")\
			.click()
			
	def clickListItem(self, index, listItem):
		listItem.child(text = str(index), resourceId = "com.tpvision.philipstvapp.debug:id/menu_item_position", \
					   className = "android.widget.TextView") \
				.right(resourceId = "com.tpvision.philipstvapp.debug:id/menu_item_header_text", \
					   className = "android.widget.TextView")\
				.click()
			
	def scrollToIndex(self, index, listItem):
		print(self.getCurrentTime() + self.TAG + "scroll to index: " + str(index))
		listItem.scroll.vert.to(text = str(index), resourceId = "com.tpvision.philipstvapp.debug:id/menu_item_position", \
						    className = "android.widget.TextView")
		
	def getListItemName(self, index, listItem):	
		musicName = listItem.child(text = str(index), resourceId = "com.tpvision.philipstvapp.debug:id/menu_item_position", \
					               className = "android.widget.TextView") \
				            .right(resourceId = "com.tpvision.philipstvapp.debug:id/menu_item_header_text", \
					               className = "android.widget.TextView")\
				            .info["text"]
		return musicName
	
	def getCurrentTime(self):
		ct = time.time()
		local_time = time.localtime(ct)
		data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
		data_secs = (ct - long(ct)) * 1000
		time_stamp = "%s.%03d" % (data_head, data_secs)
		return time_stamp
		
		