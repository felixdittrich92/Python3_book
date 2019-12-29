#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class MeinWidget(QtWidgets.QWidget):
    def __init__(self, parent=None): 
        super().__init__(parent)
        self.pen = QtGui.QPen(QtGui.QColor(0,0,0)) 
        self.pen.setWidth(3) 
        self.brush1 = QtGui.QBrush(QtGui.QColor(100,100,100,100))
        self.brush2 = QtGui.QBrush(QtGui.QColor(200,200,200,100))
        
    def paintEvent(self, event): 
        painter = QtGui.QPainter(self) 
        painter.setPen(self.pen) 
        painter.setBrush(self.brush1) 
        painter.drawEllipse(10, 10, 130, 130)

        painter.setBrush(self.brush2)
        painter.drawEllipse(110, 10, 130, 130)
        
app = QtWidgets.QApplication(sys.argv) 
widget = MeinWidget()
widget.resize(250, 150) 
widget.show()
sys.exit(app.exec_())
 
