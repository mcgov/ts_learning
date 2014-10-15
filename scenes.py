import os, sys
import pygame
from random import randint, choice, sample, shuffle
from kelpy.CommandableImageSprite import *
from kelpy.Miscellaneous import *
from kelpy.DisplayQueue import *
from kelpy.OrderedUpdates import *
from kelpy.EventHandler import *


def display_naming_scene( screen, images, seeds , sixteen_displayat, SCALE):
	
	

	faudio = os.path.dirname( __file__ )+"stimuli/audio/find/"  ##This returns the filepath relative to this file. We're loading a bunch of things from the stimuli folder.

	find_audio =[
	faudio+"find_beppo.wav",
	faudio+"find_deela.wav",
	faudio+"find_finna.wav",
	faudio+"find_guffi.wav",
	faudio+"find_higoo.wav",
	faudio+"find_kogay.wav",
	faudio+"find_lahdo.wav",
	faudio+"find_mobi.wav",
	faudio+"find_nadoo.wav",
	faudio+"find_pavy.wav",
	faudio+"find_roozy.wav",
	faudio+"find_soma.wav",
	faudio+"find_tibble.wav",
	faudio+"find_vaylo.wav",
	faudio+"find_zefay.wav"
	]

	transparent_button = os.path.dirname( __file__ )+"/stimuli/transparent.png"
	img = [None] * 16


	img[0] = CommandableImageSprite( screen, (0,0), transparent_button, scale=1.0)
	img[1] = CommandableImageSprite( screen, sixteen_displayat[0], images[0], scale=SCALE )
	img[2] = CommandableImageSprite( screen, sixteen_displayat[1] , images[1], scale=SCALE )
	img[3] = CommandableImageSprite( screen, sixteen_displayat[2], images[2], scale=SCALE )
	img[4] = CommandableImageSprite( screen, sixteen_displayat[3], images[3], scale=SCALE )
	img[5] = CommandableImageSprite( screen, sixteen_displayat[4], images[4], scale=SCALE )
	img[6] = CommandableImageSprite( screen, sixteen_displayat[5] , images[5], scale=SCALE )
	img[7] = CommandableImageSprite( screen, sixteen_displayat[6], images[6], scale=SCALE )
	img[8] = CommandableImageSprite( screen, sixteen_displayat[7], images[7], scale=SCALE )
	img[9] = CommandableImageSprite( screen, sixteen_displayat[8], images[8], scale=SCALE )
	img[10] = CommandableImageSprite( screen, sixteen_displayat[9] , images[9], scale=SCALE )
	img[11] = CommandableImageSprite( screen, sixteen_displayat[10], images[10], scale=SCALE )
	img[12] = CommandableImageSprite( screen, sixteen_displayat[11], images[11], scale=SCALE )
	img[13] = CommandableImageSprite( screen, sixteen_displayat[12], images[12], scale=SCALE )
	img[14] = CommandableImageSprite( screen, sixteen_displayat[13] , images[13], scale=SCALE )
	img[15] = CommandableImageSprite( screen, sixteen_displayat[14], images[14], scale=SCALE )
	
	Q = DisplayQueue()
	

	dos = OrderedUpdates(img)
	
	finished = False
	clicked = 0
	raynj = None
	pickthisone = None
	if isinstance( seeds, int ):
		raynj = seeds
		pickthisone = raynj
	elif isinstance( seeds , list):
		raynj = len(seeds)-1
		pickthisone = seeds[randint(0, raynj )]
	else:
		return "We experienced a problem!"
	Q.append(obj='sound', file= find_audio[pickthisone])
	for event in kelpy_standard_event_loop(screen, Q, dos):
		
		# if time()-start_time > MAX_DISPLAY_TIME:
		# 	pass

		# If the event is a click:
		if is_click(event):
			if finished:
				break
			# check if each of our images was clicked
			whom = who_was_clicked(dos)
					
			if whom is img[0]:  ## which is our hidden button
				clicked+=1
				if clicked >1:
					finished  = True


