# -*- coding: utf-8 -*-

import pygame
from . import settings
from .common import logger

def play():

    pygame.init()

    screen = pygame.display.set_mode(settings.DISPLAY)

    pygame.display.set_caption(settings.GAME_TITLE)

    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()
