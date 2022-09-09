# -*- coding: utf-8 -*-

from pathlib import Path
from os import path
from . import settings
from ..common import get_logger

logger = get_logger('pokemon1')

def path_to_character(file):
    return path.join(Path(__file__).parent, settings.CHAR_PATH, file)

def path_to_tile(file):
    return path.join(Path(__file__).parent, settings.TILE_PATH, file)
