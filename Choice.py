# -*- coding: utf-8 -*-

"""

	Choice tasks...

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
from scenes import display_naming_scene


IMAGE_SCALE = 0.15
QUAD_IMAGE_SCALE = .11
OCTUPLE_OFFSET = 115
HOFFSET = 100
VOFFSET = 100
MAX_DISPLAY_TIME = 3.0
GROW_RATIO = 1.2
CLICK_LIMIT = 6
##############################################
## Set up pygame

screen, spot = initialize_kelpy(fullscreen=True)

OFF_LEFT = spot.west
background_color = (140, 140, 140) # 90 # 190

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
				

def present_choice_single(images, targetidx):
	
	img = [None] * 2
	
	## set the image locations
	## Images here are commandable sprites, so we can tell them what to do using Q below
	img[0] = CommandableImageSprite( screen, spot.center, button_image, scale=.5, brightness=.5)
	img[1] = CommandableImageSprite( screen, double_displayat[1], images[targetidx[0]], scale=QUAD_IMAGE_SCALE)
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# Set up the updates, etc. 
	
	# A queue of animation operations
	Q = DisplayQueue()
	
	timesclicked = 0  ##keep track of how many times things have been clicked! this one is just a single int

	# What order do we draw sprites and things in?
	dos = OrderedUpdates(*img) # Draw and update in this order
	
	start_time = time()  ## start logging the start time. start.
	
	## The standard event loop in kelpy -- this loops infinitely to process interactions
	## and throws events depending on what the user does
	finished = False
	
	for event in kelpy_standard_event_loop(screen, Q, dos):
		
		if timesclicked == CLICK_LIMIT:
			timesclicked = timesclicked+1
			Q.append(obj=img[1], action='swapblink', position=(1000,400), image=target_images_gray[targetidx[0]], period=.5, duration=0, rotation=0, scale=QUAD_IMAGE_SCALE, brightness=1.0 )
			Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))

		

		# If the event is a click:
		if is_click(event) and not Q.commands:
			
				
			# check if each of our images was clicked
			whom = who_was_clicked(dos)
			

			if whom is img[1]:  ## which is the button btw
				if timesclicked > CLICK_LIMIT:
					return "single,"+ str(targetidx[0])
				else:
					timesclicked = timesclicked + 1
					if timesclicked == 1:
						Q.append(obj='sound', file=target_audio[targetidx[0]]) 
					elif timesclicked == 2:
						Q.append(obj='sound', file=target_audio2[targetidx[0]])
					elif timesclicked == 3:
						Q.append(obj='sound', file=target_audio3[targetidx[0]])
					elif timesclicked == 4:
						Q.append(obj='sound', file=target_audio[targetidx[0]]) 
					elif timesclicked == 5:
						Q.append(obj='sound', file=target_audio2[targetidx[0]])
					elif timesclicked == 6:
						Q.append(obj='sound', file=target_audio3[targetidx[0]])
					else:
						pass
					
					Q.append(obj=img[1], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
					Q.append(obj=img[1], action="scale", amount=(1/1.5), duration=1.0)

def present_choice_double(images, rightid, wrongid):
	
	guys = [None, rightid, wrongid]
	img = [None] * 3
	
	## set the image locations
	## Images here are commandable sprites, so we can tell them what to do using Q below
	img[0] = CommandableImageSprite( screen, spot.center, button_image, scale=.5, brightness=.5)
	img[1] = CommandableImageSprite( screen, double_displayat[0], images[rightid], scale=QUAD_IMAGE_SCALE)
	img[2] = CommandableImageSprite( screen, double_displayat[1] , images[wrongid], scale=QUAD_IMAGE_SCALE)
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# Set up the updates, etc. 
	
	# A queue of animation operations
	Q = DisplayQueue()
	
	# Draw a single animation in if you want!
	
	

	# What order do we draw sprites and things in?
	dos = OrderedUpdates(*img) # Draw and update in this order
	
	start_time = time()
	#Q.append(obj='sound', file=kstimulus("sounds/good_job.wav"))  ## This should be changed to play the proper intro sound for the character. right now it just, quite annoyingly, says "Good job!"
	finished = False
	clicked = [0] * 3
	outputString= "double," + str(rightid) + "," + str(wrongid) +  ",("
 	## The standard event loop in kelpy -- this loops infinitely to process interactions
	## and throws events depending on what the user does
	for event in kelpy_standard_event_loop(screen, Q, dos):
		

		# If the event is a click:
		if is_click(event) and not Q.commands:
			if clicked[1] > CLICK_LIMIT and clicked[2] > CLICK_LIMIT:
				return outputString +")"
							# check if each of our images was clicked
			whom = who_was_clicked(dos)
			for i in range(1,3):
				if whom is img[i]:  ## which is the button btw
					if clicked[i] > CLICK_LIMIT:
						pass
					else:
						outputString = outputString+ str(format(guys[i], 'x'))
						clicked[i] = clicked[i] + 1
						if clicked[i] == 1:
							Q.append(obj='sound', file=(target_audio[guys[i]]) )
						elif clicked[i] == 2:
							Q.append(obj='sound', file=(target_audio2[guys[i]]) )
						elif clicked[i] == 3:
							Q.append(obj='sound', file=(target_audio3[guys[i]]) )
						elif clicked[i] == 4:
							Q.append(obj='sound', file=target_audio[guys[i]] ) 
						elif clicked[i] == 5:
							Q.append(obj='sound', file=target_audio2[guys[i]] )
						elif clicked[i] == 6:
							Q.append(obj='sound', file=target_audio3[guys[i]] )
						else:
							pass
						
						
						Q.append(obj=img[i], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
						Q.append(obj=img[i], action="scale", amount=(1/1.5), duration=1.0)
						if clicked[i] == CLICK_LIMIT:
							clicked[i] = clicked[i]+1
							Q.append(obj=img[i], action='swapblink', position=(1000,400), image=target_images_gray[guys[i]], period=.5, duration=0, rotation=0, scale=QUAD_IMAGE_SCALE, brightness=1.0 )
							Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))
#!# Change so that there's only one function!

def present_choice_quadruple(images, rightid, wrong1, wrong2, wrong3):
	

	img = [None] * 5
	guys = [None, rightid, wrong1, wrong2, wrong3]
	## set the image locations
	## Images here are commandable sprites, so we can tell them what to do using Q below
	img[0] = CommandableImageSprite( screen, spot.center, button_image, scale=.5, brightness=.5)
	img[1] = CommandableImageSprite( screen, quadruple_displayat[0], images[rightid], scale=QUAD_IMAGE_SCALE )
	img[2] = CommandableImageSprite( screen, quadruple_displayat[1] , images[wrong1], scale=QUAD_IMAGE_SCALE )
	img[3] = CommandableImageSprite( screen, quadruple_displayat[2], images[wrong2], scale=QUAD_IMAGE_SCALE )
	img[4] = CommandableImageSprite( screen, quadruple_displayat[3], images[wrong3], scale=QUAD_IMAGE_SCALE )

	outputString= "quad," + str(rightid) + "," + str(wrong1) + "," + str(wrong2) + "," + str(wrong3) +  ",("
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# Set up the updates, etc. 
	
	# A queue of animation operations
	Q = DisplayQueue()
	
	# Draw a single animation in if you want!
	
	

	# What order do we draw sprites and things in?
	dos = OrderedUpdates(*img) # Draw and update in this order
	
	start_time = time()
	#Q.append(obj='sound', file=kstimulus("sounds/good_job.wav"))  ## This should be changed to play the proper intro sound for the character. right now it just, quite annoyingly, says "Good job!"
	finished = False
	clicked = [0] * 5

 	## The standard event loop in kelpy -- this loops infinitely to process interactions
	## and throws events depending on what the user does
	for event in kelpy_standard_event_loop(screen, Q, dos):
		

		# If the event is a click:
		if is_click(event) and not Q.commands:
			if clicked[1] > CLICK_LIMIT and clicked[2] > CLICK_LIMIT and clicked [3] > CLICK_LIMIT and clicked[4] > CLICK_LIMIT:
				return outputString + ")"
			# check if each of our images was clicked
			whom = who_was_clicked(dos)
			
			for i in range(1,5):
				if whom is img[i]:  ## which is the button btw
					if clicked[i] > CLICK_LIMIT:
						pass
					else:
						outputString = outputString+ str(format(guys[i], 'x'))
						clicked[i] = clicked[i] + 1
						if clicked[i] == 1:
							Q.append(obj='sound', file=(target_audio[guys[i]]) )
						elif clicked[i] == 2:
							Q.append(obj='sound', file=(target_audio2[guys[i]]) )
						elif clicked[i] == 3:
							Q.append(obj='sound', file=(target_audio3[guys[i]]) )
						elif clicked[i] == 4:
							Q.append(obj='sound', file=target_audio[guys[i]] ) 
						elif clicked[i] == 5:
							Q.append(obj='sound', file=target_audio2[guys[i]] )
						elif clicked[i] == 6:
							Q.append(obj='sound', file=target_audio3[guys[i]] )
						else:
							pass
						
						
						Q.append(obj=img[i], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
						Q.append(obj=img[i], action="scale", amount=(1/1.5), duration=1.0)
						if clicked[i] == CLICK_LIMIT:
							clicked[i] = clicked[i]+1
							Q.append(obj=img[i], action='swapblink', position=(1000,400), image=target_images_gray[guys[i]], period=.5, duration=0, rotation=0, scale=QUAD_IMAGE_SCALE, brightness=1.0 )
							Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))
			
def present_choice_octuple(images, rightid, wrong1, wrong2, wrong3, wrong4, wrong5, wrong6, wrong7):
	

	img = [None] * 9
	
	#!# Maybe call "guys" "image_locations"
	
	guys = [None, rightid, wrong1, wrong2, wrong3, wrong4, wrong5, wrong6, wrong7]
	## set the image locations
	## Images here are commandable sprites, they are displayed in a shuffled order on the screen, but are logged in this order.
	img[0] = CommandableImageSprite( screen, spot.center, button_image, scale=.5, brightness=.5)
	 
	#!# Can rename img[0] to "button" and write the below in a loop
	
	img[1] = CommandableImageSprite( screen, octuple_displayat[0], images[rightid], scale=QUAD_IMAGE_SCALE )
	img[2] = CommandableImageSprite( screen, octuple_displayat[1] , images[wrong1], scale=QUAD_IMAGE_SCALE )
	img[3] = CommandableImageSprite( screen, octuple_displayat[2], images[wrong2], scale=QUAD_IMAGE_SCALE )
	img[4] = CommandableImageSprite( screen, octuple_displayat[3], images[wrong3], scale=QUAD_IMAGE_SCALE )
	img[5] = CommandableImageSprite( screen, octuple_displayat[4], images[wrong4], scale=QUAD_IMAGE_SCALE )
	img[6] = CommandableImageSprite( screen, octuple_displayat[5] , images[wrong5], scale=QUAD_IMAGE_SCALE )
	img[7] = CommandableImageSprite( screen, octuple_displayat[6], images[wrong6], scale=QUAD_IMAGE_SCALE )
	img[8] = CommandableImageSprite( screen, octuple_displayat[7], images[wrong7], scale=QUAD_IMAGE_SCALE )


	outputString= "oct," + str(rightid) + "," + str(wrong1) + "," + str(wrong2) + "," + str(wrong3) +  "," + str(wrong4) + "," + str(wrong5) + "," + str(wrong6) + "," + str(wrong7) +  ",("

	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# Set up the updates, etc. 
	
	# A queue of animation operations
	Q = DisplayQueue()
	
	# Draw a single animation in if you want!
	
	

	# What order do we draw sprites and things in?
	dos = OrderedUpdates(*img) # Draw and update in this order
	
	start_time = time()
	#Q.append(obj='sound', file=kstimulus("sounds/good_job.wav"))  ## This should be changed to play the proper intro sound for the character. right now it just, quite annoyingly, says "Good job!"
	finished = False
	clicked = [0] * 9

 	## The standard event loop in kelpy -- this loops infinitely to process interactions
	## and throws events depending on what the user does
	for event in kelpy_standard_event_loop(screen, Q, dos):
		

		# If the event is a click:
		if is_click(event) and not Q.commands:
			
			#!# if all([x > 3 for x in clicked]):
			if clicked[1] >CLICK_LIMIT and clicked[2] > CLICK_LIMIT and clicked[3] > CLICK_LIMIT and clicked[4] > CLICK_LIMIT and clicked[5] > CLICK_LIMIT and clicked[6] > CLICK_LIMIT and clicked[7] > CLICK_LIMIT and clicked[8] > CLICK_LIMIT:
				return outputString + ")"
			# check if each of our images was clicked
			whom = who_was_clicked(dos)
			
			for i in range(1,9):
				if whom is img[i]:  ## which is the button btw
					if clicked[i] > CLICK_LIMIT:
						pass
					else:
						outputString = outputString+ str(format(guys[i], 'x'))
						clicked[i] = clicked[i] + 1
						if clicked[i] == 1:
							Q.append(obj='sound', file=(target_audio[guys[i]]) )
						elif clicked[i] == 2:
							Q.append(obj='sound', file=(target_audio2[guys[i]]) )
						elif clicked[i] == 3:
							Q.append(obj='sound', file=(target_audio3[guys[i]]) )
						elif clicked[i] == 4:
							Q.append(obj='sound', file=target_audio[guys[i]] ) 
						elif clicked[i] == 5:
							Q.append(obj='sound', file=target_audio2[guys[i]] )
						elif clicked[i] == 6:
							Q.append(obj='sound', file=target_audio3[guys[i]] )
						else:
							pass
						
						
						Q.append(obj=img[i], action="scale", amount=1.5, duration=1.0)  ##append simultaneous doesn't work : (
						Q.append(obj=img[i], action="scale", amount=(1/1.5), duration=1.0)
						if clicked[i] == CLICK_LIMIT:
							clicked[i] = clicked[i]+1
							Q.append(obj=img[i], action='swapblink', position=(1000,400), image=target_images_gray[guys[i]], period=.5, duration=0, rotation=0, scale=QUAD_IMAGE_SCALE, brightness=1.0 )
							Q.append(obj='sound', file=kstimulus('sounds/Cheek-Pop.wav'))
			
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main experiment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	

# Set up images:
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


target_audio = [
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


button_image = kstimulus("shapes/circle_purple.png")

## set up display spots
double_displayat = [ (screen.get_width()/4, 400), ((screen.get_width()/4)*3, 400) ] 
quadruple_displayat= [ ((screen.get_width()/4) + 105, 400), ((screen.get_width()/4)-105, 400),  (((screen.get_width()/4)*3)+105, 400) , (((screen.get_width()/4)*3)-105, 400) ]
octuple_displayat =[ ((screen.get_width()/4) + OCTUPLE_OFFSET, 400-OCTUPLE_OFFSET), ((screen.get_width()/4) + OCTUPLE_OFFSET, 400+OCTUPLE_OFFSET),  ((screen.get_width()/4)-OCTUPLE_OFFSET, 400-OCTUPLE_OFFSET), ((screen.get_width()/4)-OCTUPLE_OFFSET, 400+OCTUPLE_OFFSET),  (((screen.get_width()/4)*3)+OCTUPLE_OFFSET, 400-OCTUPLE_OFFSET) , (((screen.get_width()/4)*3)+OCTUPLE_OFFSET, 400+OCTUPLE_OFFSET), (((screen.get_width()/4)*3)-OCTUPLE_OFFSET, 400-OCTUPLE_OFFSET), (((screen.get_width()/4)*3)-OCTUPLE_OFFSET, 400+OCTUPLE_OFFSET) ]
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

##########################################################################################################################################################3
## finally run the thing, also print the block number, the targetidx, and the index of the correct image. ##Note that this may display duplicates as is.
## the last item is the presen_trial function that actually runs the trial.



seeds = pickrandom(15)
targetidx = randint(0,(len(target_images)-1))
# print "CHOICE SINGLES:"

display_wait_scene()
print present_choice_single(target_images, [ seeds[0] ])
display_naming_scene(screen, target_images, [ seeds[0] ], sixteen_displayat, QUAD_IMAGE_SCALE )
display_wait_scene()

# print "CHOICE DOUBLES:" ################
for block in range(1):	  ########## NOTE: adjust the amount of times this runs a single by adjusting the integer in the parenthesis there <<< --------
	shuffle(double_displayat)
	#print block, filename(target_images[seeds[0]]),filename(target_images[seeds[1]])
	print present_choice_double(target_images, seeds[1], seeds[2] )
display_wait_scene()

display_naming_scene(screen, target_images, seeds[1:3], sixteen_displayat, QUAD_IMAGE_SCALE )

display_wait_scene()
# print "CHOICE QUADRUPLES:" ############################
for block in range(1):	########## NOTE: You can adjust the amount of times this runs  by adjusting the integer in the parenthesis there <<< --------
	
	 #pick some random images to display (by picking random indexes which we'll use to pull things from the array of image locations).
	shuffle(quadruple_displayat)
	#print block, filename(target_images[seeds[0]]),filename(target_images[seeds[1]]), filename(target_images[seeds[2]]), filename(target_images[seeds[3]])
	print present_choice_quadruple(target_images, seeds[3], seeds[4], seeds[5] ,seeds[6] )
	#!# Or: print present_choice_quadruple(target_images, *seeds)
display_wait_scene()

display_naming_scene(screen, target_images, seeds[3:7], sixteen_displayat, QUAD_IMAGE_SCALE )

display_wait_scene()
# print "CHOICE OCTUPLES:"  ################################
for block in range (1):     ########## NOTE: You can adjust the amount of times this runs by adjusting the integer in the parenthesis there <<< --------
	shuffle (octuple_displayat)
	#print block, filename(target_images[seeds[0]]),filename(target_images[seeds[1]]), filename(target_images[seeds[2]]), filename(target_images[seeds[3]]), filename(target_images[seeds[4]]), filename(target_images[seeds[5]]), filename(target_images[seeds[6]]), filename(target_images[seeds[7]]),
	print present_choice_octuple(target_images, seeds[7], seeds[8], seeds[9] ,seeds[10] ,seeds[11] ,seeds[12], seeds[13], seeds[14] )

display_wait_scene()
display_naming_scene(screen, target_images, seeds[7:15], sixteen_displayat, QUAD_IMAGE_SCALE )
display_wait_scene()



seeds = pickrandom(15) ##reshuffle those images.
display_naming_scene(screen, target_images, seeds , sixteen_displayat, QUAD_IMAGE_SCALE)
display_wait_scene()

