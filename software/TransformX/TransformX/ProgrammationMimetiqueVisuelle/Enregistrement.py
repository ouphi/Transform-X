'''This lib is usefull for the recording of mouvement'''
from PyQt4 import QtGui, QtCore
from pypot.dynamixel import *
from PyQt4.QtCore import SIGNAL

import sys
sys.path.insert(0, 'ProgrammationMimetiqueVisuelle')

from SaveWindows import *
import pickle
import view
import time


def readFile(self,nom):
       '''Lit  et execute le mouvement du fichier Texte'''
       y=0;
       while(y!=self.spinBox.value()):
         self.my_robot.compliant=False
         print(self.count_positions)
         file_move = open("MyMovement/"+nom, "rb")
         self.count_positions=pickle.load(file_move)
         print(self.count_positions)
         for x in range(0, self.count_positions):
             #var = pickle.load(file_move)
             print(x)

             mapos={'m11':pickle.load(file_move),'m12':pickle.load(file_move),'m13':pickle.load(file_move),
                     'm21':pickle.load(file_move),'m22':pickle.load(file_move),'m23':pickle.load(file_move),
                  'm31':pickle.load(file_move),'m32':pickle.load(file_move),'m33':pickle.load(file_move),
                  'm41':pickle.load(file_move),'m42':pickle.load(file_move),'m43':pickle.load(file_move)}
             print(mapos)
             self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True) 
         file_move.close() 
         y=y+1

def saveOn(self):
         ''' Relache les moteurs et commence l'enregistrement'''
         self.my_robot.compliant = True
         self.releasemotor()
         #self.move_recorder.start()
         self.count_positions=0
         


def saveOf(self):
      ''' #Fin d'enregistrement du deplacement On sauvegarde dans un filemove2 le nombre de coup+le contenu de file move'''

      file_move = open("MyMovement/file_move.txt", "rb")
      file_move2 = open("MyMovement/file_move2.txt", "wb") 
      pickle.dump(self.count_positions,file_move2)
      for x in range(0, self.count_positions):
        pickle.dump(pickle.load(file_move),file_move2)        
        pickle.dump(pickle.load(file_move),file_move2)
        pickle.dump(pickle.load(file_move),file_move2)
        pickle.dump(pickle.load(file_move),file_move2)
        pickle.dump(pickle.load(file_move),file_move2)
        pickle.dump(pickle.load(file_move),file_move2)
        pickle.dump(pickle.load(file_move),file_move2)
        pickle.dump(pickle.load(file_move),file_move2)
        pickle.dump(pickle.load(file_move),file_move2)
        pickle.dump(pickle.load(file_move),file_move2)
        pickle.dump(pickle.load(file_move),file_move2)
        pickle.dump(pickle.load(file_move),file_move2)

      file_move.close()
      file_move2.close()
      self. wind2 = SaveWindowsF()
      self.connect(self.wind2, SIGNAL("fermeture(PyQt_PyObject)"), self.actu) 
        # la deuxi�me fen�tre sera 'modale' (la premi�re fen�tre sera inactive)
      self.wind2.setWindowModality(QtCore.Qt.ApplicationModal)
        # appel de la deuxi�me fen�tre
      self.wind2.show()
      
       # self.readFile("file_move.txt")
      self.my_robot.compliant = False
      

 #Ecrit dans un fichier Texte
def writeInFile(self):
        file_move = open("MyMovement/file_move.txt", "ab")
        self.getcurrentaction()
        pickle.dump(self.MotorChange.value(),file_move)
        pickle.dump(self.Motor2Change.value(),file_move)
        pickle.dump(self.Motor3Change.value(),file_move)
        pickle.dump(self.Motor4Change.value(),file_move)
        pickle.dump(self.Motor5Change.value(),file_move)
        pickle.dump(self.Motor6Change.value(),file_move)
        pickle.dump(self.Motor7Change.value(),file_move)
        pickle.dump(self.Motor8Change.value(),file_move)
        pickle.dump(self.Motor9Change.value(),file_move)
        pickle.dump(self.Motor10Change.value(),file_move)
        pickle.dump(self.Motor11Change.value(),file_move)
        pickle.dump(self.Motor12Change.value(),file_move)
        self.count_positions = self.count_positions+1
        file_move.close()
       