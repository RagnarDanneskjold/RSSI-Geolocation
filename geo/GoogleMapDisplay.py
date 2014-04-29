#!/usr/bin/python
# -*- coding: utf-8 -*-

from MapBuilder import *
import sys
from PyQt4 import QtCore, QtGui, QtWebKit
from PyQt4.QtCore import *
from FakePlane import FakePlane
import time

class GoogleMapDisplay(QtGui.QMainWindow):
    def __init__(self, lat0=46.51860809, lon0=6.559470177, zoom=16):
        """
            Initialize the browser GUI and connect the events
        """
        QtGui.QMainWindow.__init__(self)
        self.resize(800, 600)
        self.centralwidget = QtGui.QWidget(self)

        self.mainLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(0)

        self.html = QtWebKit.QWebView()
        self.mainLayout.addWidget(self.html)
        self.setCentralWidget(self.centralwidget)
        self.mymap = MapBuilder(lat0, lon0, zoom, 'ROADMAP')

    def addPoint(self, lat, lon, radius=1, fillOpacity=1.0, fillColor='#00FF00', strokeColor='#000000'):
        self.mymap.addCircle(Circle(lat, lon, radius=radius, \
                                    fillColor=fillColor, fillOpacity=fillOpacity, strokeColor=strokeColor))

    def drawMap(self):
        url = '../res/mymap.html'
        self.mymap.draw(url)
        self.html.load(QtCore.QUrl(url))
        self.html.show()

    def addPoints(self, listOfPoints, size=1, color='#0000FF'):
        for (lat, lon) in listOfPoints:
            self.addPoint(lat, lon, size, color)


