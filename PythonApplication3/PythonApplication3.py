#!/usr/bin/python
 
from PyQt4 import QtGui, QtCore
import sys

import view
import eventdev
from eventdev import eventviewdev
 

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    devappli =  eventviewdev()
  
    devappli.main()

    app.exec_()
