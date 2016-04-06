 
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
'''This lib handle the basic Araignee moves'''

def AraigneeSideRight(self):
                '''Move the spider to the right'''
                time.sleep(0.2)
                if(self.previous!=6): 
                    mapos={'m13':30,'m23':30,'m33':30,'m43':30}
                    self.my_robot.goto_position(mapos, duration=0.3, wait=True)  
                #Deplacement Araignee LATERALE  droite
                 
                mapos={'m41':-30,'m42':40,'m21':90,'m22':125}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True)   
                #time.sleep(0.1) 
                mapos={'m31':90,'m32':125,'m11':-30,'m12':40}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True)   
                mapos={'m21':0,'m22':90,'m23':20,'m41':0,'m42':90,'m43':20}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
                #mapos={'m21':30}
                #self.my_robot.goto_position(mapos, duration=0.1, wait=True)  
                mapos={'m11':90,'m12':125,'m31':-30,'m32':40}
                
                self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
                
                mapos={'m21':-30,'m22':40,'m41':90,'m42':125}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
                #time.sleep(0.1)
                 
                mapos={'m11':0,'m12':90,'m13':20,'m31':0,'m32':90,'m33':30}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True)  
                self.previous=6

def AraigneeSideLeft(self):
                '''Move the spider to the left'''

              #Deplacement Araignee LATERALE 
        

                if(self.previous!=5): 
                    mapos={'m13':30,'m23':30,'m33':30,'m43':30}
                    self.my_robot.goto_position(mapos, duration=0.3, wait=True)  

                time.sleep(0.2)
                mapos={'m21':-30,'m22':40,'m41':90,'m42':125}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True)   
                #time.sleep(0.1) 
                mapos={'m11':90,'m12':125,'m31':-30,'m32':40}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True)   
                mapos={'m21':0,'m22':90,'m23':20,'m41':0,'m42':90,'m43':20}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
                #mapos={'m21':30}
                #self.my_robot.goto_position(mapos, duration=0.1, wait=True)  
                mapos={'m31':90,'m32':125,'m11':-30,'m12':40}
                
                self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
                
                mapos={'m41':-30,'m42':40,'m21':90,'m22':125}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
                #time.sleep(0.1)
                 
                mapos={'m11':0,'m12':90,'m13':20,'m31':0,'m32':90,'m33':30}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
                self.previous=5 

def AraigneeDown(self):

                '''Move the spider down'''

                time.sleep(0.2)
                if(self.previous!=4): 
                    mapos={'m13':90,'m23':90,'m33':90,'m43':90}
                    self.my_robot.goto_position(mapos, duration=0.3, wait=True)  

                mapos={'m21':-30,'m22':40,'m41':90,'m42':125}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True)   
                #time.sleep(0.1) 
                mapos={'m11':-30,'m12':40,'m31':90,'m32':125}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True)   
                mapos={'m21':0,'m22':90,'m23':90,'m41':0,'m42':90,'m43':90}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
                #mapos={'m21':30}
                #self.my_robot.goto_position(mapos, duration=0.1, wait=True)  
                mapos={'m31':-30,'m32':40,'m11':90,'m12':125}
                
                self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
                
                mapos={'m41':-30,'m42':40,'m21':90,'m22':125}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
                #time.sleep(0.1)
                 
                mapos={'m11':0,'m12':90,'m13':90,'m31':0,'m32':90,'m33':90}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True)  
                #mapos={'m31':30}
                self.previous=4

def AraigneeLeft(self):

                '''Move the spider slowly turn to the left'''

                time.sleep(0.2)    
                if(self.previous!=3): 
                    mapos={'m13':0,'m23':0,'m33':90,'m43':90}
                    self.my_robot.goto_position(mapos, duration=0.3, wait=True)                 
                print ("left")

                mapos={'m41':-30,'m42':40,'m21':90,'m22':125}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True)   
                #time.sleep(0.1) 
                mapos={'m31':-30,'m32':40,'m11':90,'m12':125}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True)   
                mapos={'m21':0,'m22':90,'m23':0,'m41':0,'m42':90,'m43':90}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
                #mapos={'m21':30}
                #self.my_robot.goto_position(mapos, duration=0.1, wait=True)  
                mapos={'m11':-30,'m12':40,'m31':90,'m32':125}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
                mapos={'m21':-30,'m22':40,'m41':90,'m42':125}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
                #time.sleep(0.1)
                 
                mapos={'m11':0,'m12':90,'m13':0,'m31':0,'m32':90,'m33':90}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True)
                self.previous=3;

def AraigneeRight(self):
                '''Make the  spider slowly turn to the  Right'''

                time.sleep(0.2)
                if(self.previous!=2): 
                    mapos={'m13':90,'m23':90,'m33':0,'m43':0}
                    self.my_robot.goto_position(mapos, duration=0.3, wait=True)   

              
                mapos={'m41':-30,'m42':40,'m21':90,'m22':125}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True)   
                #time.sleep(0.1) 
                mapos={'m31':-30,'m32':40,'m11':90,'m12':125}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True)   
                mapos={'m21':0,'m22':90,'m23':90,'m41':0,'m42':90,'m43':0}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
                #mapos={'m21':30}
                #self.my_robot.goto_position(mapos, duration=0.1, wait=True)  
                mapos={'m11':-30,'m12':40,'m31':90,'m32':125}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
                mapos={'m21':-30,'m22':40,'m41':90,'m42':125}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
                #time.sleep(0.1)
                 
                mapos={'m11':0,'m12':90,'m13':90,'m31':0,'m32':90,'m33':0}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True)
                 
                self.previous=2;

def AraigneeUp(self):
                
                '''Move the spider up'''
                time.sleep(0.2)

                if(self.previous!=1): 
                    mapos={'m13':90,'m23':90,'m33':90,'m43':90}
                    self.my_robot.goto_position(mapos, duration=0.3, wait=True)   

                mapos={'m41':-30,'m42':40,'m21':90,'m22':125}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True)   
                #time.sleep(0.1) 
                mapos={'m31':-30,'m32':40,'m11':90,'m12':125}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True)   
                mapos={'m21':0,'m22':90,'m23':90,'m41':0,'m42':90,'m43':90}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
                #mapos={'m21':30}
                #self.my_robot.goto_position(mapos, duration=0.1, wait=True)  
                mapos={'m11':-30,'m12':40,'m31':90,'m32':125}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
                mapos={'m21':-30,'m22':40,'m41':90,'m42':125}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True) 
                #time.sleep(0.1)
                 
                mapos={'m11':0,'m12':90,'m13':90,'m31':0,'m32':90,'m33':90}
                self.my_robot.goto_position(mapos, duration=0.15, wait=True)  
                #mapos={'m31':30}
                #self.my_robot.goto_position(mapos, duration=0.1, wait=True)                
  
                self.previous=1;                
def AraigneeChange(self):
            
             '''Change to a spider form'''
             self.my_robot.compliant=False
             mapos={'m11':90,'m12':0,'m13':25,'m21':90,'m22':0,'m23':25,
                  'm31':self.listepos[6],'m32':self.listepos[7],'m33':25,'m41':self.listepos[9],'m42':self.listepos[10],'m43':25}
             self.my_robot.goto_position(mapos, duration=0.7, wait=True)  
    
             mapos={'m11':0,'m12':90,'m13':25,'m21':0,'m22':90,'m23':25,
               'm31':self.listepos[6],'m32':self.listepos[7],'m33':25,'m41':self.listepos[9],'m42':self.listepos[10],'m43':25}
             self.my_robot.goto_position(mapos, duration=0.7, wait=True)  

             mapos={'m11':0,'m12':90,'m13':25,'m21':0,'m22':90,'m23':25,
              'm31':self.listepos[6],'m32':self.listepos[7],'m33':25,'m41':self.listepos[9],'m42':self.listepos[10],'m43':25}
             self.my_robot.goto_position(mapos, duration=0.7, wait=True)  

             mapos={'m11':0,'m12':90,'m13':25,'m21':0,'m22':90,'m23':25,
              'm31':90,'m32':0,'m33':25,'m41':90,'m42':0,'m43':25}
             self.my_robot.goto_position(mapos, duration=0.7, wait=True)  

             mapos={'m11':0,'m12':90,'m13':25,'m21':0,'m22':90,'m23':25,
              'm31':0,'m32':90,'m33':25,'m41':0,'m42':90,'m43':25}
             self.my_robot.goto_position(mapos, duration=0.7, wait=True)  
             self.serpent=False
             self.CommandPrompt.setHtml('''<html><body>Mode Araignee!!<br>Z:Avancer<br>Q:Gauche    A:Lateral Gauche<br>D:Droite   E:Lateral Droite<br>S:Bas <br>L:Led Play</body></html''')