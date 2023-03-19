import pygame
from pygame.locals import *
import time
import random 

from .load import *
from .music import *

background_over = pygame.image.load("assets/overbackground.png")

class Menu:
    def print_menu(screen):
        screen.blit(Load.menu, [1180, 0])

    def click_menu(screen):
        Chomp.print_counter(screen)
        
    def print_speed(screen):
        Chomp.print_speed(screen)

class Action(object):
    atemoney = 0
    thisblob = Load.blob
    whichmoney = 1
    movementboost = 0.5

class Player_Positions(object):
    x = 20
    y = 450

class Money_Positions(object):
    x = 300
    y = 470

class Chomp:
    def print_counter(screen):
        font = pygame.font.Font(None, 100)
        counter = font.render("Points: " + str(Action.atemoney), True, 'White')
        screen.blit(counter, [0, 0])
    
    def print_speed(screen):
        font = pygame.font.Font(None, 100)
        speed = font.render("Normal", True, 'White')
        if Action.whichmoney == 1:
                speed = font.render("Speed: Normal", True, 'White')
        elif Action.whichmoney == 2:
                speed = font.render("Speed: Fast", True, 'Purple')
        elif Action.whichmoney == 3:
                speed = font.render("Speed: Slow", True, 'Green')
        screen.blit(speed, [0, 80])
        

    def eat(screen):
        if (Money_Positions.x>=Player_Positions.x-100 and Money_Positions.x<=Player_Positions.x+250) and (Money_Positions.y>=Player_Positions.y and Money_Positions.y<=Player_Positions.y+215):
            Play.play_chomp()
            Money_Positions.y = 470
            while Money_Positions.x>=Player_Positions.x-100 and Money_Positions.x<=Player_Positions.x+150:
                Money_Positions.x = random.randint(20, 1000)
            up = random.randint(0, 1)
            if up==1:
                Money_Positions.y -= random.randint(100, 200)
            Action.atemoney += 1
            if Action.whichmoney == 1:
                Action.movementboost = 0.5
            elif Action.whichmoney == 2:
                Action.movementboost = 0.25
            elif Action.whichmoney == 3:
                Action.movementboost = 0.75
            Action.whichmoney = random.choice([1, 2, 3])

class Movement:
    def jump(screen, background_image, print_the_menu):
        Play.play_jump()
        saveblob = Action.thisblob
        if saveblob == Load.blob:
            Action.thisblob = Load.BlobJumpSus
        else:
            Action.thisblob = Load.BlobJumpSus2
        for i in range(200):
            Player_Positions.y -= 1
            if i%50==0:
                screen.blit(background_image, [0, 0])
                if Action.whichmoney == 1:
                    screen.blit(Load.money, [Money_Positions.x, Money_Positions.y])
                    screen.blit(background_over, [0, 0])
                elif Action.whichmoney == 2:
                    screen.blit(Load.money2, [Money_Positions.x, Money_Positions.y])
                    screen.blit(background_over, [0, 0])
                elif Action.whichmoney == 3:
                    screen.blit(Load.money3, [Money_Positions.x, Money_Positions.y])
                    screen.blit(background_over, [0, 0])
                Menu.print_menu(screen)
                
                screen.blit(Action.thisblob, (Player_Positions.x, Player_Positions.y))
                screen.blit(background_over, [0, 0])
                if print_the_menu==1:
                    Menu.click_menu(screen)
                    Menu.print_speed(screen)
                if print_the_menu==0:
                    Menu.print_menu(screen)
                pygame.display.flip()
                time.sleep(0.1)

        Chomp.eat(screen)

        if saveblob == Load.blob:
            Action.thisblob = Load.BlobJumpJos
        else:
            Action.thisblob = Load.BlobJumpJos2
            
        for i in range(200):
            Player_Positions.y += 1
            if i%50==0:
                screen.blit(background_image, [0, 0])
                if Action.whichmoney == 1:
                    screen.blit(Load.money, [Money_Positions.x, Money_Positions.y])
                    screen.blit(background_over, [0, 0])
                elif Action.whichmoney == 2:
                    screen.blit(Load.money2, [Money_Positions.x, Money_Positions.y])
                    screen.blit(background_over, [0, 0])
                elif Action.whichmoney == 3:
                    screen.blit(Load.money3, [Money_Positions.x, Money_Positions.y])
                    screen.blit(background_over, [0, 0])
                Menu.print_menu(screen)
                screen.blit(Action.thisblob, (Player_Positions.x, Player_Positions.y))
                screen.blit(background_over, [0, 0])
                if print_the_menu==1:
                    Menu.click_menu(screen)
                    Menu.print_speed(screen)
                if print_the_menu==0:
                    Menu.print_menu(screen)
                pygame.display.flip()
                time.sleep(0.1)
        Action.thisblob = saveblob

    def left(screen):
        Play.play_movement()
        Player_Positions.x -= 50
        Action.thisblob = Load.BlobZdrobit
        screen.blit(Action.thisblob, (Player_Positions.x, Player_Positions.y))
        screen.blit(background_over, [0, 0])
        pygame.display.flip()
        Action.thisblob = Load.blob2
        time.sleep(Action.movementboost)

    def right(screen):
        Play.play_movement()
        Player_Positions.x += 50
        Action.thisblob = Load.BlobZdrobit2
        screen.blit(Action.thisblob, (Player_Positions.x, Player_Positions.y))
        screen.blit(background_over, [0, 0])
        pygame.display.flip()
        Action.thisblob = Load.blob
        time.sleep(Action.movementboost)