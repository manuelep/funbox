# -*- coding: utf-8 -*-

import pygame
from .common import logger
from . import settings

class Player(object):
    """docstring for Player."""

    def __init__(self):
        super(Player, self).__init__()

    def update(self):
        logger.debug('Updating player')

    def render(self, screen):
        pygame.draw.rect(screen, settings.WHITE, (10, 10, 10, 10,), 2)
