
import pygame, random

from gale.input_handler import InputHandler, InputData
from gale.state_machine import BaseState
from gale.text import render_text

import settings

class Car:
    def __init__(self, posx: int, skin: int) -> None:
        self.x = posx
        self.y = -settings.TEXTURES["car1"].get_height()
        self.width = settings.TEXTURES["car1"].get_width()
        self.height = settings.TEXTURES["car1"].get_height()
        self.skin = skin
        self.vy = 0
        self.rotate = 180
        self.posSet = [470, 610, 745, 883]
    
    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def update(self, dt: float) -> None:
        self.y += 50
        if self.y > settings.VIRTUAL_HEIGHT:
            self.y = -settings.TEXTURES["car1"].get_height()
            self.x = random.randint(0,3)
            self.skin = random.randint(0, settings.NUM_SKIN-1)
            print("posx", self.x)
        


    def render(self, surface: pygame.Surface) -> None:
        surface.blit(pygame.transform.rotate(settings.TEXTURES["car"+str(self.skin)],self.rotate) , (self.posSet[self.x], self.y))

    
