#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_tutorials
----------------------------------

Tests for `tutorials` module.
"""

import unittest

import tutorials


class TestTutorials(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(tutorials.hello_world())
        pass

    def tearDown(self):
        pass
