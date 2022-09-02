# -*- coding: utf-8 -*-

from .common import logger
from enum import Enum
import pygame

class GameState(Enum):
    """docstring for GameState."""
    NONE = 0
    RUNNING = 1
    ENDED = 2


class Game(object):
    """docstring for Game."""

    def __init__(self, screen):
        super(Game, self).__init__()
        self.screen = screen
        self.game_state = GameState.NONE

    def set_up(self):
        logger.debug('Questo è il setup')
        self.game_state = GameState.RUNNING
        ## TODO:
        # 1. definizione giocatori

    def update(self):
        logger.debug("Questo è l'update")
        # TODO:
        # Disegno dei giocatori nell'area di gioco
        self.handle_events()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logger.debug('QUIT!')
                self.game_state = GameState.ENDED
