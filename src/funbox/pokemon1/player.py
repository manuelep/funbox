# -*- coding: utf-8 -*-

import pygame
from .common import logger
from . import settings

class Player(object):
    """docstring for Player."""

    def __init__(self, x_position, y_position):
        super(Player, self).__init__()
        self.position = [x_position, y_position]

    def update(self):
        logger.debug('Updating player')

    def update_position(self, x_change, y_change):
        self.position[0] += x_change
        self.position[1] += y_change

    def render(self, screen):
        pygame.draw.rect(screen, settings.WHITE,
            (
                self.position[0] * settings.PLAYER_SCALE,
                self.position[1] * settings.PLAYER_SCALE,
                settings.PLAYER_SCALE,
                settings.PLAYER_SCALE,
            ),
            2
        )
