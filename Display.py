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

# Loading images
closedDoorImg = pg.image.load("Data/Assets/Images/closedDoor0.jpg")
openedDoorImg = pg.image.load("Data/Assets/Images/openedDoor0.jpg")
# resizing the images
# closedDoorImgSize = closedDoorImg.get_rect().size  NOT NEEDED
closedDoorImgSize = np.asarray((229, 394))
openedDoorImgSize = np.asarray((229, 394))
# print(closedDoorImgSize)
closedDoorImg = pg.transform.scale(closedDoorImg, closedDoorImgSize)
openedDoorImg = pg.transform.scale(openedDoorImg, openedDoorImgSize)

door0 = Obj(150, 30, closedDoorImg, True)
door1 = Obj(550, 30, closedDoorImg, True)
door2 = Obj(950, 30, closedDoorImg, True)
chosenDoor = False

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
            if chosenDoor:
                # TODO: Add actual functionality to the buttons
                # noinspection PyArgumentList,PyArgumentList
                if pg.Rect.collidepoint(switchButton, mousePos):
                    print("Switch button pressed!")
                elif pg.Rect.collidepoint(dontSwitchButton, mousePos):
                    print("Don't switch button pressed")
                else:
                    pass
            else:
                # TODO: Write buttons
                # noinspection PyArgumentList,PyArgumentList,PyArgumentList
                if pg.Rect.collidepoint(door0.Rect, mousePos):
                    print("door 0 pressed")
                    if not doors[1]:
                        door1.texture = openedDoorImg
                    else:
                        door2.texture = openedDoorImg
                elif pg.Rect.collidepoint(door1.Rect, mousePos):
                    print("door 1 pressed")
                    if not doors[0]:
                        door0.texture = openedDoorImg
                    else:
                        door2.texture = openedDoorImg
                elif pg.Rect.collidepoint(door2.Rect, mousePos):
                    print("door 2 pressed")
                    if doors[1]:
                        door1.texture = openedDoorImg
                    else:
                        door2.texture = openedDoorImg
                else:
                    pass
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                chosenDoor = not chosenDoor

        # check if the event is the X button
        if event.type == pg.QUIT:
            # if it is quit the game
            pg.quit()
            exit(0)
    time.sleep(0.01)
