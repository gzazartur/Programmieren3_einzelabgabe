#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 20:27:46 2018

@author: pyoneer
"""
from unittest import mock
import unittest
import simulation_test
with mock.MagicMock() as ZahlenManipulator:
    z = ZahlenManipulator()
    z.get_wert.side_effect = [1, 2, 3, 4, 5]
    suite = unittest.TestLoader().loadTestsFromTestCase(
                                    simulation_test)
    unittest.TextTestRunner(verbosity=1).run(suite)
    assert len(z.get_wert.mock_calls) == 5