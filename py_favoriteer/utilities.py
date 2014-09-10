#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import os
from os.path import expanduser


CONFIG_FILE = '.favoriteer.cfg'


def get_config(config_file):
    config = ConfigParser.SafeConfigParser()
    if os.path.isfile(config_file):
        config.read(config_file)
        return config
    else:
        raise Exception(
            "Unable to locate config file ({0})".format(config_file))


def get_config_file_from_default_locations(
        default_locations=[expanduser('~')],
        config_name=CONFIG_FILE):

    for location in default_locations:
        config_path = os.path.join(location, config_name)
        if os.path.isfile(config_path):
            return config_path

    return None

# vim: filetype=python
