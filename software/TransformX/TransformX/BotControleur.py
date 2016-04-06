#!/usr/bin/python
 
from PyQt4 import QtGui, QtCore
from pypot.dynamixel import *
from pypot.dynamixel import autodetect_robot
from PyQt4.QtCore import SIGNAL
from enum import Enum

import sys
sys.path.insert(0, 'DepPrimitive')
sys.path.insert(0, 'ProgrammationMimetiqueVisuelle')
from SpecialMove import *
from AraigneePython import *
from SnakePython import *
from Enregistrement import *
from SaveWindows import *
import pickle
import view
import time
from pypot.dynamixel.io import io_320
from pypot.robot import *
from pypot.primitive.move import *

class BotControl(QtGui.QMainWindow, view. Ui_VueDevellopeur):
    '''This class connect the action to the different boutton of the interface'''
    previous=0 #Variable qui permet de memoriser la dernier touche tapper par l'utilisateur, elle permet d'epurer les deplacement
    #my_robot = from_json('monrobot.json')#Generation du robot a partir du json
    vitesse=1.00#Vitesse de base du robot
    listepos=[0, 0, 0, 0, 0, 0,0,0,0,0,0,0]
    serpent=False#Variable permettant de memoriser la forme du robot serpent=true <=> Deplacement venant des primitives de SnakePython.py

    
    count_positions = 0#Variable utile a la PMV, elle permet de memoriser le nombre de mouvement saisie par l'utilisateur
        
    wind2=None
    
    my_robot=None
    #"""description of class"""
    def __init__(self,my_robot=None,parent=None):
        
        self.my_robot=my_robot
        self.my_robot.compliant = False

        #Appelle au constructeur du père qui est chargé de la vue de la fenetre     
        super(BotControl, self).__init__(parent)
        #Lancement de la fenetre
        self.setupUi(self)

        #vider lES fichierS temporaires
        file_move = open("MyMovement/file_move.txt", "wb")
        file_move.close()
        file_move2 = open("MyMovement/file_move2.txt", "wb")
        file_move2.close()
        self.ChargementListeDesMouvements();

        self.CommandPrompt.setHtml('''<html><body>Mode Araignee!!<br>Z:Avancer<br>Q:Gauche   A:Lateral Gauche<br>D:Droite   E:Lateral Droite<br>S:Bas<br>L:Led Play </body></html''')
       
        #Affichage des positions initiales du robot
        self.my_robot.compliant=True
        self.MotorChange.setValue(self.my_robot.m11.present_position)
        self.Motor2Change.setValue(self.my_robot.m12.present_position)
        self.Motor3Change.setValue(self.my_robot.m13.present_position)
        self.Motor4Change.setValue(self.my_robot.m21.present_position)
        self.Motor5Change.setValue(self.my_robot.m22.present_position)
        self.Motor6Change.setValue(self.my_robot.m23.present_position)
        self.Motor7Change.setValue(self.my_robot.m31.present_position)
        self.Motor8Change.setValue(self.my_robot.m32.present_position)
        self.Motor9Change.setValue(self.my_robot.m33.present_position)
        self.Motor10Change.setValue(self.my_robot.m41.present_position)
        self.Motor11Change.setValue(self.my_robot.m42.present_position)
        self.Motor12Change.setValue(self.my_robot.m43.present_position)
        self.Vitessenum.setValue(1.00)
        self.my_robot.compliant=False

        self.connectActions()
    #Ajoute des fonctions a nos boutons
    def connectActions(self):
        

       '''This fonction connect action to the different action they produce '''
        
       self.comboBox.activated[str].connect(self.onActivated) 

       self.pushButton.clicked.connect(self.releasemotor)
       self.pushButton_2.clicked.connect(self.deplacement)
       self.DebutEnregistrementBoutton.clicked.connect(self.BeginSave)
       self.FinEnregistrementBoutton.clicked.connect(self.EndSave)
       self.GetCurrentPosition_btn.clicked.connect(self.getcurrentaction)
       self.Changementdeforme.clicked.connect(self.Changementdeformes)
       self.EnregistrerPosition.clicked.connect(self.WriteFile)
       self.ColorCombo.activated[str].connect(self.onColorActivated)
       
 #Fonction de switch entre Araignee et Serpent
    def Changementdeformes(self):
         '''Load the different primitive fonction of transformation'''
         if self.serpent==True:
             
             AraigneeChange(self)

         elif self.serpent==False:

             SnakeChange(self)
          
    def getcurrentaction(self):
        (self.onColorActivated)
        
        self.MotorChange.setValue(self.my_robot.m11.present_position)
        self.Motor2Change.setValue(self.my_robot.m12.present_position)
        self.Motor3Change.setValue(self.my_robot.m13.present_position)
        self.Motor4Change.setValue(self.my_robot.m21.present_position)
        self.Motor5Change.setValue(self.my_robot.m22.present_position)
        self.Motor6Change.setValue(self.my_robot.m23.present_position)
        self.Motor7Change.setValue(self.my_robot.m31.present_position)
        self.Motor8Change.setValue(self.my_robot.m32.present_position)
        self.Motor9Change.setValue(self.my_robot.m33.present_position)
        self.Motor10Change.setValue(self.my_robot.m41.present_position)
        self.Motor11Change.setValue(self.my_robot.m42.present_position)
        self.Motor12Change.setValue(self.my_robot.m43.present_position)


        
    def BeginSave(self):
         '''Load the fonction of begin the recording'''

         saveOn(self)

    def EndSave(self):
        '''Load the fonction who End the recording and save it'''

        saveOf(self)


    def WriteFile(self):
        '''Load the fonction who write one deplacement'''
        writeInFile(self)

 #Relachement des moteurs
    def releasemotor(self):
        '''Simply release the motor'''

        print("relachement des moteurs")
        self. my_robot.compliant = True


        print("relachement terminé")

    def deplacement(self):
        '''Base deplacement of the motor regarding the position of motor angle value Box'''

        self.my_robot.compliant = False

        self.listepos[0]=self.MotorChange.value()
        self.listepos[1]=self.Motor2Change.value()
        self.listepos[2]=self.Motor3Change.value()
        self.listepos[3]=self.Motor4Change.value()
        self.listepos[4]=self.Motor5Change.value()
        self.listepos[5]=self.Motor6Change.value()
        self.listepos[6]=self.Motor7Change.value() 
        self.listepos[7]=self.Motor8Change.value() 
        self.listepos[8]=self.Motor9Change.value()      
        self.listepos[9]=self.Motor10Change.value() 
        self.listepos[10]=self.Motor11Change.value() 
        self.listepos[11]=self.Motor12Change.value() 
        mapos={'m11':self.listepos[0],'m12':self.listepos[1],'m13':self.listepos[2],'m21':self.listepos[3],'m22':self.listepos[4],'m23':self.listepos[5],
               'm31':self.listepos[6],'m32':self.listepos[7],'m33':self.listepos[8],'m41':self.listepos[9],'m42':self.listepos[10],'m43':self.listepos[11]}
        self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True)  



#FONCTIONEVENEMENT CLAVIER
    def keyPressEvent(self, event):
        '''Handle the different keyboard event such as ZQSD(WASD) deplacement'''
        print("ca marche")
        self.my_robot.compliant = False

       

        if event.key() == QtCore.Qt.Key_Z: 
            print ("UP")
            #Deplacement SERPENT
            if self.serpent==True:
                    SnakeUp(self)
            if self.serpent==False:
                    AraigneeUp(self)
               
        if event.key() == QtCore.Qt.Key_D: 


            if self.serpent==True:
                    
                SnakeRight(self)

            if self.serpent==False:
                
                AraigneeRight(self)


        if event.key() == QtCore.Qt.Key_Q:

            
            if self.serpent==True:
                
                SnakeLeft(self)


            if self.serpent==False:   
                 
              AraigneeLeft(self)

        if event.key() == QtCore.Qt.Key_S: 
            
            print ("down")
            if self.serpent==True:
                    
                SnakeDown(self)
             
            if self.serpent==False:
                
                AraigneeDown(self)

        if event.key() == QtCore.Qt.Key_A: 
               
         if self.serpent==False:

                AraigneeSideLeft(self)

        if event.key() == QtCore.Qt.Key_E: 
                
            if self.serpent==False:

                AraigneeSideRight(self)
    
        if event.key() == QtCore.Qt.Key_R: 
          
            climb(self)

        if event.key() == QtCore.Qt.Key_T: 

            retourner(self)
        if event.key() == QtCore.Qt.Key_L: 
           
            XL320LEDColors = Enum('Colors', 'off red green yellow '
                      'blue pink cyan white')
            y=0
            while(y<9):
                y=y+1
                z=y
                for m in self.my_robot.motors:
                          
                          
                           z=z+1
                           if(z>8):
                               z=1
                           m.led=XL320LEDColors(z).name
                           
                time.sleep(self.Vitessenum.value())
            for m in self.my_robot.motors:
                          m.led="cyan"

            #time.sleep(self.Vitessenum.value())
            #for m in self.my_robot.motors:
            #              m.led="off"
            

    def ChargementListeDesMouvements(self):
        self.comboBox.clear()
        count=True
        f=open('ListeDesMouvements.txt','r')
        for line in f:
               for word in line.split():
                  print(word) 
                  
                  if(count==True):self.comboBox.addItem(word)
                  count=not count
        f.close()


    def onActivated(self, text):
        '''This fonction is activate each time you select a movement on the combobox'''
        nom="%s.txt" % text
        print(nom)
        readFile(self,nom)
        


    def onColorActivated(self,text):
      for m in self.my_robot.motors:
        m.led=text



    def actu(self,x):
        '''Update the scrollBar with the new movement and free the temp file'''
        
        self.ChargementListeDesMouvements()
        self.count_positions=0

        #vider lES fichierS temporaires
        file_move = open("MyMovement/file_move.txt", "wb")
        file_move.close()
        file_move2 = open("MyMovement/file_move2.txt", "wb")
        file_move2.close()        

    def main(self):
        self.show()

  
