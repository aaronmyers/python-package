#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_fake
----------------------------------

Tests for `fake` module.
"""

import unittest

import fake


class TestFake(unittest.TestCase):

    def setUp(self):
        self.message = 'hello'

    def test_something(self):
        output = fake.hello()
        assert(output == self.message)

    def tearDown(self):
        pass
