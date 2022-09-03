# -*- coding: utf-8 -*-

from .common import logger
from enum import Enum
import pygame
from .player import Player

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
        self.objects = []

    def set_up(self):
        logger.debug('Questo è il setup')
        self.game_state = GameState.RUNNING
        self.player = Player(1, 1)
        self.objects.append(self.player)
        ## TODO:
        # 1. definizione giocatori

    def update(self):
        logger.debug("Questo è l'update")
        # TODO:
        # Disegno dei giocatori nell'area di gioco
        self.handle_events()
        for object in self.objects:
            object.render(self.screen)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logger.debug('QUIT!')
                self.game_state = GameState.ENDED
            if event.type == pygame.KEYDOWN:
                # UP
                if event.key == pygame.K_w:
                    self.player.update_position(0, -1)
                elif event.key == pygame.K_s:
                    self.player.update_position(0, 1)
                elif event.key == pygame.K_d:
                    self.player.update_position(1, 0)
                elif event.key == pygame.K_a:
                    self.player.update_position(-1, 0)
