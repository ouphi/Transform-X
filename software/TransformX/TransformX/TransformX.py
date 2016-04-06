#!/usr/bin/python

from PyQt4 import QtGui, QtCore
import sys

import view

import pypot.robot
from BotControleur import *
 

if __name__=='__main__':
    '''Main Class of TransformX : Init the robot and launch ther interface'''
    my_robot = from_json('monrobot.json')#Generation du robot a partir du json
    app = QtGui.QApplication(sys.argv)
    devappli = BotControl(my_robot)
  
    devappli.main()

    app.exec_()
    print("Liberation du robot")
    my_robot.compliant = True
    my_robot.close()