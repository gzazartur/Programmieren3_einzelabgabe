#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 15:12:49 2018

@author: pyoneer
"""

import unittest
import getraenkeautomat

class getraenkeautomattest(unittest.TestCase):

    def setUp(self):
        self.__getraenkeautomat = getraenkeautomat.getraenkeautomat()

    def test_richtiger_betrag(self):
        self.assertEqual(self.__getraenkeautomat.getZustand(), 'Anfang')
        self.assertEqual(self.__getraenkeautomat.getBefehle(), ['50Cent', '1Cent', '2Cent', '5Cent', '10Cent', '20Cent', '1Euro', '2Euro', 'beenden'])

        self.__getraenkeautomat.eingabe('50Cent')
        self.assertEqual(self.__getraenkeautomat.getZustand(), 'Auswahl')
        self.assertEqual(self.__getraenkeautomat.getBefehle(), ['Limonade', 'Mineralwasser', 'beenden'])

        self.__getraenkeautomat.eingabe('Limonade')
        self.assertEqual(self.__getraenkeautomat.getZustand(), 'Anfang')
        self.assertEqual(self.__getraenkeautomat.getBefehle(), ['50Cent', '1Cent', '2Cent', '5Cent', '10Cent', '20Cent', '1Euro', '2Euro', 'beenden'])

    def test_falscher_bertrag(self):
        self.__getraenkeautomat.eingabe('10Cent')
        self.assertEqual(self.__getraenkeautomat.getZustand(), 'falscheMünze')
        self.assertEqual(self.__getraenkeautomat.getBefehle(), ['Limonade', 'Mineralwasser', 'beenden'])

        self.__getraenkeautomat.eingabe('Limonade')
        self.assertEqual(self.__getraenkeautomat.getZustand(), 'Anfang')
        self.assertEqual(self.__getraenkeautomat.getBefehle(), ['50Cent', '1Cent', '2Cent', '5Cent', '10Cent', '20Cent', '1Euro', '2Euro', 'beenden'])


suite = unittest.TestLoader().loadTestsFromTestCase(getraenkeautomattest)
unittest.TextTestRunner(verbosity=1).run(suite)