# -*- coding: utf-8 -*-

"""

	No Choice tasks...

"""

import os, sys
import pygame
from random import randint, choice, sample, shuffle
from time import time

from kelpy.CommandableImageSprite import *
from kelpy.Miscellaneous import *
from kelpy.DisplayQueue import *
from kelpy.OrderedUpdates import *
from kelpy.EventHandler import *

IMAGE_SCALE = 0.15
QUAD_IMAGE_SCALE = .12
OCTUPLE_OFFSET = 150
HOFFSET = 100
VOFFSET = 100
MAX_DISPLAY_TIME = 3.0
GROW_RATIO = 1.2
##############################################
## Set up pygame

screen, spot = initialize_kelpy(fullscreen=True)

OFF_LEFT = spot.west
background_color = (140, 140, 140) # 90 # 190

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Run a single trial
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	

def present_choice_single(images, targetidx):
	
	img = [None] * 2
	
	## set the image locations
	## Images here are commandable sprites, so we can tell them what to do using Q below
	img[0] = CommandableImageSprite( screen, spot.center, button_image, scale=.5, brightness=.5)
	img[1] = CommandableImageSprite( screen, double_displayat[1], images[targetidx], scale=IMAGE_SCALE)
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# Set up the updates, etc. 
	
	# A queue of animation operations
	Q = DisplayQueue()
	
	timesclicked = 0

	# What order do we draw sprites and things in?
	dos = OrderedUpdates(*img) # Draw and update in this order
	
	start_time = time()
	#play_sound(kstimulus("sounds/good_job.wav"))  ## This should be changed to play the proper intro sound for the character. right now it just, quite annoyingly, says "Good job!"
	## The standard event loop in kelpy -- this loops infinitely to process interactions
	## and throws events depending on what the user does
	finished = False
	
	for event in kelpy_standard_event_loop(screen, Q, dos):
		
		if timesclicked == 3:
			timesclicked = timesclicked+1
			Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images_gray[targetidx], period=.5, duration=0, rotation=0, scale=IMAGE_SCALE, brightness=1.0 )
			Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))

		

		# If the event is a click:
		if is_click(event):
			
				
			# check if each of our images was clicked
			whom = who_was_clicked(dos)
			

			if whom is img[1]:  ## which is the button btw
				if timesclicked > 3:
					break
				else:
					timesclicked = timesclicked + 1
					#play_sound(kstimulus("sounds/good_job.wav")) 
					#Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images[targetidx], period=.5, duration=0, rotation=0, scale=IMAGE_SCALE, brightness=1.0 )
					
					Q.append(obj=img[1], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
					Q.append(obj=img[1], action="scale", amount=(1/1.5), duration=1.0)

def present_choice_double(images, rightid, wrongid):
	

	img = [None] * 3
	
	## set the image locations
	## Images here are commandable sprites, so we can tell them what to do using Q below
	img[0] = CommandableImageSprite( screen, spot.center, button_image, scale=.5, brightness=.5)
	img[1] = CommandableImageSprite( screen, double_displayat[0], images[rightid], scale=IMAGE_SCALE)
	img[2] = CommandableImageSprite( screen, double_displayat[1] , images[wrongid], scale=IMAGE_SCALE)
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# Set up the updates, etc. 
	
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
		

		# If the event is a click:
		if is_click(event):
			
			# check if each of our images was clicked
			whom = who_was_clicked(dos)
			
			if whom is img[1]:  ## which is the button btw
				if clicked[1] > 3:
					pass
				else:
					clicked[1] = clicked[1] + 1
					#play_sound(kstimulus("sounds/good_job.wav")) 
					#Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images[targetidx], period=.5, duration=0, rotation=0, scale=IMAGE_SCALE, brightness=1.0 )
					
					Q.append(obj=img[1], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
					Q.append(obj=img[1], action="scale", amount=(1/1.5), duration=1.0)
					if clicked[1] == 3:
						clicked[1] = clicked[1]+1
						Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images_gray[rightid], period=.5, duration=0, rotation=0, scale=IMAGE_SCALE, brightness=1.0 )
						Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))

			if whom is img[2]:  ## which is the button btw
				if clicked[2] > 3:
					pass
				else:
					clicked[2] = clicked[2] + 1
					#play_sound(kstimulus("sounds/good_job.wav")) 
					#Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images[targetidx], period=.5, duration=0, rotation=0, scale=IMAGE_SCALE, brightness=1.0 )
					
					Q.append(obj=img[2], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
					Q.append(obj=img[2], action="scale", amount=(1/1.5), duration=1.0)
					if clicked[2] == 3:
						clicked[2] = clicked[2]+1
						Q.append(obj=img[2], action='swapblink', position=(1000,400), image=target_images_gray[wrongid], period=.5, duration=0, rotation=0, scale=IMAGE_SCALE, brightness=1.0 )
						Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))
			
def present_choice_quadruple(images, rightid, wrong1, wrong2, wrong3):
	

	img = [None] * 5
	
	## set the image locations
	## Images here are commandable sprites, so we can tell them what to do using Q below
	img[0] = CommandableImageSprite( screen, spot.center, button_image, scale=.5, brightness=.5)
	img[1] = CommandableImageSprite( screen, quadruple_displayat[0], images[rightid], scale=QUAD_IMAGE_SCALE )
	img[2] = CommandableImageSprite( screen, quadruple_displayat[1] , images[wrong1], scale=QUAD_IMAGE_SCALE )
	img[3] = CommandableImageSprite( screen, quadruple_displayat[2], images[wrong2], scale=QUAD_IMAGE_SCALE )
	img[4] = CommandableImageSprite( screen, quadruple_displayat[3], images[wrong3], scale=QUAD_IMAGE_SCALE )


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# Set up the updates, etc. 
	
	# A queue of animation operations
	Q = DisplayQueue()
	
	# Draw a single animation in if you want!
	
	

	# What order do we draw sprites and things in?
	dos = OrderedUpdates(*img) # Draw and update in this order
	
	start_time = time()
	play_sound(kstimulus("sounds/good_job.wav"))  ## This should be changed to play the proper intro sound for the character. right now it just, quite annoyingly, says "Good job!"
	finished = False
	clicked = [0] * 5

 	## The standard event loop in kelpy -- this loops infinitely to process interactions
	## and throws events depending on what the user does
	for event in kelpy_standard_event_loop(screen, Q, dos):
		

		# If the event is a click:
		if is_click(event):
			
			# check if each of our images was clicked
			whom = who_was_clicked(dos)
			
			if whom is img[1]:  ## which is the button btw
				if clicked[1] > 3:
					pass
				else:
					clicked[1] = clicked[1] + 1
					#play_sound(kstimulus("sounds/good_job.wav")) 
					#Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images[targetidx], period=.5, duration=0, rotation=0, scale=IMAGE_SCALE, brightness=1.0 )
					
					Q.append(obj=img[1], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
					Q.append(obj=img[1], action="scale", amount=(1/1.5), duration=1.0)
					if clicked[1] == 3:
						clicked[1] = clicked[1]+1
						Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images_gray[rightid], period=.5, duration=0, rotation=0, scale=QUAD_IMAGE_SCALE, brightness=1.0 )
						Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))

			if whom is img[2]:  ## which is the button btw
				if clicked[2] > 3:
					pass
				else:
					clicked[2] = clicked[2] + 1
					#play_sound(kstimulus("sounds/good_job.wav")) 
					#Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images[targetidx], period=.5, duration=0, rotation=0, scale=IMAGE_SCALE, brightness=1.0 )
					
					Q.append(obj=img[2], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
					Q.append(obj=img[2], action="scale", amount=(1/1.5), duration=1.0)
					if clicked[2] == 3:
						clicked[2] = clicked[2]+1
						Q.append(obj=img[2], action='swapblink', position=(1000,400), image=target_images_gray[wrong1], period=.5, duration=0, rotation=0, scale=QUAD_IMAGE_SCALE, brightness=1.0 )
						Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))

			if whom is img[3]:  ## which is the button btw
				if clicked[3] > 3:
					pass
				else:
					clicked[3] = clicked[3] + 1
					#play_sound(kstimulus("sounds/good_job.wav")) 
					#Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images[targetidx], period=.5, duration=0, rotation=0, scale=IMAGE_SCALE, brightness=1.0 )
					
					Q.append(obj=img[3], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
					Q.append(obj=img[3], action="scale", amount=(1/1.5), duration=1.0)
					if clicked[3] == 3:
						clicked[3] = clicked[3]+1
						Q.append(obj=img[3], action='swapblink', position=(1000,400), image=target_images_gray[wrong2], period=.5, duration=0, rotation=0, scale=QUAD_IMAGE_SCALE, brightness=1.0 )
						Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))

			if whom is img[4]:  ## which is the button btw
				if clicked[4] > 3:
					pass
				else:
					clicked[4] = clicked[4] + 1
					#play_sound(kstimulus("sounds/good_job.wav")) 
					#Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images[targetidx], period=.5, duration=0, rotation=0, scale=IMAGE_SCALE, brightness=1.0 )
					
					Q.append(obj=img[4], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
					Q.append(obj=img[4], action="scale", amount=(1/1.5), duration=1.0)
					if clicked[4] == 3:
						clicked[4] = clicked[4]+1
						Q.append(obj=img[4], action='swapblink', position=(1000,400), image=target_images_gray[wrong3], period=.5, duration=0, rotation=0, scale=QUAD_IMAGE_SCALE, brightness=1.0 )
						Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))
			
def present_choice_octuple(images, rightid, wrong1, wrong2, wrong3, wrong4, wrong5, wrong6, wrong7):
	

	img = [None] * 9
	
	## set the image locations
	## Images here are commandable sprites, so we can tell them what to do using Q below
	img[0] = CommandableImageSprite( screen, spot.center, button_image, scale=.5, brightness=.5)
	img[1] = CommandableImageSprite( screen, octuple_displayat[0], images[rightid], scale=QUAD_IMAGE_SCALE )
	img[2] = CommandableImageSprite( screen, octuple_displayat[1] , images[wrong1], scale=QUAD_IMAGE_SCALE )
	img[3] = CommandableImageSprite( screen, octuple_displayat[2], images[wrong2], scale=QUAD_IMAGE_SCALE )
	img[4] = CommandableImageSprite( screen, octuple_displayat[3], images[wrong3], scale=QUAD_IMAGE_SCALE )
	img[5] = CommandableImageSprite( screen, octuple_displayat[4], images[wrong4], scale=QUAD_IMAGE_SCALE )
	img[6] = CommandableImageSprite( screen, octuple_displayat[5] , images[wrong5], scale=QUAD_IMAGE_SCALE )
	img[7] = CommandableImageSprite( screen, octuple_displayat[6], images[wrong6], scale=QUAD_IMAGE_SCALE )
	img[8] = CommandableImageSprite( screen, octuple_displayat[7], images[wrong7], scale=QUAD_IMAGE_SCALE )



	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# Set up the updates, etc. 
	
	# A queue of animation operations
	Q = DisplayQueue()
	
	# Draw a single animation in if you want!
	
	

	# What order do we draw sprites and things in?
	dos = OrderedUpdates(*img) # Draw and update in this order
	
	start_time = time()
	play_sound(kstimulus("sounds/good_job.wav"))  ## This should be changed to play the proper intro sound for the character. right now it just, quite annoyingly, says "Good job!"
	finished = False
	clicked = [0] * 9

 	## The standard event loop in kelpy -- this loops infinitely to process interactions
	## and throws events depending on what the user does
	for event in kelpy_standard_event_loop(screen, Q, dos):
		

		# If the event is a click:
		if is_click(event):
			
			# check if each of our images was clicked
			whom = who_was_clicked(dos)
			
			if whom is img[1]:  ## which is the button btw
				if clicked[1] > 3:
					pass
				else:
					clicked[1] = clicked[1] + 1
					#play_sound(kstimulus("sounds/good_job.wav")) 
					#Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images[targetidx], period=.5, duration=0, rotation=0, scale=IMAGE_SCALE, brightness=1.0 )
					
					Q.append(obj=img[1], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
					Q.append(obj=img[1], action="scale", amount=(1/1.5), duration=1.0)
					if clicked[1] == 3:
						clicked[1] = clicked[1]+1
						Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images_gray[rightid], period=.5, duration=0, rotation=0, scale=QUAD_IMAGE_SCALE, brightness=1.0 )
						Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))

			if whom is img[2]:  ## which is the button btw
				if clicked[2] > 3:
					pass
				else:
					clicked[2] = clicked[2] + 1
					#play_sound(kstimulus("sounds/good_job.wav")) 
					#Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images[targetidx], period=.5, duration=0, rotation=0, scale=IMAGE_SCALE, brightness=1.0 )
					
					Q.append(obj=img[2], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
					Q.append(obj=img[2], action="scale", amount=(1/1.5), duration=1.0)
					if clicked[2] == 3:
						clicked[2] = clicked[2]+1
						Q.append(obj=img[2], action='swapblink', position=(1000,400), image=target_images_gray[wrong1], period=.5, duration=0, rotation=0, scale=QUAD_IMAGE_SCALE, brightness=1.0 )
						Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))

			if whom is img[3]:  ## which is the button btw
				if clicked[3] > 3:
					pass
				else:
					clicked[3] = clicked[3] + 1
					#play_sound(kstimulus("sounds/good_job.wav")) 
					#Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images[targetidx], period=.5, duration=0, rotation=0, scale=IMAGE_SCALE, brightness=1.0 )
					
					Q.append(obj=img[3], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
					Q.append(obj=img[3], action="scale", amount=(1/1.5), duration=1.0)
					if clicked[3] == 3:
						clicked[3] = clicked[3]+1
						Q.append(obj=img[3], action='swapblink', position=(1000,400), image=target_images_gray[wrong2], period=.5, duration=0, rotation=0, scale=QUAD_IMAGE_SCALE, brightness=1.0 )
						Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))

			if whom is img[4]:  ## which is the button btw
				if clicked[4] > 3:
					pass
				else:
					clicked[4] = clicked[4] + 1
					#play_sound(kstimulus("sounds/good_job.wav")) 
					#Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images[targetidx], period=.5, duration=0, rotation=0, scale=IMAGE_SCALE, brightness=1.0 )
					
					Q.append(obj=img[4], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
					Q.append(obj=img[4], action="scale", amount=(1/1.5), duration=1.0)
					if clicked[4] == 3:
						clicked[4] = clicked[4]+1
						Q.append(obj=img[4], action='swapblink', position=(1000,400), image=target_images_gray[wrong3], period=.5, duration=0, rotation=0, scale=QUAD_IMAGE_SCALE, brightness=1.0 )
						Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))
			if whom is img[5]:  ## which is the button btw
				if clicked[5] > 3:
					pass
				else:
					clicked[5] = clicked[5] + 1
					#play_sound(kstimulus("sounds/good_job.wav")) 
					#Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images[targetidx], period=.5, duration=0, rotation=0, scale=IMAGE_SCALE, brightness=1.0 )
					
					Q.append(obj=img[5], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
					Q.append(obj=img[5], action="scale", amount=(1/1.5), duration=1.0)
					if clicked[5] == 3:
						clicked[5] = clicked[5]+1
						Q.append(obj=img[5], action='swapblink', position=(1000,400), image=target_images_gray[wrong4], period=.5, duration=0, rotation=0, scale=QUAD_IMAGE_SCALE, brightness=1.0 )
						Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))

			if whom is img[6]:  ## which is the button btw
				if clicked[6] > 3:
					pass
				else:
					clicked[6] = clicked[6] + 1
					#play_sound(kstimulus("sounds/good_job.wav")) 
					#Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images[targetidx], period=.5, duration=0, rotation=0, scale=IMAGE_SCALE, brightness=1.0 )
					
					Q.append(obj=img[6], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
					Q.append(obj=img[6], action="scale", amount=(1/1.5), duration=1.0)
					if clicked[6] == 3:
						clicked[6] = clicked[2]+1
						Q.append(obj=img[6], action='swapblink', position=(1000,400), image=target_images_gray[wrong5], period=.5, duration=0, rotation=0, scale=QUAD_IMAGE_SCALE, brightness=1.0 )
						Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))

			if whom is img[7]:  ## which is the button btw
				if clicked[7] > 3:
					pass
				else:
					clicked[7] = clicked[7] + 1
					#play_sound(kstimulus("sounds/good_job.wav")) 
					#Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images[targetidx], period=.5, duration=0, rotation=0, scale=IMAGE_SCALE, brightness=1.0 )
					
					Q.append(obj=img[7], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
					Q.append(obj=img[7], action="scale", amount=(1/1.5), duration=1.0)
					if clicked[7] == 3:
						clicked[7] = clicked[7]+1
						Q.append(obj=img[7], action='swapblink', position=(1000,400), image=target_images_gray[wrong6], period=.5, duration=0, rotation=0, scale=QUAD_IMAGE_SCALE, brightness=1.0 )
						Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))

			if whom is img[8]:  ## which is the button btw
				if clicked[8] > 3:
					pass
				else:
					clicked[8] = clicked[8] + 1
					#play_sound(kstimulus("sounds/good_job.wav")) 
					#Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images[targetidx], period=.5, duration=0, rotation=0, scale=IMAGE_SCALE, brightness=1.0 )
					
					Q.append(obj=img[8], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
					Q.append(obj=img[8], action="scale", amount=(1/1.5), duration=1.0)
					if clicked[8] == 3:
						clicked[8] = clicked[8]+1
						Q.append(obj=img[8], action='swapblink', position=(1000,400), image=target_images_gray[wrong7], period=.5, duration=0, rotation=0, scale=QUAD_IMAGE_SCALE, brightness=1.0 )
						Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))
	
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main experiment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	

# Set up images:
location = os.path.dirname( __file__ )+"stimuli/"  ##This returns the filepath relative to this file. We're loading a bunch of things from the stimuli folder.

target_images = [
location+"bluedrop.png",
location+"bluewolf.png",
location+"bunnyboy.png",
location+"flatmouse.png",
location+"greenhog.png",
location+"pokeydog.png",
location+"purplepandapony.png",
location+"polkadotrocker.png",
location+"queenbear.png",
location+"skimaskbunny.png",
location+"thuglion.png",
location+"treegirl.png",
location+"whitemetalbear.png",
location+"cubehouseguy.png",
location+"greencatwheels.png",
location+"greenclownbunny.png",
location+"yellowegghead.png",
location+"bluebearnoship.png"
]
target_images_gray = [
location+"bluedrop_gray.png",
location+"bluewolf_gray.png",
location+"bunnyboy_gray.png",
location+"flatmouse_gray.png",
location+"greenhog_gray.png",
location+"pokeydog_gray.png",
location+"purplepandapony_gray.png",
location+"polkadotrocker_gray.png",
location+"queenbear_gray.png",
location+"skimaskbunny_gray.png",
location+"thuglion_gray.png",
location+"treegirl_gray.png",
location+"whitemetalbear_gray.png", 
location+"cubehouseguy_gray.png",
location+"greencatwheels_gray.png",
location+"greenclownbunny_gray.png",
location+"yellowegghead_gray.png",
location+"bluebearnoship_gray.png"
]

target_audio = [ ] ## unimplemented, should contain a list of all the audio intros in order (the same order as the things above).

button_image = kstimulus("shapes/circle_purple.png")

## set up display spots
double_displayat = [ (screen.get_width()/4, 400), ((screen.get_width()/4)*3, 400) ] 
quadruple_displayat= [ ((screen.get_width()/4) + 100, 400), ((screen.get_width()/4)-100, 400),  (((screen.get_width()/4)*3)+100, 400) , (((screen.get_width()/4)*3)-100, 400) ]
octuple_displayat =[ ((screen.get_width()/4) + OCTUPLE_OFFSET, 400-OCTUPLE_OFFSET), ((screen.get_width()/4) + OCTUPLE_OFFSET, 400+OCTUPLE_OFFSET),  ((screen.get_width()/4)-OCTUPLE_OFFSET, 400-OCTUPLE_OFFSET), ((screen.get_width()/4)-OCTUPLE_OFFSET, 400+OCTUPLE_OFFSET),  (((screen.get_width()/4)*3)+OCTUPLE_OFFSET, 400-OCTUPLE_OFFSET) , (((screen.get_width()/4)*3)+OCTUPLE_OFFSET, 400+OCTUPLE_OFFSET), (((screen.get_width()/4)*3)-OCTUPLE_OFFSET, 400-OCTUPLE_OFFSET), (((screen.get_width()/4)*3)-OCTUPLE_OFFSET, 400+OCTUPLE_OFFSET) ]
##present a number of blocks



## finally run the thing, also print the block number, the targetidx, and the index of the correct image. ##Note that this may display duplicates as is.
## the last item is the presen_trial function that actually runs the trial.


# targetidx = randint(0,(len(target_images)-1))
# print "SINGLES:"
# print targetidx, filename(target_images[targetidx]), present_choice_single(target_images, targetidx)

# print "CHOICE DOUBLES:"

# targetidx = randint(0,(len(target_images)-1)) #pick a new image to start at.
# shuffle(double_displayat)
# print targetidx, filename(target_images[targetidx]), present_choice_double(target_images, targetidx, (targetidx-1))

#print "NO CHOICE QUADRUPLES:"
# for block in range(10):	

#targetidx = randint(0,(len(target_images)-1)) #pick a new image to start at.
#shuffle(quadruple_displayat)
#print targetidx, filename(target_images[targetidx]), present_choice_quadruple(target_images, targetidx, (targetidx-1), (targetidx-2), (targetidx-3))

print "NO CHOICE OCTUPLES:"
	

targetidx = randint(0,(len(target_images)-1)) #pick a new image to start at.
shuffle(quadruple_displayat)
print targetidx, filename(target_images[targetidx]), present_choice_octuple(target_images, targetidx, (targetidx-1), (targetidx-2), (targetidx-3), (targetidx-4), (targetidx-5) ,(targetidx-6), (targetidx-7) )


