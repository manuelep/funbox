# -*- coding: utf-8 -*-

import sys
import logging

from . import settings

# #######################################################
# implement custom loggers form settings.LOGGERS
# #######################################################

def get_logger(package):

    logger = logging.getLogger(package)
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
    )
    for item in settings.LOGGERS:
        level, filename = item.split(":", 1)
        if filename in ("stdout", "stderr"):
            handler = logging.StreamHandler(getattr(sys, filename))
        else:
            handler = logging.FileHandler(filename)
        handler.setFormatter(formatter)
        logger.setLevel(getattr(logging, level.upper(), "DEBUG"))
        logger.addHandler(handler)

    return logger
