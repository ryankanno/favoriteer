#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import ok_
from nose.tools import raises
import os
from py_favoriteer.utilities import get_config
import unittest


class TestUtilities(unittest.TestCase):

    def setUp(self):
        self.cwd = os.path.dirname(os.path.realpath(__file__))
        self.config_file = os.path.join(self.cwd, 'data', '.favoriteer.cfg')

    def test_get_config_with_config_returns_valid_config(self):
        config = get_config(self.config_file)
        ok_(config is not None)

    @raises(Exception)
    def test_get_config_with_invalid_config_raises_exception(self):
        get_config('/b/a/d/config')

# vim: filetype=python
