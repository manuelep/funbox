# -*- coding: utf-8 -*-

import pygame
from . import settings

pygame.init()

screen = pygame.display.set_mode(settings.DISPLAY)

pygame.display.set_caption(settings.GAME_TITLE)

while True:
    pygame.display.flip()
