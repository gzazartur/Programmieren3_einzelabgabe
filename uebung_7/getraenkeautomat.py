#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 13:29:35 2018

@author: pyoneer
"""

class getraenkeautomat:
    """
    >>> g = getraenkeautomat()
    >>> g.zustandsAusgabe()
    Zustand:  Anfang
    Befehle:  ['50Cent', '1Cent', '2Cent', '5Cent', '10Cent', '20Cent', '1Euro', '2Euro', 'beenden']
    >>> g.eingabe('50Cent')
    Ausgabe: Bitte wählen
    >>> g.zustandsAusgabe()
    Zustand:  Auswahl
    Befehle:  ['Limonade', 'Mineralwasser', 'beenden']
    >>> g.eingabe('Limonade')
    Ausgabe: Bitte Limonade entnehmen
    >>> g.zustandsAusgabe()
    Zustand:  Anfang
    Befehle:  ['50Cent', '1Cent', '2Cent', '5Cent', '10Cent', '20Cent', '1Euro', '2Euro', 'beenden']
    >>> g.eingabe('10Cent')
    Ausgabe: eingabeSpeichern
    >>> g.zustandsAusgabe()
    Zustand:  falscheMünze
    Befehle:  ['Limonade', 'Mineralwasser', 'beenden']
    >>> g.eingabe('Limonade')
    Ausgabe: 10Cent
    >>> g.zustandsAusgabe()
    Zustand:  Anfang
    Befehle:  ['50Cent', '1Cent', '2Cent', '5Cent', '10Cent', '20Cent', '1Euro', '2Euro', 'beenden']
    """

    zustand = 'Anfang'
    befehle = ['50Cent','1Cent', '2Cent', '5Cent',
               '10Cent','20Cent', '1Euro', '2Euro', 'beenden']
    rückgabe = '0Cent'


    def eingabe(self, auswahl):

        if self.zustand == 'Anfang':
            self.befehle = ['Limonade','Mineralwasser','beenden']

            if auswahl == '50Cent':
                print('Ausgabe: Bitte wählen')
                self.zustand = 'Auswahl'
            if auswahl == '1Cent' or auswahl == '2Cent' or auswahl == '5Cent' or auswahl == '10Cent' or auswahl == '20Cent':
                print('Ausgabe: eingabeSpeichern')
                self.zustand = 'falscheMünze'
                self.rückgabe = auswahl
            if auswahl == '1Euro' or auswahl == '2Euro':
                self.zustand = 'Rückgabe'
                self.rückgabe = auswahl

        elif self.zustand == 'Auswahl':
            self.befehle = ['50Cent','1Cent', '2Cent', '5Cent',
                       '10Cent','20Cent', '1Euro', '2Euro', 'beenden']

            if auswahl == 'Limonade':
                print('Ausgabe: Bitte Limonade entnehmen')
            elif auswahl == 'Mineralwasser':
                print('Ausgabe: Bitte Mineralwasser entnehmen')

            if self.rückgabe == '1Euro' or self.rückgabe == '2Euro':
                print('Bitte Rückgeld entnehmen')

            self.zustand = 'Anfang'
        else:
            self.befehle = ['50Cent','1Cent', '2Cent', '5Cent',
                       '10Cent','20Cent', '1Euro', '2Euro', 'beenden']
            self.zustand = 'Anfang'
            print('Ausgabe:', self.rückgabe)

    def zustandsAusgabe(self):
        print('Zustand: ' , self.zustand)
        print('Befehle: ' , self.befehle)

    def getZustand(self):
        return self.zustand

    def getBefehle(self):
        return self.befehle

if __name__ == "__main__":

    import doctest
    doctest.testmod()

