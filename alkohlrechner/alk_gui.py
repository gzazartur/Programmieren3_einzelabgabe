#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 18:02:31 2018

@author: pyoneer
"""

from PyQt5 import QtWidgets, QtCore, uic


class alkoholrechner_gui(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        # load and show the user interface created with the designer.
        self.ui = uic.loadUi('alkoholrechner.ui')
        self.ui.show()

        self.ui.cmd_getr_hin.clicked.connect(self.hinzu)
        self.ui.cmd_getr_del.clicked.connect(self.delete)
        self.ui.cmd_ber.clicked.connect(self.berechen)

    def umrechnung_ml_zu_g(self, menge, vol):
        return menge*1000 * (vol/100) * 0.8

    def tho_bak(self, alk_menge, gewicht, geschlecht, grosse):
        if geschlecht == 'männlich':
            r = 0.31608 - 0.004821 * gewicht + 0.004432 * grosse
            return alk_menge/(gewicht * r)
        else:
            r = 0.31223 - 0.006446 * gewicht + 0.004466 * grosse
            return alk_menge/(gewicht * r)

    def resorptionsdefizits(self, tho_bak):
        return tho_bak - (tho_bak * 15/100)

    def abbauwert(self, zeit, respdef):
        return respdef - zeit * 0.15

    def hinzu(self):
        rowPos = self.ui.tabwid_getranke.rowCount()
        self.ui.tabwid_getranke.insertRow(rowPos)

    def delete(self):
        indices = self.ui.tabwid_getranke.selectionModel().selectedRows()

        for index in sorted(indices):
            self.ui.tabwid_getranke.removeRow(index.row())

    def berechen(self):
        ui = self.ui
        geschlecht = ui.cbox_geschlecht.currentText()
        alter = int(ui.le_alter.text())
        gewicht = float(ui.le_gewicht.text())
        grosse = float(ui.le_grosse.text())
        zeitraum = float(ui.le_time.text())

        vol = 0
        menge = 0

        for _col in range(ui.tabwid_getranke.rowCount()):
            vol += float(ui.tabwid_getranke.item(_col, 1).text())
            menge += float(ui.tabwid_getranke.item(_col, 2).text())

        auf_alg = self.umrechnung_ml_zu_g(menge,vol)
        tho_bak = self.tho_bak(auf_alg, gewicht, geschlecht, grosse)
        resp_de = self.resorptionsdefizits(tho_bak)
        bak = self.abbauwert(zeitraum, resp_de)

        bak = round(bak, 2)

        if bak < 0:
            ui.txt_erg_promille.setNum(0)
        else:
            ui.txt_erg_promille.setNum(bak)

        if bak >= 4:
            ui.progressBar.setValue(4)
        else:
            ui.progressBar.setValue(bak)

        if bak >= 0 and bak <= 1:
            ui.txt_browser.setText("Wir sehen immer schlechter, etwa 15% Sehleistung haben wir bei diesem Promillewert schon eingebüßt. Auch das Hören ist beeinträchtigt und wir können Geschwindigkeiten nicht mehr richtig einschätzen. Da kann es durchaus passieren, dass wir beim Vorbeigehen versehentlich jemanden anrempeln. Nicht selten werden wir dann sauer, weil wir reizbarer sind, als im nüchternen Zustand")
        elif bak > 1 and bak <= 2:
            ui.txt_browser.setText("Im sogenannten Rauschstadium kommt es zur weiteren Verschlechterung der Sehfähigkeit und vor allem des räumlichen Sehens. Wir sind verwirrt und haben deutliche Sprech-, Reaktions-, Gleichgewichts- und Orientierungsstörungen. Wer so viel Alkohol im Blut hat, hat auch seine Kritikfähigkeit meist verloren. Das sind deutliche Warnsignale für eine Alkoholvergiftung.")
        elif bak > 2 and bak <= 3:
            ui.txt_browser.setText("Bei diesem Promillewert ist professionelle Hilfe gefragt. Wer das Betäubungsstadium erreicht, reagiert kaum noch und bewegt sich unkoordiniert. Durch Erbrechen versucht der Körper, sich zumindest des Alkohols im Magen zu entledigen. Gleichzeitig kann es zur Muskelerschlaffung kommen.")
        elif bak > 3:
            ui.txt_browser.setText("TOD!!!")



if __name__ == '__main__':
    alk = alkoholrechner_gui()
