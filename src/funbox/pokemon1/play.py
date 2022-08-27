# -*- coding: utf-8 -*-

import logging
import itertools
from .. import settings

if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('-l', '--log-level', help='Log level setup',
        default=[], action='append',
        choices = [logging.getLevelName(level) for level in range(10, 60, 10)]
    )

    parser.add_argument('-f', '--log-file', help='Log file',
        default=[], action='append'
    )

    args = parser.parse_args()

    if any((args.log_level, args.log_file,)):
        settings.LOGGERS = [f'{level.lower() or "info"}:{store or "stdout"}'
            for level,store in itertools.zip_longest(args.log_level, args.log_file)]

    from .main import play, foo

    foo()
