# Importing libraries
from typing import List, Any

import pygame as pg
import time
import numpy as np
import random
from pygame.locals import *

# Initiating functions
pg.init()
pg.display.init()
pg.mixer.init()


class Obj:
    # An class that will create the objects that will be visible on the screen
    def __init__(self, xpos: int, ypos: int, currenttexture: object, visible: bool):
        """

        Parameters
        ----------
        xpos - int
        ypos - int
        currenttexture - pygame.surface
        visible - bool
        """
        self.x = xpos
        self.y = ypos
        self.texture = currenttexture
        self.visible = visible
        self.Rect = pg.Rect((xpos, ypos), (229, 394))
        Obj.List.append(self)

    List = []

    def blit(self):
        # display the object on the screen on the corresponding positions and texture
        screen.blit(self.texture, (self.x, self.y))


def finishRound():
    # TODO: Add a scoreboard that measures the win/lose ratio, and display it to the screen
    print(chosenDoor[1])
    if chosenDoor[1] == 0:
        if doors[0]:
            door0.texture = carDoorImg
        elif doors[1]:
            door1.texture = carDoorImg
        elif doors[2]:
            door2.texture = carDoorImg
        else:
            print("Error0")
    elif chosenDoor[1] == 1:
        if doors[0]:
            door0.texture = carDoorImg
        elif doors[1]:
            door1.texture = carDoorImg
        elif doors[2]:
            door2.texture = carDoorImg
        else:
            print("Error1")
    elif chosenDoor[1] == 2:
        if doors[0]:
            door0.texture = carDoorImg
        elif doors[1]:
            door1.texture = carDoorImg
        elif doors[2]:
            door2.texture = carDoorImg
        else:
            print("Error2")
    else:
        print("Errorrrrr")


# Defining constants
WIDTH, HEIGHT = (1280, 720)
SIZE = (WIDTH, HEIGHT)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen settings
screen = pg.display.set_mode(size=SIZE)
pg.display.set_caption("Monty Hall")

# Loading assets
closedDoorImg = pg.image.load("Data/Assets/Images/closedDoor0.jpg")
openedDoorImg = pg.image.load("Data/Assets/Images/openedDoor0.jpg")
goatDoorImg = pg.image.load("Data/Assets/Images/GoatDoor0.jpg")
carDoorImg = pg.image.load("Data/Assets/Images/CarDoor0.jpg")
openDoorSound = pg.mixer.Sound("Data/Assets/Sounds/doorOpen0.wav")

# resizing the images
# closedDoorImgSize = closedDoorImg.get_rect().size  NOT NEEDED
closedDoorImgSize = np.asarray((229, 394))
openedDoorImgSize = np.asarray((229, 394))
goatDoorImgSize = np.asarray((229, 394))
carDoorImgSize = np.asarray((229, 394))
# print(closedDoorImgSize)
closedDoorImg = pg.transform.scale(closedDoorImg, closedDoorImgSize)
openedDoorImg = pg.transform.scale(openedDoorImg, openedDoorImgSize)
goatDoorImg = pg.transform.scale(goatDoorImg, goatDoorImgSize)
carDoorImg = pg.transform.scale(carDoorImg, carDoorImgSize)

door0 = Obj(150, 30, closedDoorImg, True)
door1 = Obj(550, 30, closedDoorImg, True)
door2 = Obj(950, 30, closedDoorImg, True)
chosenDoor = [False, 0]

doors = [False, True, False]
random.shuffle(doors)
print(doors)

while True:
    screen.fill(WHITE)
    for i in Obj.List:
        i.blit()
    largeText = pg.font.Font('freesansbold.ttf', 115)
    switchButton = pg.Rect(75, 500, 400, 150)
    dontSwitchButton = pg.Rect(805, 500, 400, 150)
    pg.draw.rect(screen, GREEN, switchButton)
    pg.draw.rect(screen, RED, dontSwitchButton)
    pg.draw.line(screen, BLACK, (0, 0), (150, 30))
    pg.display.flip()
    for event in pg.event.get():
        # Check if the mouse is clicked down and it's position
        if event.type == pg.MOUSEBUTTONDOWN:
            mousePos = pg.mouse.get_pos()
            # Check for the position of the mouse relative to the current game state and it's buttons
            if chosenDoor[0]:
                # noinspection PyArgumentList,PyArgumentList
                if pg.Rect.collidepoint(switchButton, mousePos):
                    # Check for the clicking on the switch button, then check for which door was pressed,
                    # and then check if the chosen door had the car or the goat
                    print("switch button pressed")
                    print(chosenDoor[1])
                    finishRound()
                elif pg.Rect.collidepoint(dontSwitchButton, mousePos):
                    # Check for the clicking on the don't switch button, then check for which door was pressed,
                    # and then check if the chosen door had the car or the goat
                    print("Don't switch button pressed")
                    print(chosenDoor[1])
                    finishRound()
                else:
                    pass
            else:
                # noinspection PyArgumentList,PyArgumentList,PyArgumentList
                if pg.Rect.collidepoint(door0.Rect, mousePos):
                    # Check if door[0] was pressed
                    openDoorSound.play()
                    print("door 0 pressed")
                    chosenDoor[1] = 0
                    if not doors[1]:
                        # check if doors[1] is a goat, if true then change it's texture and mark that the user chose
                        # a door
                        door1.texture = goatDoorImg
                        chosenDoor[0] = True
                    else:
                        # if doors[1] is a car, change the texture of door2 to the goat
                        door2.texture = goatDoorImg
                        chosenDoor[0] = True
                elif pg.Rect.collidepoint(door1.Rect, mousePos):
                    # check if door[1] was pressed
                    openDoorSound.play()
                    print("door 1 pressed")
                    chosenDoor[1] = 1
                    if not doors[0]:
                        # check if doors[0] is a goat, if true change the texture of door0 to a goat.
                        door0.texture = goatDoorImg
                        chosenDoor[0] = True
                    else:
                        # if doors[0] is a car, change the texture of door[2] to a goat.
                        door2.texture = goatDoorImg
                        chosenDoor[0] = True
                elif pg.Rect.collidepoint(door2.Rect, mousePos):
                    openDoorSound.play()
                    print("door 2 pressed")
                    chosenDoor[1] = 2
                    if not doors[0]:
                        # check if doors[0] is a goat, if yes change the texture of the door1 to a goat, and mark that
                        # the user has chosen a door.
                        door0.texture = goatDoorImg
                        chosenDoor[0] = True
                    else:
                        # if doors[0] is a car, change door1 to a goat, and mark that the user had chosen a door
                        door1.texture = goatDoorImg
                        chosenDoor[0] = True
                else:
                    pass
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                chosenDoor[0] = not chosenDoor[0]

        # check if the event is the X button
        if event.type == pg.QUIT:
            # if it is quit the game
            pg.quit()
            exit(0)
    time.sleep(0.01)
