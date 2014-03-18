#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import ConfigParser
import logging
import os
from os.path import expanduser
import sys
import traceback
from twython import TwythonStreamer


__all__ = ['main']
__author__ = ""
__url__ = ""
__version__ = ""
__license__ = ""

CONFIG_FILE = '.favoriteer.cfg'
CONFIG_SECTION = 'twitter'
LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'


def init_argparser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-c', '--config_file',
                        help="config file - if none specified, looks in ~ and ./ for .favoriteer.cfg", metavar="FILE")
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='increase chattiness of script')
    return parser


def get_config(args):
    config_file = args.config_file or get_config_from_default_locations()
    config = ConfigParser.SafeConfigParser()
    try:
        config.read(config_file)
        return config
    except:
        raise Exception("Unable to locate config file ({0}) from command line, current dir, or user's home directory".format(CONFIG_FILE))


def get_config_from_default_locations():
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    config_in_curr_dir = os.path.join(curr_dir, CONFIG_FILE)

    home_dir = expanduser('~')
    config_in_home_dir = os.path.join(home_dir, CONFIG_FILE)

    if os.path.isfile(config_in_curr_dir):
        return config_in_curr_dir
    elif os.path.isfile(config_in_home_dir):
        return config_in_home_dir
    else:
        return None


def do_work_son(args):
    config = get_config(args)

    ACCESS_KEY = config.get(CONFIG_SECTION, 'ACCESS_KEY')
    ACCESS_SECRET = config.get(CONFIG_SECTION, 'ACCESS_SECRET')

    logging.debug("Accessing twitters with access key: {0}".format(ACCESS_KEY))
    logging.debug("Accessing twitters with access secret: {0}".format(ACCESS_SECRET))

    # ask database for users
    users = get_all_users()

    # for each user, use consumer_key, consumer_secret
    for user in users:
        for favorite in user.following:
            if favorite.last_update > (datetime.datetime.utcnow() + timedelta(mins=15)):
                new_favorites = get_favorites_since(favorites.last_update_id)
                for new_favorite in new_favorites:
                    save(new_favorite)


def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = init_argparser()
    args = parser.parse_args(argv)

    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format=LOG_FORMAT)

    try:
        do_work_son(args)
    except:
        trace = traceback.format_exc()
        logging.error("OMGWTFBBQ: {0}".format(trace))
        sys.exit(1)

    # Yayyy-yah
    sys.exit(0)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

# vim: filetype=python
