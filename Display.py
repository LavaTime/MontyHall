# Importing libraries
from typing import List, Any

import pygame as pg
import time
import numpy as np
from pygame.locals import *

# Initiating functions
pg.init()
pg.display.init()

# Defining constants
WIDTH, HEIGHT = (1280, 720)
SIZE = (WIDTH, HEIGHT)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Obj:
    # An class that will create the objects that will be visible on the screen
    def __init__(self, xpos: int, ypos: int, currenttexture: object, visible: bool) -> object:
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
        Obj.List.append(self)

    List = []

    def blit(self):
        # display the object on the screen on the corresponding positions and texture
        screen.blit(self.texture, (self.x, self.y))


# Screen settings
screen = pg.display.set_mode(size=SIZE)
pg.display.set_caption("Monty Hall")

# Loading images
closedDoorImg = pg.image.load("Data/Assets/Images/closedDoor0.jpg")
# resizing the images
# closedDoorImgSize = closedDoorImg.get_rect().size  NOT NEEDED
closedDoorImgSize = np.asarray((229, 394))
# print(closedDoorImgSize)
closedDoorImg = pg.transform.scale(closedDoorImg, closedDoorImgSize)

door1 = Obj(150, 30, closedDoorImg, True)
door2 = Obj(550, 30, closedDoorImg, True)
door3 = Obj(959, 30, closedDoorImg, True)


while True:
    screen.fill(WHITE)
    for i in Obj.List:
        i.blit()
    largeText = pg.font.Font('freesansbold.ttf', 115)
    pg.draw.rect(screen, GREEN, pg.Rect(75, 500, 400, 150))
    pg.draw.rect(screen, RED, pg.Rect(805, 500, 400, 150))
    pg.display.flip()
    for event in pg.event.get():
        # Check if the mouse is clicked down and it's position
        if event.type == pg.MOUSEBUTTONDOWN:
            # TODO: Click function
            mousePos = pg.mouse.get_pos()
            # Check for the position of the mouse relative to the current game state and it's buttons

        # check if the event is the X button
        if event.type == pg.QUIT:
            # if it is quit the game
            pg.quit()
            exit(0)
    time.sleep(0.01)
