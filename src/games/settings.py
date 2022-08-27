# -*- coding: utf-8 -*-

GAME_TITLE = "Pokemon Clone"

DISPLAY = (600, 400)

BLACK = (0,0,0,)

WHITE = (255,255,255,)

# logger settings
LOGGERS = [
    "debug:stdout"
]  # syntax "severity:filename" filename can be stderr or stdout

# try import private settings
try:
    from .settings_private import *
except (ImportError, ModuleNotFoundError):
    pass
