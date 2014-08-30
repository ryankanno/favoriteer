#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import os
from os.path import expanduser


CONFIG_FILE = '.favoriteer.cfg'


def get_config(config_file):
    config = ConfigParser.SafeConfigParser()
    try:
        config.read(config_file)
        return config
    except:
        raise Exception("Unable to locate config file ({0}) from command line, \
                current dir, or user's home directory".format(CONFIG_FILE))


def get_config_file_from_default_locations():
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

# vim: filetype=python
