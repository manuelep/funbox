# -*- coding: utf-8 -*-

from . import settings
from .common import logger
from enum import Enum
import pygame
from .player import Player
from .common import path_to_tile
from pathlib import Path

map_tile_image = {
    "G": pygame.image.load(path_to_tile('tileGrass1.png')),
    "g": pygame.image.load(path_to_tile('tileGrass2.png')),
    "S": pygame.image.load(path_to_tile('tileSand1.png')),
    "s": pygame.image.load(path_to_tile('tileSand2.png')),
}

class GameState(Enum):
    """docstring for GameState."""
    NONE = 0
    RUNNING = 1
    ENDED = 2

class Map(object):
    """docstring for Map."""

    def __init__(self, src):
        super(Map, self).__init__()
        self.tiles = self.load(src)

    def load(self, src):
        tiles = []
        with open(Path(__file__).parent / src) as mapfile:
            for index,line in enumerate(mapfile):
                tileline = line.split()
                tiles.append(tileline)
            self.height = index
            self.width = len(line)
        return tiles

    def render(self, screen):
        for yy,tileline in enumerate(self.tiles):
            for xx,tile in enumerate(tileline):
                image = map_tile_image[tile]
                rect = pygame.Rect(xx * settings.SCALE, yy * settings.SCALE, settings.SCALE, settings.SCALE)
                screen.blit(image, rect)


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
        self.map = Map('map01.txt')

    def update(self):
        logger.debug("Questo è l'update")
        # TODO:
        # Disegno dei giocatori nell'area di gioco
        self.screen.fill(settings.BLACK)

        self.map.render(self.screen)

        self.handle_events()

        for object in self.objects:
            object.render(self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logger.debug('QUIT!')
                self.game_state = GameState.ENDED
            if event.type == pygame.KEYDOWN:
                newx, newy = self.player.position
                if event.key == pygame.K_w:
                    newy = max(self.player.position[1]-1, 0)
                elif event.key == pygame.K_s:
                    newy = min(self.player.position[1]+1, self.map.height)
                elif event.key == pygame.K_d:
                    newx = min(self.player.position[0]+1, self.map.width)
                elif event.key == pygame.K_a:
                    newx = max(self.player.position[0]-1, 0)

                self.player.update_position(newx, newy, relative=False)
