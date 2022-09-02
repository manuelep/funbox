# -*- coding: utf-8 -*-

import pygame
from . import settings
from .common import logger
from .game import Game
from .game import GameState

def play():

    pygame.init()

    screen = pygame.display.set_mode(settings.DISPLAY)
    game = Game(screen)

    pygame.display.set_caption(settings.GAME_TITLE)

    game.set_up()
    while game.game_state==GameState.RUNNING:
        game.update()
        pygame.display.flip()
        logger.debug(game.game_state)
    logger.debug(game.game_state)

    # Done! Time to quit.
    pygame.quit()
