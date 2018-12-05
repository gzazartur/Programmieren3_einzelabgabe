#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 20:15:58 2018

@author: pyoneer
"""
import unittest
import numpy as np
from unittest import mock

with mock.MagicMock() as simulation:
    z = simulation()
    z.g_force.side_effect = 1

class simulation_test(unittest.TestCase):
    def test_g_force(self):
        assert z.g_force.mock_calls == 1







suite = unittest.TestLoader().loadTestsFromTestCase(simulation_test)
unittest.TextTestRunner(verbosity=1).run(suite)
