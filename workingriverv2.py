#!/usr/bin/env python
# encoding: utf-8


import sys
import os
import pygame


RIGHT = 1
STOP = 0
LEFT = -1


screen_width = 640
screen_height = 480


def main():

    gameover = False
    screen = pygame.display.set_mode((screen_width, screen_height))
    background = pygame.image.load('game_background.jpg').convert()
    screen.blit(background, (0, 0)) #draw the background screen
    
    farmer = pygame.image.load('farmer.png').convert_alpha()
    farmerPosition = pygame.Rect(30,10,60,75)
    screen.blit(farmer, farmerPosition) #draw the farmer

    zombie = pygame.image.load('zombie.png').convert_alpha()
    zombiePosition = pygame.Rect(30,110,60,75)
    screen.blit(zombie, zombiePosition) #draw the zombie
    

    convict = pygame.image.load('convict.png').convert_alpha()
    convictPosition = pygame.Rect(35,250,60,75)
    screen.blit(convict, convictPosition) #draw the convict

    witch = pygame.image.load('witch.png').convert_alpha()
    witchPosition = pygame.Rect(35,360,60,75)
    screen.blit(witch, witchPosition) #draw the witch

#    Lose = pygame.image.load('start.bmp').convert() 
    Win = pygame.image.load('winner.png').convert_alpha()
    lose = pygame.image.load('lose.png').convert_alpha()
    winlose_pos = pygame.Rect(screen_width/2 - 280, screen_height/4 - 30, 560, 60)

    menu_return = pygame.image.load('menureturn.png').convert_alpha()
    menu_return_pressed = pygame.image.load('menureturn_pressed.png').convert_alpha()
    menu_pos = pygame.Rect(screen_width/2 - 280, 250, 560, 60)

    restart = pygame.image.load('restart.png').convert_alpha()
    restart_pressed = pygame.image.load('restart_pressed.png').convert_alpha()
    restart_pos = pygame.Rect(screen_width/2 - 280, 200 , 560, 60)


    pygame.display.set_caption("Halloween River Crossing")


    pygame.display.update() #display all elements

    move = STOP
    zombiemove = STOP
    convictmove = STOP
    witchmove = STOP
    while 1:
       for event in pygame.event.get():
          if event.type == pygame.QUIT:
             sys.exit()
          elif event.type == pygame.KEYDOWN:
				# Check for key press
              if event.key == pygame.K_q:
				  # if key pressed is 'f' key, move farmer (check if moving from left to right or other way)
                if move == STOP and farmerPosition.left > 300:
                      move = LEFT
                elif move == STOP and farmerPosition.left < 300:
                      move = RIGHT
              elif event.key == pygame.K_w:
                if move == STOP and farmerPosition.left > 300:
                      move = LEFT
                elif move == STOP and farmerPosition.left < 300:
                      move = RIGHT
                if zombiemove == STOP and zombiePosition.left >= 515 and farmerPosition.left >= 515:
                      zombiemove = LEFT
                elif zombiemove == STOP and zombiePosition.left <= 30 and farmerPosition.left <= 30:
                      zombiemove = RIGHT
              elif event.key == pygame.K_e:
                if move == STOP and farmerPosition.left > 300:
                      move = LEFT
                elif move == STOP and farmerPosition.left < 300:
                      move = RIGHT
                if convictmove == STOP and convictPosition.left >= 515 and farmerPosition.left >= 515:
                      convictmove = LEFT
                elif convictmove == STOP and convictPosition.left <= 35 and farmerPosition.left <= 30:
                      convictmove = RIGHT
              elif event.key == pygame.K_r:
                if move == STOP and farmerPosition.left > 300:
                      move = LEFT
                elif move == STOP and farmerPosition.left < 300:
                      move = RIGHT
                if witchmove == STOP and witchPosition.left >= 515 and farmerPosition.left >= 515:
                      witchmove = LEFT
                elif witchmove == STOP and witchPosition.left <= 35 and farmerPosition.left <= 30:
                      witchmove = RIGHT 
       mouse_x, mouse_y = pygame.mouse.get_pos()
       screen.blit(background, farmerPosition, farmerPosition) # erase
       if (move == RIGHT):
           if (farmerPosition.left <= (550 - 30)) and gameover == False:
               farmerPosition = farmerPosition.move(9, 0) # move farmer
           else:
               move = STOP
       if (move == LEFT):
           if (farmerPosition.left >= (30)) and gameover == False:
               farmerPosition = farmerPosition.move(-9, 0) # move farmer
           else:
               move = STOP
       screen.blit(farmer, farmerPosition) # draw new farmer
       pygame.display.update()  # and show it all
       pygame.time.delay(10)  # stop the program for 1/100 second

       screen.blit(background, zombiePosition, zombiePosition) # erase
       if (zombiemove == RIGHT):
           if (zombiePosition.left <= (550 - 30)) and gameover == False:
               zombiePosition = zombiePosition.move(9, 0) # move farmer
           else:
               zombiemove = STOP
       if (zombiemove == LEFT):
           if (zombiePosition.left >= (30)) and gameover == False:
              zombiePosition = zombiePosition.move(-9, 0) # move farmer
           else:
              zombiemove = STOP
       screen.blit(zombie, zombiePosition) # draw new farmer
       pygame.display.update()  # and show it all
       pygame.time.delay(10)  # stop the program for 1/100 second

       screen.blit(background, convictPosition, convictPosition) # erase
       if (convictmove == RIGHT):
           if (convictPosition.left <= (550 - 30)) and gameover == False:
               convictPosition = convictPosition.move(9, 0) # move farmer
           else:
               convictmove = STOP
       if (convictmove == LEFT):
           if (convictPosition.left >= (35)) and gameover == False:
              convictPosition = convictPosition.move(-9, 0) # move farmer
           else:
              convictmove = STOP
       screen.blit(convict, convictPosition) # draw new farmer
       pygame.display.update()  # and show it all
       pygame.time.delay(10)  # stop the program for 1/100 second

       screen.blit(background, witchPosition, witchPosition) # erase
       if (witchmove == RIGHT):
           if (witchPosition.left <= (550 - 30)) and gameover == False:
               witchPosition = witchPosition.move(9, 0) # move farmer
           else:
               witchmove = STOP
       if (witchmove == LEFT):
           if (witchPosition.left >= (35)) and gameover == False:
              witchPosition = witchPosition.move(-9, 0) # move farmer
           else:
              witchmove = STOP
       screen.blit(witch, witchPosition) # draw new farmer
       pygame.display.update()  # and show it all
       pygame.time.delay(10)  # stop the program for 1/100 second
              
       
       # Win
       if farmerPosition.left >= 515 and zombiePosition.left >= 515 and convictPosition.left >= 515 and witchPosition.left >= 515:
        gameover = True
        screen.blit(Win, winlose_pos)
        screen.blit(restart, restart_pos)
        screen.blit(menu_return, menu_pos)
        pygame.display.update()
        if mouse_x >= 40 and (mouse_x <=600):
          if mouse_y >= 200 and (mouse_y <= 245):
            screen.blit(restart_pressed, restart_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
              main()
          elif mouse_y >= 250 and (mouse_y <= 310):
            screen.blit(menu_return_pressed, menu_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
              pygame.quit()
              sys.exit()
          else:
            screen.blit(restart, restart_pos)
            screen.blit(menu_return, menu_pos)
        else:
          screen.blit(restart, restart_pos)
          screen.blit(menu_return, menu_pos)

       # zombie and convict together Left
       elif farmerPosition.left >= 515 and zombiePosition.left <= 30 and convictPosition.left <= 35 and witchPosition.left >= 515:
        gameover = True
        screen.blit(lose, winlose_pos)
        screen.blit(restart, restart_pos)
        screen.blit(menu_return, menu_pos)
        pygame.display.update()
#        pygame.time.delay(2500)
        if mouse_x >= 40 and (mouse_x <=600):
          if mouse_y >= 200 and (mouse_y <= 245):
            screen.blit(restart_pressed, restart_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
              main()
          elif mouse_y >= 250 and (mouse_y <= 310):
            screen.blit(menu_return_pressed, menu_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
              pygame.quit()
              sys.exit()
          else:
            screen.blit(restart, restart_pos)
            screen.blit(menu_return, menu_pos)
        else:
          screen.blit(restart, restart_pos)
          screen.blit(menu_return, menu_pos)
       # zombie and convict together Right
       elif farmerPosition.left <= 100 and zombiePosition.left >= 515 and convictPosition.left >= 515 and witchPosition.left <= 515:
        gameover = True
        screen.blit(lose, winlose_pos)
        pygame.display.update()
        screen.blit(restart, restart_pos)
        screen.blit(menu_return, menu_pos)
#        pygame.time.delay(2500)
        if mouse_x >= 40 and (mouse_x <=600):
          if mouse_y >= 200 and (mouse_y <= 245):
            screen.blit(restart_pressed, restart_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
              main()
          elif mouse_y >= 250 and (mouse_y <= 310):
            screen.blit(menu_return_pressed, menu_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
              pygame.quit()
              sys.exit()
          else:
            screen.blit(restart, restart_pos)
            screen.blit(menu_return, menu_pos)
        else:
          screen.blit(restart, restart_pos)
          screen.blit(menu_return, menu_pos)

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            main()
          else:
            pygame.quit()
            sys.exit()
       # witch and convict together Left
       elif farmerPosition.left >= 515 and zombiePosition.left >= 515 and convictPosition.left <= 35 and witchPosition.left <= 35:
        gameover = True
        screen.blit(lose, winlose_pos)
        screen.blit(restart, restart_pos)
        screen.blit(menu_return, menu_pos)
        pygame.display.update()
#        pygame.time.delay(2500)
        if mouse_x >= 40 and (mouse_x <=600):
          if mouse_y >= 200 and (mouse_y <= 245):
            screen.blit(restart_pressed, restart_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
              main()
          elif mouse_y >= 250 and (mouse_y <= 310):
            screen.blit(menu_return_pressed, menu_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
              pygame.quit()
              sys.exit()
          else:
            screen.blit(restart, restart_pos)
            screen.blit(menu_return, menu_pos)
        else:
          screen.blit(restart, restart_pos)
          screen.blit(menu_return, menu_pos)
       # witch and convict together Right
       elif farmerPosition.left <= 30 and zombiePosition.left <= 30 and convictPosition.left >= 515 and witchPosition.left >= 515:
        gameover = True
        screen.blit(lose, winlose_pos)
        screen.blit(restart, restart_pos)
        screen.blit(menu_return, menu_pos)
        pygame.display.update()
#        pygame.time.delay(2500)
        if mouse_x >= 40 and (mouse_x <=600):
          if mouse_y >= 200 and (mouse_y <= 245):
            screen.blit(restart_pressed, restart_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
              main()
          elif mouse_y >= 250 and (mouse_y <= 310):
            screen.blit(menu_return_pressed, menu_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
              pygame.quit()
              sys.exit()
          else:
            screen.blit(restart, restart_pos)
            screen.blit(menu_return, menu_pos)
        else:
          screen.blit(restart, restart_pos)
          screen.blit(menu_return, menu_pos)


if __name__ == '__main__':
    main()

