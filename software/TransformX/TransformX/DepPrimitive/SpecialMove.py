 #!/usr/bin/python

'''This lib Handle Some Complexe move such as step climbing or be able to flip'''
from PyQt4 import QtGui, QtCore
from pypot.dynamixel import *
from pypot.dynamixel import autodetect_robot
from PyQt4.QtCore import SIGNAL

from SaveWindows import SaveWindowsF
import sys
import pickle
import time
from pypot.robot import from_json
from pypot.primitive.move import MoveRecorder, Move, MovePlayer
sys.path.insert(0, 'ProgrammationMimetiqueVisuelle')
from SpecialMove import *
from AraigneePython import *
from SnakePython import *
from Enregistrement import *

def retourner(self):
         '''Make the Robot Flip'''
         time.sleep(0.3)
     #    self.Vitessenum.setValue(1)
         readFile(self,"Retourner/retourner1.txt")
         time.sleep(0.3)
         readFile(self,"Retourner/retourner2.txt")
         time.sleep(0.3)
         readFile(self,"Retourner/retourner3.txt") 

def climb(self):

            '''Experiment step climbing'''
            y=0
            time.sleep(0.1)
            self.Vitessenum.setValue(0.1)
            while y<15:
              readFile(self,"climb/step1bis.txt")
              y=y+1
   
            self.Vitessenum.setValue(0.8)
            readFile(self,"climb/step2bis.txt")
            self.Vitessenum.setValue(1)
            readFile(self,"climb/step3bis.txt")
            self.serpent=False
            if(self.previous!=1): 
                    mapos={'m13':90,'m23':90,'m33':90,'m43':90}
                    self.my_robot.goto_position(mapos, duration=0.3, wait=True)   

            mapos={'m41':-30,'m42':40,'m21':90,'m22':125}
            self.my_robot.goto_position(mapos, duration=0.15, wait=True)   
            mapos={'m31':-30,'m32':40,'m11':90,'m12':125}
            self.my_robot.goto_position(mapos, duration=0.15, wait=True)   
            mapos={'m21':0,'m22':90,'m23':90,'m41':0,'m42':90,'m43':90}
            self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
            mapos={'m11':-30,'m12':40,'m31':90,'m32':125}
            self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
            mapos={'m21':-30,'m22':40,'m41':90,'m42':125}
            self.my_robot.goto_position(mapos, duration=0.15, wait=True) 

            mapos={'m11':0,'m12':90,'m13':90,'m31':0,'m32':90,'m33':90}
            self.my_robot.goto_position(mapos, duration=0.15, wait=True)  
            if(self.previous!=1): 
                    mapos={'m13':90,'m23':90,'m33':90,'m43':90}
                    self.my_robot.goto_position(mapos, duration=0.3, wait=True)   

            mapos={'m41':-30,'m42':40,'m21':90,'m22':125}
            self.my_robot.goto_position(mapos, duration=0.15, wait=True)   
            mapos={'m31':-30,'m32':40,'m11':90,'m12':125}
            self.my_robot.goto_position(mapos, duration=0.15, wait=True)   
            mapos={'m21':0,'m22':90,'m23':90,'m41':0,'m42':90,'m43':90}
            self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
            mapos={'m11':-30,'m12':40,'m31':90,'m32':125}
            self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
            mapos={'m21':-30,'m22':40,'m41':90,'m42':125}
            self.my_robot.goto_position(mapos, duration=0.15, wait=True) 

            mapos={'m11':0,'m12':90,'m13':90,'m31':0,'m32':90,'m33':90}
            self.my_robot.goto_position(mapos, duration=0.15, wait=True)  
            readFile(self,"climb/step5bis.txt")
            readFile(self,"climb/step7bis.txt")
            self.my_robot.m32.goto_position(90,duration=0.5, wait=True)
            self.my_robot.m12.goto_position(0,duration=0.5, wait=True)
            self.my_robot.m42.goto_position(0,duration=0.5, wait=True)
            self.my_robot.m22.goto_position(0,duration=0.5, wait=True)
            self.my_robot.m32.goto_position(0,duration=0.5, wait=True)
         