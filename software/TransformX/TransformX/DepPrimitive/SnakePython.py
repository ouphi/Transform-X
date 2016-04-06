 #!/usr/bin/python

'''This lib handle the basic Snake moves'''
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

def SnakeDown(self):
                '''Go Down snake primitive'''
                time.sleep(0.1)
                mapos={'m11':0,'m12':20,'m13':90,'m21':120,'m22':20,'m23':90,
               'm31':120,'m32':20,'m33':90,'m41':0,'m42':20,'m43':90}
                self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True) 
                mapos={'m11':0,'m12':-40,'m13':90,'m21':120,'m22':-40,'m23':90,
               'm31':120,'m32':-40,'m33':90,'m41':0,'m42':-40,'m43':90}
                self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True) 
                mapos={'m11':120,'m12':-40,'m13':90,'m21':0,'m22':-40,'m23':90,
               'm31':0,'m32':-40,'m33':90,'m41':120,'m42':-40,'m43':90}
                self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True) 
                mapos={'m11':120,'m12':20,'m13':90,'m21':0,'m22':20,'m23':90,
               'm31':0,'m32':20,'m33':90,'m41':120,'m42':20,'m43':90}
                self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True) 

def SnakeLeft(self):
                '''Go Left snake primitive'''
                time.sleep(0.1)
                mapos={'m11':120,'m12':20,'m13':self.listepos[2],'m21':120,'m22':20,'m23':self.listepos[5],
               'm31':0,'m32':20,'m33':self.listepos[8],'m41':0,'m42':20,'m43':self.listepos[11]}
                self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True) 
                mapos={'m11':120,'m12':-40,'m13':self.listepos[2],'m21':120,'m22':-40,'m23':self.listepos[5],
               'm31':0,'m32':-40,'m33':self.listepos[8],'m41':0,'m42':-40,'m43':self.listepos[11]}
                self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True) 
                mapos={'m11':0,'m12':-40,'m13':self.listepos[2],'m21':0,'m22':-40,'m23':self.listepos[5],
               'm31':120,'m32':-40,'m33':self.listepos[8],'m41':120,'m42':-40,'m43':self.listepos[11]}
                self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True) 
                mapos={'m11':0,'m12':20,'m13':self.listepos[2],'m21':0,'m22':20,'m23':self.listepos[5],
               'm31':120,'m32':20,'m33':self.listepos[8],'m41':120,'m42':20,'m43':self.listepos[11]}
                self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True) 

def SnakeRight(self):
                '''Go Right snake primitive'''

                time.sleep(0.1)
                mapos={'m11':0,'m12':20,'m13':self.listepos[2],'m21':0,'m22':20,'m23':self.listepos[5],
               'm31':120,'m32':20,'m33':self.listepos[8],'m41':120,'m42':20,'m43':self.listepos[11]}
                self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True) 
                mapos={'m11':0,'m12':-40,'m13':self.listepos[2],'m21':0,'m22':-40,'m23':self.listepos[5],
               'm31':120,'m32':-40,'m33':self.listepos[8],'m41':120,'m42':-40,'m43':self.listepos[11]}
                self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True) 
                mapos={'m11':120,'m12':-40,'m13':self.listepos[2],'m21':120,'m22':-40,'m23':self.listepos[5],
               'm31':0,'m32':-40,'m33':self.listepos[8],'m41':0,'m42':-40,'m43':self.listepos[11]}
                self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True) 
                mapos={'m11':120,'m12':20,'m13':self.listepos[2],'m21':120,'m22':20,'m23':self.listepos[5],
               'm31':0,'m32':20,'m33':self.listepos[8],'m41':0,'m42':20,'m43':self.listepos[11]}
                self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True) 

def SnakeUp(self):

                '''Go Up snake primitive'''

                                
                mapos={'m11':120,'m12':20,'m13':90,'m21':0,'m22':20,'m23':90,
               'm31':0,'m32':20,'m33':90,'m41':120,'m42':20,'m43':90}
                self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True) 
                mapos={'m11':120,'m12':-40,'m13':90,'m21':0,'m22':-40,'m23':90,
               'm31':0,'m32':-40,'m33':90,'m41':120,'m42':-40,'m43':90}
                self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True) 
                mapos={'m11':0,'m12':-40,'m13':90,'m21':120,'m22':-40,'m23':90,
               'm31':120,'m32':-40,'m33':90,'m41':0,'m42':-40,'m43':90}
                self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True) 
                mapos={'m11':0,'m12':20,'m13':90,'m21':120,'m22':20,'m23':90,
               'm31':120,'m32':20,'m33':90,'m41':0,'m42':20,'m43':90}
                self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True) 

def SnakeChange(self):
             '''Take the form of a Snake '''

             self.my_robot.compliant=False
             mapos={'m11':90,'m12':0,'m13':90,'m21':90,'m22':90,'m23':90,
                  'm31':self.listepos[6],'m32':90,'m33':90,'m41':self.listepos[9],'m42':0,'m43':90}
             self.my_robot.goto_position(mapos, duration=1, wait=True)  
    
             mapos={'m11':0,'m12':0,'m13':90,'m21':0,'m22':0,'m23':90,
               'm31':self.listepos[6],'m32':0,'m33':90,'m41':self.listepos[9],'m42':0,'m43':90}
             self.my_robot.goto_position(mapos, duration=1, wait=True)  
             self.serpent=True
             self.CommandPrompt.setHtml('''<html><body>Mode Serpent!!<br>Z:Avancer<br>Q:Gauche<br>D:Droite<br>S:Bas<br>L:Led Play </body></html''')
         
     