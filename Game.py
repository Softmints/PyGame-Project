# Menu system
# Used for starting the game, changing options and
# learning rules of the game

###-----------------------STUFF FOR INITIALISATION START-----------------------###
import sys
import os
import pygame
from workingriverv2 import *
import workingriverv2
import py_compile

py_compile.compile('game.py')

# initialise mixer and assign sound files to variables
pygame.mixer.init(frequency=22050,size=-16,channels=8)
menuclick = pygame.mixer.Sound('click.wav')
horrorloop = pygame.mixer.music.load('horrorloopfade.wav')
pygame.mixer.music.play(-1, 0.0)

#Used for storing user settings on whether to play sound or not
try:
	settings = open('settings.txt', 'r')
	if settings.read() == str(True):
		pygame.mixer.music.set_volume(0.008)
		menuclick.set_volume(0.08)
		settings.close()
	else:
		menuclick.set_volume(0)
		pygame.mixer.music.set_volume(0)
except IOError:
	settings = open('settings.txt', 'w')
	settings.write('True')
	settings.close()

try:
	settings = open('settings_2.txt', 'r')
	if settings.read() == str(True):
		menuclick.set_volume(0.08)
		settings.close()
	else:
		menuclick.set_volume(0)
except IOError:
	settings = open('settings_2.txt', 'w')
	settings.write('True')
	settings.close()

#Booleans for changing menus and determining whether game is being played
playing_game = False
instructions_page = False
options_page = False
main_menu_page = True

# determines help screen
slide_number = 0 

#screen width and height
screen_width = 640
screen_height = 480

# initialise display 640x480 and use background image
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('background.bmp').convert()
screen.blit(background,(0,0))

		###-----------Main Menu images Start-----------###
# Loads start button images and defines position
game_name = pygame.image.load('gamename.png').convert_alpha()
game_name_pos = pygame.Rect(screen_width/2 - 280, 50, 560, 60)
screen.blit(game_name, game_name_pos)

farmer = pygame.image.load('farmer.png').convert_alpha()
farmerPosition = pygame.Rect(100,100,60,75)
farmerPosition2 = pygame.Rect(100,170,60,75)
farmerPosition3 = pygame.Rect(100,240,60,75)

witch = pygame.image.load('witch.png').convert_alpha()
witchPosition = pygame.Rect(35,360,60,75)
screen.blit(witch, witchPosition) #draw the witch

zombie = pygame.image.load('zombie.png').convert_alpha()
zombiePosition = pygame.Rect(screen_width/2 - 37.5 ,360,60,75)
screen.blit(zombie, zombiePosition) #draw the zombie

convict = pygame.image.load('convict.png').convert_alpha()
convictPosition = pygame.Rect(540,360,60,75)
screen.blit(convict, convictPosition) #draw the convict

screen.blit(convict, convictPosition)
screen.blit(zombie, zombiePosition)
screen.blit(witch, witchPosition)

screen.blit(farmer, farmerPosition) #draw the farmer

start = pygame.image.load('start.png').convert_alpha()
start_pressed = pygame.image.load('start_pressed.png').convert_alpha()
start_position = pygame.Rect(screen_width/2 - 173.5, screen_height/2 - 94,347,47)
screen.blit(start, start_position)

options = pygame.image.load('options.png').convert_alpha()
options_pressed = pygame.image.load('options_pressed.png').convert_alpha()
options_position = pygame.Rect(screen_width/2 - 173.5, screen_height/2 - 23.5,347,47)
screen.blit(options, options_position)

htp = pygame.image.load('htp.png').convert_alpha()
htp_pressed = pygame.image.load('htp_pressed.png').convert_alpha()
htp_position = pygame.Rect(screen_width/2 - 173.5, screen_height/2 + 47,347,47)
screen.blit(htp, htp_position)
		###-----------Main Menu images END-------------###

		###-----------GENERAL images Start-----------###
back = pygame.image.load('btm.png').convert_alpha()
back_position = pygame.Rect(550,400, 69, 54)
back_pressed = pygame.image.load('btm_pressed.png').convert_alpha()

options_header = pygame.image.load('optionsheader.png').convert_alpha()
options_header_pos = pygame.Rect(screen_width/2 - 280, 50, 560,60)

htp_header = pygame.image.load('htpheader.png').convert_alpha()
htp_header_pos = pygame.Rect(screen_width/2 - 280, 15, 560,60)

music = pygame.image.load('music.png').convert_alpha()
music_pos = pygame.Rect(screen_width/4 - 280, 150, 560, 60)

sfx = pygame.image.load('sfx.png').convert_alpha()
sfx_pos = pygame.Rect(screen_width/4 - 305, 210, 560, 60)

ison = pygame.image.load('ison.png').convert_alpha()
isoff = pygame.image.load('isoff.png').convert_alpha()
onoff_pos = pygame.Rect(screen_width/4 + 75,150,200,60)

ison_sfx = pygame.image.load('ison.png').convert_alpha()
isoff_sfx = pygame.image.load('isoff.png').convert_alpha()
onoff_sfx_pos = pygame.Rect(screen_width/4 + 75,210,300,60)

back_slide = pygame.image.load('back.png').convert_alpha()
back_slide_pressed = pygame.image.load('back_pressed.png').convert_alpha()
back_slide_pos = pygame.Rect(screen_width/4 - 150, 60, 200, 60)

next = pygame.image.load('next.png').convert_alpha()
next_pressed = pygame.image.load('next_pressed.png').convert_alpha()
next_pos = pygame.Rect(screen_width/4 + 275, 60, 200, 60)

slide_1 = pygame.image.load('slide_1.png').convert_alpha()
slide_2 = pygame.image.load('slide_2.png').convert_alpha()
slide_3 = pygame.image.load('slide_3.png').convert_alpha()
slide_4 = pygame.image.load('slide_4.png').convert_alpha()
slide_pos = pygame.Rect(0,100, 200, 60)
		###-----------GENERAL images END-------------###
###-----------------------STUFF FOR INITIALISATION END-------------------------###


###-----------------------MAIN FUNCTION START----------------------------------###
def main2():

	if playing_game == False:
		if instructions_page == False and main_menu_page == True and options_page == False:
			main_menu()

		if instructions_page == False and main_menu_page == False and options_page == True:
			options_screen()

		if instructions_page == True and main_menu_page == False and options_page == False:
			how_to_play()
	else:
		workingriverv2.main()
###-----------------------MAIN FUNCTION END------------------------------------###


###-----------------------MAIN_MENU START--------------------------------------###
def main_menu():
	# Gain access to global variables
	global main_menu_page
	global instructions_page
	global options_page
	global playing_game

	# sanity check
	run_once = True

	if mouse_x >= 146 and (mouse_x <= 493) and  main_menu_page == True:
		if mouse_y >= 146 and (mouse_y <= 193):
			if mouse_down[0]:
				print "hi"
				print playing_game
				playing_game = True
				pygame.mixer.Sound.play(menuclick)
			while run_once == True:
				# change the colour of the button
				screen.blit(background,(0,0))
				screen.blit(farmer, farmerPosition)
				screen.blit(game_name, game_name_pos)
				screen.blit(options, options_position)
				screen.blit(htp, htp_position)
				screen.blit(start_pressed, start_position)
				screen.blit(convict, convictPosition)
				screen.blit(zombie, zombiePosition)
				screen.blit(witch, witchPosition)
				# stop the screen from drawing loads of images
				run_once = not run_once

		#if mouse over these coords change button colour
		#if player clicks, take them to the options page
		elif mouse_y >= 216.5 and (mouse_y <=263.5):
			if mouse_down[0]:
				pygame.mixer.Sound.play(menuclick)
				main_menu_page = False
				options_page = True
				options_screen()
			while run_once == True:
				screen.blit(background,(0,0))
				screen.blit(farmer, farmerPosition2)
				screen.blit(game_name, game_name_pos)
				screen.blit(start, start_position)
				screen.blit(htp, htp_position)
				screen.blit(options_pressed, options_position)
				screen.blit(convict, convictPosition)
				screen.blit(zombie, zombiePosition)
				screen.blit(witch, witchPosition)
				run_once = not run_once

		#if mouse over these coords change button colour
		#if player clicks, take them to the How to Play page
		elif mouse_y >= 287 and (mouse_y <= 334):
			if mouse_down[0]:
				pygame.mixer.Sound.play(menuclick)
				main_menu_page = False
				instructions_page = True
				how_to_play()
			while run_once == True:
				screen.blit(background, (0,0))
				screen.blit(farmer, farmerPosition3)
				screen.blit(game_name, game_name_pos)
				screen.blit(start, start_position)
				screen.blit(options, options_position)
				screen.blit(htp_pressed, htp_position)
				screen.blit(convict, convictPosition)
				screen.blit(zombie, zombiePosition)
				screen.blit(witch, witchPosition)
				run_once = not run_once
		else:
			# set button colour to default if not between y coords
			# of any button on main screen (erase)
#			run_once = True
			screen.blit(background, (0,0))
			screen.blit(game_name, game_name_pos)
			screen.blit(start, start_position)
			screen.blit(options, options_position)
			screen.blit(htp, htp_position)
			screen.blit(witch, witchPosition)
			screen.blit(zombie, zombiePosition)
			screen.blit(convict, convictPosition)
	else:
		# set button colour to default if not between x coords
		# of any button on main screen
		# Also re-draws the screen when coming back from another page (erase)
#		run_once = True
		screen.blit(background,(0,0))
		screen.blit(game_name, game_name_pos)
		screen.blit(start, start_position)
		screen.blit(options, options_position)
		screen.blit(htp, htp_position)
		screen.blit(witch, witchPosition)
		screen.blit(zombie, zombiePosition)
		screen.blit(convict, convictPosition)
###-----------------------MAIN MENU FUNCTION END-------------------------------###



###-----------------------HOW TO PLAY FUNCTION START---------------------------###
def how_to_play():

	global main_menu_page
	global instructions_page
	global slide_number
	run_once = True

	screen.blit(background,(0,0))
	screen.blit(back, back_position)
	screen.blit(htp_header, htp_header_pos)

	screen.blit(next, next_pos)
	screen.blit(back_slide, back_slide_pos)

	screen.blit(slide_1, slide_pos)	

	if mouse_x >= 550 and (mouse_x <= 619):
		if mouse_y >= 400 and (mouse_y <= 454):
			if mouse_down[0]:
				pygame.mixer.Sound.play(menuclick)
				print "You've gone back"		#FOR DEBUGGING REMEMBER TO REMOVE
				instructions_page = False
				main_menu_page = True
				main_menu()
			while run_once == True:
				screen.blit(background,(0,0))
				screen.blit(back_pressed, back_position)
				screen.blit(htp_header, htp_header_pos)
				screen.blit(next, next_pos)
				screen.blit(back_slide, back_slide_pos)

				run_once = not run_once
		else:
			screen.blit(background, (0,0))
			screen.blit(back, back_position)
			screen.blit(htp_header, htp_header_pos)
			screen.blit(next, next_pos)
			screen.blit(back_slide, back_slide_pos)
	else:
		screen.blit(background, (0,0))
		screen.blit(back, back_position)
		screen.blit(htp_header, htp_header_pos)
		screen.blit(next, next_pos)
		screen.blit(back_slide, back_slide_pos)

	# takes user back to previous help slide
	if mouse_x >= 60 and (mouse_x <= 150):
		if mouse_y >= 60 and (mouse_y <=120):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					pygame.mixer.Sound.play(menuclick)
					slide_number -=1
					if slide_number <=0:
						slide_number = 0
					print slide_number
			screen.blit(background, (0,0))	# erase and draw everything again
			screen.blit(back_slide_pressed, back_slide_pos)
			screen.blit(back, back_position)
			screen.blit(htp_header, htp_header_pos)
			screen.blit(next, next_pos)

	# takes user to next help slide
	if mouse_x >= 490 and (mouse_x<= 570):
		if mouse_y >= 60 and (mouse_y <= 120):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					pygame.mixer.Sound.play(menuclick)
					slide_number +=1
					if slide_number >=3:
						slide_number = 3
					print slide_number
			screen.blit(background, (0,0))	#erase and draw everything again
			screen.blit(back_slide, back_slide_pos)
			screen.blit(back, back_position)
			screen.blit(htp_header, htp_header_pos)
			screen.blit(next_pressed, next_pos)

	if slide_number == 0:
		screen.blit(slide_1,(slide_pos))

	if slide_number == 1:
		screen.blit(slide_2,(slide_pos))

	if slide_number == 2:
		screen.blit(slide_3,(slide_pos))

	if slide_number == 3:
		screen.blit(slide_4,(slide_pos))

###-----------------------HOW TO PLAY FUNCTION END-----------------------------###


###----------------------OPTIONS_SCREEN FUNCTION START-------------------------###
def options_screen():

	global main_menu_page
	global options_page

	run_once = True

	screen.blit(background,(0,0))
	screen.blit(back, back_position)
	screen.blit(options_header, options_header_pos)	
	screen.blit(music, music_pos)
	screen.blit(sfx, sfx_pos)
	screen.blit(ison_sfx, onoff_sfx_pos)
#	screen.blit(text,[320,50])

	if mouse_x >= 550 and (mouse_x <= 619):
		if mouse_y >= 400 and (mouse_y <= 454):
			if mouse_down[0]:
				pygame.mixer.Sound.play(menuclick)
				options_page = False
				main_menu_page = True
				main_menu()
			while run_once == True:
				screen.blit(background,(0,0))
				screen.blit(back_pressed, back_position)
				screen.blit(options_header, options_header_pos)
				screen.blit(music, music_pos)
				screen.blit(sfx, sfx_pos)
				screen.blit(ison_sfx, onoff_sfx_pos)
				run_once = not run_once
		else:
			run_once = True
			screen.blit(background, (0,0))
			screen.blit(back, back_position)
			screen.blit(options_header, options_header_pos)
			screen.blit(music, music_pos)
			screen.blit(sfx, sfx_pos)
			screen.blit(ison_sfx, onoff_sfx_pos)
	else:
		run_once = True


	# controls settings for audio playback
	if mouse_x >= 235 and (mouse_x <= 435):
		if mouse_y >= 150 and (mouse_y <= 210):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					pygame.mixer.Sound.play(menuclick)
					settings = open('settings.txt', 'r')
					if settings.read() == str(True):
						screen.blit(ison, onoff_pos)
						pygame.display.update()			
						settings.close()
						settings = open('settings.txt', 'w')
						settings.write('False')
						settings.close()
					else:
						screen.blit(isoff, onoff_pos)
						pygame.display.update()
						settings.close()
						settings = open('settings.txt', 'w')
						settings.write('True')
						settings.close()
						setting = open('settings.txt', 'r')

		elif mouse_y >=210 and (mouse_y <= 270):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					pygame.mixer.Sound.play(menuclick)
					settings = open('settings_2.txt', 'r')
					if settings.read() == str(True):
						screen.blit(ison_sfx, onoff_sfx_pos)
						pygame.display.update()			
						settings.close()
						settings = open('settings_2.txt', 'w')
						settings.write('False')
						settings.close()
					else:
						screen.blit(isoff_sfx, onoff_sfx_pos)
						pygame.display.update()
						settings.close()
						settings = open('settings_2.txt', 'w')
						settings.write('True')
						settings.close()
						setting = open('settings_2.txt', 'r')




	settings = open('settings.txt', 'r') 
	if settings.read() == str(True):
		screen.blit(ison, onoff_pos)
		pygame.mixer.music.set_volume(0.008)
		menuclick.set_volume(0.08)
	else:
		screen.blit(isoff, onoff_pos)
		menuclick.set_volume(0)
		pygame.mixer.music.set_volume(0)

	settings_2 = open('settings_2.txt', 'r') 
	if settings_2.read() == str(True):
		screen.blit(ison_sfx, onoff_sfx_pos)
		menuclick.set_volume(0.08)
	else:
		screen.blit(isoff_sfx, onoff_sfx_pos)
		menuclick.set_volume(0)
###----------------------OPTIONS_SCREEN FUNCTION END---------------------------###


###-----------------------------EXECUTE PROGRAM--------------------------------###
while 1:
	# is mouse button x down
	mouse_down = pygame.mouse.get_pressed()

	# pygame.mouse.get_pos() returns two values: x and y
	mouse_x, mouse_y = pygame.mouse.get_pos()
	
	#REMEMBER TO INCLUDE UPDATE!
	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				run = False
				sys.exit()

	main2()
