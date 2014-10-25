# -*- coding: utf-8 -*-

"""

	No Choice tasks...

"""

import os, sys
import pygame
import csv
from random import randint, choice, sample, shuffle
from time import time

from kelpy.CommandableImageSprite import *
from kelpy.Miscellaneous import *
from kelpy.DisplayQueue import *
from kelpy.OrderedUpdates import *
from kelpy.EventHandler import *
from scenes import display_naming_scene

IMAGE_SCALE = 0.15
QUAD_IMAGE_SCALE = .1
OCTUPLE_OFFSET = 115
HOFFSET = 100
VOFFSET = 100
MAX_DISPLAY_TIME = 3.0
##############################################
## Set up pygame

screen, spot = initialize_kelpy(fullscreen=True)

OFF_LEFT = spot.west
background_color = (140, 140, 140) # 90 # 190
CLICKED_TIMES = 6





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Run a single trial
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	

def display_wait_scene():
	transparent_button = os.path.dirname( __file__ )+"stimuli/transparent.png"
	img = CommandableImageSprite( screen, (0,0), transparent_button, scale=1.0)
	
	## set the image locations
	## Images here are commandable sprites, so we can tell them what to do using Q below
	
	
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# Set up the updates, etc. 
	
	# A queue of animation operations
	Q = DisplayQueue()

	#Q.append(obj='sound', file=(target_audio1[targetidx]) )
	# Draw a single animation in if you want!
	

	# What order do we draw sprites and things in?
	dos = OrderedUpdates(img) # Draw and update in this order
	
	#play_sound(kstimulus("sounds/good_job.wav"))  ## This should be changed to play the proper intro sound for the character. right now it just, quite annoyingly, says "Good job!"
	## The standard event loop in kelpy -- this loops infinitely to process interactions
	## and throws events depending on what the user does
	finished = False
	

	for event in kelpy_standard_event_loop(screen, Q, dos):
		
		# if time()-start_time > MAX_DISPLAY_TIME:
		# 	pass

		# If the event is a click:
		if is_click(event):
			if finished:
				break
			# check if each of our images was clicked
			whom = who_was_clicked(dos)
					
			if whom is img:  ## which isn't the button btw
				
				finished  = True
					
	


def present_no_choice_single(images, targetidx):
	
	img = [None] * 2
	
	## set the image locations
	## Images here are commandable sprites, so we can tell them what to do using Q below
	img[0] = CommandableImageSprite( screen, spot.center, button_image, scale=.5)
	img[1] = CommandableImageSprite( screen, double_displayat[1], images[targetidx], scale=QUAD_IMAGE_SCALE)
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# Set up the updates, etc. 
	
	# A queue of animation operations
	Q = DisplayQueue()
	
	# Draw a single animation in if you want!
	

	# What order do we draw sprites and things in?
	dos = OrderedUpdates(*img) # Draw and update in this order
	
	start_time = time()
	#play_sound(kstimulus("sounds/good_job.wav"))  ## This should be changed to play the proper intro sound for the character. right now it just, quite annoyingly, says "Good job!"
	## The standard event loop in kelpy -- this loops infinitely to process interactions
	## and throws events depending on what the user does
	finished = False
	clicked = [0] * 2

	for event in kelpy_standard_event_loop(screen, Q, dos):
		
		# if time()-start_time > MAX_DISPLAY_TIME:
		# 	pass

		# If the event is a click:
		if is_click(event) and not Q.commands:
			if finished:
				break
			# check if each of our images was clicked
			whom = who_was_clicked(dos)
					
			if whom is img[0]:  ## which isn't the button btw
				if clicked[1] > CLICKED_TIMES:
					pass
				else:
					clicked[1] = clicked[1] + 1
					if clicked[1] == 1:
						Q.append(obj='sound', file=(target_audio1[targetidx]) )
					elif clicked[1] == 2:
						Q.append(obj='sound', file=(target_audio2[targetidx]) )
					elif clicked[1] == 3:
						Q.append(obj='sound', file=(target_audio3[targetidx]) )
					elif clicked[1] == 4:
						Q.append(obj='sound', file=(target_audio1[targetidx]) )
					elif clicked[1] == 5:
						Q.append(obj='sound', file=(target_audio2[targetidx]) )
					elif clicked[1] == 6:
						Q.append(obj='sound', file=(target_audio3[targetidx]) )
					
					else:
						pass
					
					#Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images[targetidx], period=.5, duration=0, rotation=0, scale=IMAGE_SCALE, brightness=1.0 )
					
					Q.append(obj=img[1], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
					Q.append(obj=img[1], action="scale", amount=(1/1.5), duration=1.0)
					if clicked[1] == CLICKED_TIMES:
						clicked[1] = clicked[1]+1
						Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images_gray[targetidx], period=.5, duration=0, rotation=0, scale=QUAD_IMAGE_SCALE, brightness=1.0 )
						Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))
						finished = True

def present_no_choice_double(images, rightid, wrongid, order):
	
	guys = [None ,rightid, wrongid]
	img = [None] * 3
	totalclicks = -1
	## set the image locations
	## Images here are commandable sprites, so we can tell them what to do using Q below
	img[0] = CommandableImageSprite( screen, spot.center, button_image, scale=.5)
	img[1] = CommandableImageSprite( screen, double_displayat[0], images[rightid], scale=QUAD_IMAGE_SCALE)
	img[2] = CommandableImageSprite( screen, double_displayat[1] , images[wrongid], scale=QUAD_IMAGE_SCALE)
	
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# Set up the updates, etc. 
	def guytonumber(person):  ##should probably be a switch
			print person
			if person == rightid:
				return 1
			elif person == wrongid:
				return 2
			else:
				print "error, something went super wrong"

	# A queue of animation operations
	Q = DisplayQueue()
	
	# Draw a single animation in if you want!
	
	

	# What order do we draw sprites and things in?
	dos = OrderedUpdates(*img) # Draw and update in this order
	
	start_time = time()
	#play_sound(kstimulus("sounds/good_job.wav"))  ## This should be changed to play the proper intro sound for the character. right now it just, quite annoyingly, says "Good job!"
	finished = False
	clicked = [0] * 3
	## The standard event loop in kelpy -- this loops infinitely to process interactions
	## and throws events depending on what the user does
	for event in kelpy_standard_event_loop(screen, Q, dos):
		
		# if time()-start_time > MAX_DISPLAY_TIME:
		# 	pass # could make a limit if you wanted

		# If the event is a click:
		if is_click(event) and not Q.commands: 
			if finished: ## If this is the second click, move on to the next thing!
				break
			# check if each of our images was clicked
			whom = who_was_clicked( dos )
			
			if whom is img[0]:  ## which is the button btw
				print "BUTTON PRESS: " + str(time() - start_time) , 
				totalclicks = totalclicks+1
				if clicked[1] >CLICKED_TIMES and clicked[2]>CLICKED_TIMES :
					pass
				else:
					
					index = guytonumber(order[totalclicks]) ##convert that index from the main list to the internal index.
					print filename(target_images[guys[index]])
					clicked[index] = clicked[index] + 1
					if clicked[index] == 1:
						Q.append(obj='sound', file=(target_audio1[guys[index]]) )
					elif clicked[index] == 2:
						Q.append(obj='sound', file=(target_audio2[guys[index]]) )
					elif clicked[index] == 3:
						Q.append(obj='sound', file=(target_audio3[guys[index]]) )
					elif clicked[index] == 4:
						Q.append(obj='sound', file=(target_audio1[guys[index]]) )
					elif clicked[index] == 5:
						Q.append(obj='sound', file=(target_audio2[guys[index]]) )
					elif clicked[index] == 6:
						Q.append(obj='sound', file=(target_audio3[guys[index]]) )
					else:
						pass
					#Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images[targetidx], period=.5, duration=0, rotation=0, scale=IMAGE_SCALE, brightness=1.0 )
					
					Q.append(obj=img[index], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
					Q.append(obj=img[index], action="scale", amount=(1/1.5), duration=1.0)
					if clicked[index] == CLICKED_TIMES:
						clicked[index] = clicked[index]+1
						Q.append(obj=img[index], action='swapblink', position=(1000,400), image=target_images_gray[guys[index]], period=.5, duration=0, rotation=0, scale=QUAD_IMAGE_SCALE, brightness=1.0 )
						Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))
						if clicked[1] >CLICKED_TIMES and clicked[2]>CLICKED_TIMES :
							finished = True

def present_no_choice_quadruple(images, rightid, wrong1, wrong2, wrong3, order):
	
	guys = [None ,rightid, wrong1, wrong2, wrong3]

	img = [None] * 5
	totalclicks = -1
	## set the image locations
	## Images here are commandable sprites, so we can tell them what to do using Q below
	img[0] = CommandableImageSprite( screen, spot.center, button_image, scale=.5)
	img[1] = CommandableImageSprite( screen, quadruple_displayat[0], images[rightid], scale=QUAD_IMAGE_SCALE )
	img[2] = CommandableImageSprite( screen, quadruple_displayat[1] , images[wrong1], scale=QUAD_IMAGE_SCALE )
	img[3] = CommandableImageSprite( screen, quadruple_displayat[2], images[wrong2], scale=QUAD_IMAGE_SCALE )
	img[4] = CommandableImageSprite( screen, quadruple_displayat[3], images[wrong3], scale=QUAD_IMAGE_SCALE )

	def guytonumber(person):  ##should probably be a switch
			print person
			if person == rightid:
				return 1
			elif person == wrong1:
				return 2
			elif person == wrong2:
				return 3
			elif person == wrong3:
				return 4
			else:
				print "error, something went super wrong"


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# Set up the updates, etc. 
	
	# A queue of animation operations
	Q = DisplayQueue()
	
	# What order do we draw sprites and things in?
	dos = OrderedUpdates(*img) # Draw and update in this order
	
	start_time = time()
	#play_sound(kstimulus("sounds/good_job.wav"))  ## This should be changed to play the proper intro sound for the character. right now it just, quite annoyingly, says "Good job!"
	finished = False
	clicked = [0] * 5
	## The standard event loop in kelpy -- this loops infinitely to process interactions
	## and throws events depending on what the user does
	for event in kelpy_standard_event_loop(screen, Q, dos):
		
		# if time()-start_time > MAX_DISPLAY_TIME:
		# 	pass # could make a limit if you wanted

		# If the event is a click:
		if is_click(event) and not Q.commands: 
			if finished: ## If this is the second click, move on to the next thing!
				break
			# check if each of our images was clicked
			whom = who_was_clicked( dos )
			
			if whom is img[0]:  ## which is the button btw
				print "BUTTON PRESS: " + str(time() - start_time) , 
				totalclicks = totalclicks+1
				if clicked[1] >CLICKED_TIMES and clicked[2]>CLICKED_TIMES and clicked[3] > CLICKED_TIMES and clicked[4] > CLICKED_TIMES:
					pass
				else:
					
					index = guytonumber(order[totalclicks]) ##convert that index from the main list to the internal index.
					print filename(target_images[guys[index]])
					clicked[index] = clicked[index] + 1
					if clicked[index] == 1:
						Q.append(obj='sound', file=(target_audio1[guys[index]]) )
					elif clicked[index] == 2:
						Q.append(obj='sound', file=(target_audio2[guys[index]]) )
					elif clicked[index] == 3:
						Q.append(obj='sound', file=(target_audio3[guys[index]]) )
					elif clicked[index] == 4:
						Q.append(obj='sound', file=(target_audio1[guys[index]]) )
					elif clicked[index] == 5:
						Q.append(obj='sound', file=(target_audio2[guys[index]]) )
					elif clicked[index] == 6:
						Q.append(obj='sound', file=(target_audio3[guys[index]]) )
					else:
						pass
					#Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images[targetidx], period=.5, duration=0, rotation=0, scale=IMAGE_SCALE, brightness=1.0 )
					
					Q.append(obj=img[index], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
					Q.append(obj=img[index], action="scale", amount=(1/1.5), duration=1.0)
					if clicked[index] == CLICKED_TIMES:
						clicked[index] = clicked[index]+1
						Q.append(obj=img[index], action='swapblink', position=(1000,400), image=target_images_gray[guys[index]], period=.5, duration=0, rotation=0, scale=QUAD_IMAGE_SCALE, brightness=1.0 )
						Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))
						if clicked[1] >CLICKED_TIMES and clicked[2]>CLICKED_TIMES and clicked[3] > CLICKED_TIMES and clicked[4] > CLICKED_TIMES :
							finished = True

def present_no_choice_octuple(images, rightid, wrong1, wrong2, wrong3, wrong4, wrong5, wrong6, wrong7, order):
	
	guys = [None ,rightid, wrong1, wrong2, wrong3, wrong4, wrong5, wrong6, wrong7]
	totalclicks = -1
	img = [None] * 9
	
	## set the image locations
	## Images here are commandable sprites, so we can tell them what to do using Q below
	img[0] = CommandableImageSprite( screen, spot.center, button_image, scale=.5)
	img[1] = CommandableImageSprite( screen, octuple_displayat[0], images[rightid], scale=QUAD_IMAGE_SCALE )
	img[2] = CommandableImageSprite( screen, octuple_displayat[1] , images[wrong1], scale=QUAD_IMAGE_SCALE )
	img[3] = CommandableImageSprite( screen, octuple_displayat[2], images[wrong2], scale=QUAD_IMAGE_SCALE )
	img[4] = CommandableImageSprite( screen, octuple_displayat[3], images[wrong3], scale=QUAD_IMAGE_SCALE )
	img[5] = CommandableImageSprite( screen, octuple_displayat[4], images[wrong4], scale=QUAD_IMAGE_SCALE )
	img[6] = CommandableImageSprite( screen, octuple_displayat[5] , images[wrong5], scale=QUAD_IMAGE_SCALE )
	img[7] = CommandableImageSprite( screen, octuple_displayat[6], images[wrong6], scale=QUAD_IMAGE_SCALE )
	img[8] = CommandableImageSprite( screen, octuple_displayat[7], images[wrong7], scale=QUAD_IMAGE_SCALE )


	def guytonumber(person):  ##should probably be a switch
		print person
		if person == rightid:
			return 1
		elif person == wrong1:
			return 2
		elif person == wrong2:
			return 3
		elif person == wrong3:
			return 4
		elif person == wrong4:
			return 5
		elif person == wrong5:
			return 6
		elif person == wrong6:
			return 7
		elif person == wrong7:
			return 8
		else:
			print "error, something went super wrong"


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# Set up the updates, etc. 
	
	# A queue of animation operations
	Q = DisplayQueue()
	
	# Draw a single animation in if you want!
	
	

	# What order do we draw sprites and things in?
	dos = OrderedUpdates(*img) # Draw and update in this order
	
	start_time = time()
	
	finished = False
	clicked = [0] * 9
	## The standard event loop in kelpy -- this loops infinitely to process interactions
	## and throws events depending on what the user does
	for event in kelpy_standard_event_loop(screen, Q, dos):
		
		# if time()-start_time > MAX_DISPLAY_TIME:
		# 	pass # could make a limit if you wanted

		# If the event is a click:
		if is_click(event) and not Q.commands:
			if finished: ## If this is the second click, move on to the next thing!
				break
			# check if each of our images was clicked
			whom = who_was_clicked( dos )
			
			donezo = [ clicked[1] > CLICKED_TIMES ,
			 			clicked[2] > CLICKED_TIMES ,
			  			clicked[3] > CLICKED_TIMES , 
			  			clicked[4] > CLICKED_TIMES ,
			  			clicked[5] > CLICKED_TIMES , 
			  			clicked[6] > CLICKED_TIMES , 
			  			clicked[7] > CLICKED_TIMES ,
			  			clicked[8] > CLICKED_TIMES  ]


			if whom is img[0] :  ## which is the button btw
				print "BUTTON PRESS: " + str(time() - start_time) , 
				if all(donezo):
					pass
				else:
					#print "Before " + str( totalclicks)
					totalclicks = totalclicks+1
					#print "Before " + str( totalclicks) + "and " + str( order[totalclicks] )

					index = guytonumber(order[totalclicks]) ##convert that index from the main list to the internal index.
					print filename(target_images[guys[index]])
					clicked[index] = clicked[index] + 1
					if clicked[index] == 1:
						Q.append(obj='sound', file=(target_audio1[guys[index]]) )
					elif clicked[index] == 2:
						Q.append(obj='sound', file=(target_audio2[guys[index]]) )
					elif clicked[index] == 3:
						Q.append(obj='sound', file=(target_audio3[guys[index]]) )
					elif clicked[index] == 4:
						Q.append(obj='sound', file=(target_audio1[guys[index]]) )
					elif clicked[index] == 5:
						Q.append(obj='sound', file=(target_audio2[guys[index]]) )
					elif clicked[index] == 6:
						Q.append(obj='sound', file=(target_audio3[guys[index]]) )
					else:
						pass
					#Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images[targetidx], period=.5, duration=0, rotation=0, scale=IMAGE_SCALE, brightness=1.0 )
					
					Q.append(obj=img[index], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
					Q.append(obj=img[index], action="scale", amount=(1/1.5), duration=1.0)
					if clicked[index] == CLICKED_TIMES:
						clicked[index] = clicked[index]+1
						Q.append(obj=img[index], action='swapblink', position=(1000,400), image=target_images_gray[guys[index]], period=.5, duration=0, rotation=0, scale=QUAD_IMAGE_SCALE, brightness=1.0 )
						Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))
						if clicked[1] >CLICKED_TIMES and clicked[2]>CLICKED_TIMES and clicked[3] > CLICKED_TIMES and clicked[4] > CLICKED_TIMES and clicked[5] >CLICKED_TIMES and clicked[6]>CLICKED_TIMES and clicked[7] > CLICKED_TIMES and clicked[8] > CLICKED_TIMES:
							finished = True
			
	
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main experiment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	
location = os.path.dirname( __file__ )+"stuph/"  ##This returns the filepath relative to this file. We're loading a bunch of things from the stimuli folder.

target_images = [
location+"beppo.png",
location+"deela.png",
location+"fina.png",
location+"guffi.png",
location+"higoo.png",
location+"kogay.png",
location+"lato.png",
location+"mobi.png",
location+"nadoo.png",
location+"pavy.png",
location+"roozy.png",
location+"soma.png",
location+"tibble.png",
location+"vaylo.png",
location+"zefay.png"
]
target_images_gray = [
location+"beppo_gray.png",
location+"deela_gray.png",
location+"fina_gray.png",
location+"guffi_gray.png",
location+"higoo_gray.png",
location+"kogay_gray.png",
location+"lato_gray.png",
location+"mobi_gray.png",
location+"nadoo_gray.png",
location+"pavy_gray.png",
location+"roozy_gray.png",
location+"soma_gray.png",
location+"tibble_gray.png",
location+"vaylo_gray.png",
location+"zefay_gray.png"
]
audio1 = os.path.dirname( __file__ )+"stimuli/audio/look1/"  ##This returns the filepath relative to this file. We're loading a bunch of things from the stimuli folder.


target_audio2 = [
audio1+"At_beppo.wav",
audio1+"At_deela.wav",
audio1+"At_finna.wav",
audio1+"At_guffi.wav",
audio1+"At_higoo.wav",
audio1+"At_kogay.wav",
audio1+"At_lahdo.wav",
audio1+"At_mobi.wav",
audio1+"At_nadoo.wav",
audio1+"At_pavy.wav",
audio1+"At_roozy.wav",
audio1+"At_soma.wav",
audio1+"At_tibble.wav",
audio1+"At_vaylo.wav",
audio1+"At_zefay.wav"
  
  ] ## unimplemented, should contain a list of all the audio intros in order (the same order as the things above).
audio2 = os.path.dirname( __file__ )+"stimuli/audio/look2/"  ##This returns the filepath relative to this file. We're loading a bunch of things from the stimuli folder.


target_audio1 = [
audio2+"Look_beppo.wav",
audio2+"Look_deela.wav",
audio2+"Look_finna.wav",
audio2+"Look_guffi.wav",
audio2+"Look_higoo.wav",
audio2+"Look_kogay.wav",
audio2+"Look_lahdo.wav",
audio2+"Look_mobi.wav",
audio2+"Look_nadoo.wav",
audio2+"Look_pavy.wav",
audio2+"Look_roozy.wav",
audio2+"Look_soma.wav",
audio2+"Look_tibble.wav",
audio2+"Look_vaylo.wav",
audio2+"Look_zefay.wav"
  ]

audio3 = os.path.dirname( __file__ )+"stimuli/audio/hello/"  ##This returns the filepath relative to this file. We're loading a bunch of things from the stimuli folder.


target_audio3 = [
audio3+"Hello_beppo.wav",
audio3+"Hello_deela.wav",
audio3+"Hello_finna.wav",
audio3+"Hello_guffi.wav",
audio3+"Hello_higoo.wav",
audio3+"Hello_kogay.wav",
audio3+"Hello_lahdo.wav",
audio3+"Hello_mobi.wav",
audio3+"Hello_nadoo.wav",
audio3+"Hello_pavy.wav",
audio3+"Hello_roozy.wav",
audio3+"Hello_soma.wav",
audio3+"Hello_tibble.wav",
audio3+"Hello_vaylo.wav",
audio3+"Hello_zefay.wav"
  ]



SIXTEEN_OFFSET = 75

button_image = kstimulus("shapes/circle_purple.png")

## set up display spots
double_displayat = [ (screen.get_width()/4, 400), ((screen.get_width()/4)*3, 400) ] 
quadruple_displayat= [ ((screen.get_width()/4) + 90, 400), ((screen.get_width()/4)-100, 400),  (((screen.get_width()/4)*3)+100, 400) , (((screen.get_width()/4)*3)-90, 400) ]
octuple_displayat =[ ((screen.get_width()/4) + OCTUPLE_OFFSET, 400-OCTUPLE_OFFSET), ((screen.get_width()/4) + OCTUPLE_OFFSET, 400+OCTUPLE_OFFSET),  ((screen.get_width()/4)-OCTUPLE_OFFSET, 400-OCTUPLE_OFFSET), ((screen.get_width()/4)-OCTUPLE_OFFSET, 400+OCTUPLE_OFFSET),  (((screen.get_width()/4)*3)+OCTUPLE_OFFSET, 400-OCTUPLE_OFFSET) , (((screen.get_width()/4)*3)+OCTUPLE_OFFSET, 400+OCTUPLE_OFFSET), (((screen.get_width()/4)*3)-OCTUPLE_OFFSET, 400-OCTUPLE_OFFSET), (((screen.get_width()/4)*3)-OCTUPLE_OFFSET, 400+OCTUPLE_OFFSET) ]
sixteen_displayat =[ 
	( ((screen.get_width()/6)*1, ((screen.get_height()/4)*1))) ,
	( ((screen.get_width()/6)*2, ((screen.get_height()/4)*1) )),
	( ((screen.get_width()/6)*3, ((screen.get_height()/4)*1) )),
	( ((screen.get_width()/6)*4, ((screen.get_height()/4)*1))) ,
	( ((screen.get_width()/6)*5, ((screen.get_height()/4)*1))) ,
	( ((screen.get_width()/6)*1, ((screen.get_height()/4)*2))) ,
	( ((screen.get_width()/6)*2, ((screen.get_height()/4)*2) )),
	( ((screen.get_width()/6)*3, ((screen.get_height()/4)*2) )),
	( ((screen.get_width()/6)*4, ((screen.get_height()/4)*2) )),
	( ((screen.get_width()/6)*5, ((screen.get_height()/4)*2) )) ,
	( ((screen.get_width()/6)*1, ((screen.get_height()/4)*3) )) ,
	( ((screen.get_width()/6)*2, ((screen.get_height()/4)*3) )),
	( ((screen.get_width()/6)*3, ((screen.get_height()/4)*3) )),
	( ((screen.get_width()/6)*4, ((screen.get_height()/4)*3) )) ,
	( ((screen.get_width()/6)*5, ((screen.get_height()/4)*3) )) ]



##present a number of blocks

#!# Can use random.sample
def pickrandom(number):
	numbers = []
	picks = 0
	while picks < number:
		pick = randint(0,(len(target_images)-1))
		if pick not in numbers:
			#print pick
			numbers.append(pick)
			picks = picks + 1
	return numbers

seeds = pickrandom(15)
targetidx = randint(0,(len(target_images)-1))
# print "CHOICE SINGLES:"

display_wait_scene()
print present_no_choice_single(target_images, seeds[0])
display_wait_scene()
display_naming_scene(screen, target_images, [seeds[0]], sixteen_displayat , QUAD_IMAGE_SCALE)
# print "CHOICE DOUBLES:" #################!# Can use random.sample
def pickrandom(number):
	numbers = []
	picks = 0
	while picks < number:
		pick = randint(0,(len(target_images)-1))
		if pick not in numbers:
			#print pick
			numbers.append(pick)
			picks = picks + 1
	return numbers
display_wait_scene()
for block in range(1):	  ########## NOTE: You can adjust the amount of times this runs a single by adjusting the integer in the parenthesis there <<< --------
	 ## this is that function above ^^ to pick some non-repeating random integers
	shuffle(double_displayat)
	#print block, filename(target_images[seeds[0]]),filename(target_images[seeds[1]])
	order = []
	for i in range( 0, CLICKED_TIMES):
		order.append(  seeds[1]  )
		order.append(  seeds[2] )
		shuffle( order )
	print present_no_choice_double(target_images, seeds[1], seeds[2], order )

display_wait_scene()
display_naming_scene(screen, target_images, seeds[1:3] , sixteen_displayat, QUAD_IMAGE_SCALE)
display_wait_scene()


# print "CHOICE QUADRUPLES:" ################################33
for block in range(1):	########## NOTE: You can adjust the amount of times this runs  by adjusting the integer in the parenthesis there <<< --------
	
	 #pick some random images to display (by picking random indexes which we'll use to pull things from the array of image locations).
	shuffle(quadruple_displayat)
	order = []
	for i in range( 0, CLICKED_TIMES):
		order.append( seeds[3] )
		order.append(  seeds[4] )
		order.append( seeds[5] )
		order.append( seeds[6] )
		shuffle( order )
	#print block, filename(target_images[seeds[0]]),filename(target_images[seeds[1]]), filename(target_images[seeds[2]]), filename(target_images[seeds[3]])
	print present_no_choice_quadruple(target_images, seeds[3], seeds[4], seeds[5] ,seeds[6], order )
	#!# Or: print present_choice_quadruple(target_images, *seeds)
display_wait_scene()
display_naming_scene(screen, target_images, seeds[3:7], sixteen_displayat, QUAD_IMAGE_SCALE)
display_wait_scene()
# print "CHOICE OCTUPLES:"  ################################




display_wait_scene()
for block in range (1):     ########## NOTE: You can adjust the amount of times this runs by adjusting the integer in the parenthesis there <<< --------
	
	shuffle (octuple_displayat)
	order = []
	for i in range( 0, CLICKED_TIMES):
		order.append( seeds[7]  )
		order.append(  seeds[8]  )
		order.append(  seeds[9] )
		order.append(  seeds[10] )
		order.append(  seeds[11] )
		order.append(  seeds[12]  )
		order.append(  seeds[13]  )
		order.append( seeds[14]  )
		shuffle( order )
	#print block, filename(target_images[seeds[0]]),filename(target_images[seeds[1]]), filename(target_images[seeds[2]]), filename(target_images[seeds[3]]), filename(target_images[seeds[4]]), filename(target_images[seeds[5]]), filename(target_images[seeds[6]]), filename(target_images[seeds[7]]),
	print present_no_choice_octuple(target_images, seeds[7], seeds[8], seeds[9] ,seeds[10] ,seeds[11] ,seeds[12], seeds[13], seeds[14], order )

display_wait_scene()
display_naming_scene(screen, target_images, seeds[7:15], sixteen_displayat, QUAD_IMAGE_SCALE )
display_wait_scene()

















#for block in range(2):
### finally run the thing, also print the block number, the targetidx, and the index of the correct image. ##Note that this may display duplicates as is.
### the last item is the presen_trial function that actually runs the trial.
	#targetidx = randint(0,(len(target_images)-1))
	#print "SINGLES:"
	#print block, targetidx, filename(target_images[targetidx]), present_no_choice_single(target_images, targetidx)

# print "NO CHOICE DOUBLES:"
# for block in range(2):	

#  	targetidx = randint(0,(len(target_images)-1)) #pick a new image to start at.
#  	shuffle(double_displayat)
#  	order = [1,2,1,2,1,2]
#  	print block, targetidx, filename(target_images[targetidx]), present_no_choice_double(target_images, targetidx, (targetidx-1), order)

# print "NO CHOICE QUADRUPLES:"
# for block in range(2):	
# 	order = [1,2,4,3,2,2,3,4,3,1,4,1]
#  	targetidx = randint(0,(len(target_images)-1)) #pick a new image to start at.
#  	shuffle(quadruple_displayat)
#  	print block, targetidx, filename(target_images[targetidx]), present_no_choice_quadruple(target_images, targetidx, (targetidx-1), (targetidx-2), (targetidx-3))

# print "NO CHOICE OCTUPLES:"
# for block in range(2):	
# 	order = [1,3,4,2,6,7,8,8,8,4,3,4,3,2,2,1,1,5,5,5,6,6,7,7]
# 	targetidx = randint(0,(len(target_images)-1)) #pick a new image to start at.
#  	shuffle(quadruple_displayat)
#  	print block, targetidx, filename(target_images[targetidx]), present_no_choice_octuple(target_images, targetidx, (targetidx-1), (targetidx-2), (targetidx-3), (targetidx-4), (targetidx-5) ,(targetidx-6), (targetidx-7) )

