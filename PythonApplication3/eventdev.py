#!/usr/bin/python
 
from PyQt4 import QtGui, QtCore
from pypot.dynamixel import *
from pypot.dynamixel import autodetect_robot


import sys
import pickle
import view
import time
from pypot.robot import from_json
from pypot.primitive.move import MoveRecorder, Move, MovePlayer
        

class eventviewdev(QtGui.QMainWindow, view. Ui_VueDevellopeur):

    my_robot = from_json('monrobot.json')
    vitesse=2.00
    listepos=[0, 0, 0, 0, 0, 0,0,0,0,0,0,0]
    serpent=False
    move_recorder = MoveRecorder(my_robot, 1, my_robot.motors)
    my_robot.compliant = False
    count_positions = 0
    #my_robot.m11.goto_position(40, duration=2, wait=True)
    #my_robot.m21.goto_position(40, duration=2, wait=True)  
   # my_robot.m22.goto_position(90, duration=1, wait=False)  
   # my_robot.m41.goto_position(40, duration=2, wait=False)
     
 
    time.sleep(1)

    #"""description of class"""
    def __init__(self, parent=None):

        #vider le fichier
        file_move = open("file_move.txt", "wb")
        file_move.close()
            
        super(eventviewdev, self).__init__(parent)
        self.setupUi(self)
        

        self.CommandPrompt.setHtml('''<html><body>hello!<br>Chargement de l'interface terminé!</body></html''')
       
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
        self.Vitessenum.setValue(2.00)
        self.my_robot.compliant=False
        #print(my_robot.m12.present_position)
        #print(my_robot.m13.present_position)
        #print(my_robot.m31.present_position)
        #print(my_robot.m32.present_position)
        #print(my_robot.m33.present_position)
       
        

        #idm = self.dxl_io.scan(range(50))
        #print(idm)
           
        self.connectActions()

    def connectActions(self):
    
       #self.motor1Change.valueChanged[int].connect(self.motoranglechange)
       #self.motor2Change.valueChanged.connect(self.motoranglechange(1))
       #self.motor3Change.valueChanged.connect(self.motoranglechange(2))
       #self.motor4Change.valueChanged.connect(self.motoranglechange(3))
       #self.motor5Change.valueChanged.connect(self.motoranglechange(4))
       #self.motor6Change.valueChanged.connect(self.motoranglechange(5))
       #self.Vitessenum.valueChanged.connect(self.vitesseChange)
       self.pushButton.clicked.connect(self.closemotor)
       self.pushButton_2.clicked.connect(self.deplacement)
       self.DebutEnregistrementBoutton.clicked.connect(self.saveOn)
       self.FinEnregistrementBoutton.clicked.connect(self.saveOf)
       self.GetCurrentPosition_btn.clicked.connect(self.getcurrentaction)
       self.Changementdeforme.clicked.connect(self.Changementdeformes)
       self.EnregistrerPosition.clicked.connect(self.writeInFile)
       

    def Changementdeformes(self):
        
         if self.serpent==True:
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

         elif self.serpent==False:

             self.my_robot.compliant=False
             mapos={'m11':90,'m12':0,'m13':0,'m21':90,'m22':90,'m23':0,
                  'm31':self.listepos[6],'m32':90,'m33':0,'m41':self.listepos[9],'m42':0,'m43':0}
             self.my_robot.goto_position(mapos, duration=1, wait=True)  
    
             mapos={'m11':0,'m12':0,'m13':0,'m21':0,'m22':0,'m23':0,
               'm31':self.listepos[6],'m32':0,'m33':0,'m41':self.listepos[9],'m42':0,'m43':0}
             self.my_robot.goto_position(mapos, duration=1, wait=True)  
             self.serpent=True
             #mapos={'m11':0,'m12':90,'m13':0,'m21':0,'m22':90,'m23':0,
             # 'm31':self.listepos[6],'m32':self.listepos[7],'m33':0,'m41':self.listepos[9],'m42':self.listepos[10],'m43':0}
             #self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True)  

             #mapos={'m11':0,'m12':90,'m13':25,'m21':0,'m22':90,'m23':0,
             # 'm31':90,'m32':0,'m33':0,'m41':90,'m42':0,'m43':0}
             #self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True)  

             #mapos={'m11':0,'m12':90,'m13':0,'m21':0,'m22':90,'m23':0,
             # 'm31':0,'m32':90,'m33':0,'m41':0,'m42':90,'m43':0}
             #self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True)  
             #self.serpent=False


    def getcurrentaction(self):

        print(self.my_robot.m11.present_position)
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

    def writeInFile(self):
        file_move = open("file_move.txt", "ab")
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
      
        
    

    def readFile(self):
         self.my_robot.compliant=False
         print(self.count_positions)
         file_move = open("file_move.txt", "rb")
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
         
    def saveOn(self):
         self.my_robot.compliant = True
         self.closemotor()
         #self.move_recorder.start()
         



    def saveOf(self):
        self.readFile()
        #print("")
        #self.move_recorder.stop()
        #with open('enregistremnent.json', 'w') as f:
        #    self.move_recorder.move.save(f)

        self.my_robot.compliant = False
        #with open('temp.json') as f:
        #     m = Move.load(f)
        #print(m)
        #move_player = MovePlayer(self.my_robot, m)
        #move_player.start()


    def closemotor(self):

        print("relachement des moteurs")
        self. my_robot.compliant = True
        #self.my_robot.close()

        print("relachement terminé")

    def deplacement(self):

        self.my_robot.compliant = False
        #self.vitesse=self.Vitessenum.value()
       # print(self.vitesse)
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
        #self.dxl_io.set_goal_position({41: self.listepos[0]})


        #while 1==1 :
        # mapos={'m11':0,'m12':8,'m13':self.listepos[2],'m28':5,'m23':self.listepos[5],
        #       'm31':120,'m32':8,'m33':self.listepos[8],'m41':120,'m42':8,'m43':self.listepos[11]}
        # self.my_robot.goto_position(mapos, duration=2, wait=True) 
        # mapos={'m11':0,'m12':-40,'m13':self.listepos[2],'m21':0,'m22':-40,'m23':self.listepos[5],
        #       'm31':120,'m32':-40,'m33':self.listepos[8],'m41':120,'m42':-40,'m43':self.listepos[11]}
        # self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True) 
        # mapos={'m11':120,'m12':-40,'m13':self.listepos[2],'m21':120,'m22':-40,'m23':self.listepos[5],
        #       'm31':0,'m32':-40,'m33':self.listepos[8],'m41':0,'m42':-40,'m43':self.listepos[11]}
        # self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True) 
        # mapos={'m11':120,'m12':8,'m13':self.listepos[2],'m21':120,'m22':8,'m23':self.listepos[5],
        #       'm31':0,'m32':8,'m33':self.listepos[8],'m41':0,'m42':8,'m43':self.listepos[11]}
        # self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True) 

       # while 1==1 :
         
       #  self.my_robot.m41.goto_position(-90, duration=0.1, wait=True) 
       #  self.my_robot.m42.goto_position(60, duration=0.1, wait=True) 
       #  self.my_robot.m41.goto_position(30, duration=0.1, wait=True) 
           
       #  self.my_robot.m21.goto_position(90, duration=0.1, wait=True) 
       #  self.my_robot.m22.goto_position(120, duration=0.1, wait=True) 
       #  self.my_robot.m21.goto_position(30, duration=0.1, wait=True) 

       #  self.my_robot.m11.goto_position(-90, duration=0.1, wait=True) 
       #  self.my_robot.m12.goto_position(60, duration=0.1, wait=True) 
       #  self.my_robot.m11.goto_position(30, duration=0.1, wait=True) 
         
       #  self.my_robot.m31.goto_position(90, duration=0.1, wait=True)
       #  self.my_robot.m32.goto_position(120, duration=0.1, wait=True) 
       #  self.my_robot.m31.goto_position(30, duration=0.1, wait=True) 

       #  mapos={'m11':0,'m12':90,'m13':90,'m21':0,'m22':90,'m23':90,
       #  'm31':0,'m32':90,'m33':90,'m41':0,'m42':90,'m43':90}
       #  self.my_robot.goto_position(mapos, duration=self.Vitessenum.value(), wait=True)  
       ##self.dxl_io.set_goal_position({12: self.listepos[1]})
        #self.dxl_io.set_goal_position({13: self.listepos[2]})
        #self.dxl_io.set_goal_position({21: self.listepos[3]})
        #self.dxl_io.set_goal_position({22: self.listepos[4]})
        #self.dxl_io.set_goal_position({23: self.listepos[5]})
       
    def openImage(self):
        fileName = QtGui.QFileDialog.getOpenFileName(
                        self,
                        "Ouvrir un fichier d'image",
                        QtCore.QDir.homePath(),
                        "Fichiers d'image (*.jpg, *.jpeg, *.gif, *.png)"
                    )

    def keyPressEvent(self, event):
        print("ca marche")
        if event.key() == QtCore.Qt.Key_Z: 
            print ("UP")
            if self.serpent==True:
                mapos={'m11':0,'m12':20,'m13':self.listepos[2],'m22':20,'m23':self.listepos[5],
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
             
            if self.serpent==False:


                #CAS1
                #self.my_robot.m41.goto_position(-90, duration=0.1, wait=True) 
                #self.my_robot.m42.goto_position(45, duration=0.1, wait=True) 

                #self.my_robot.m41.goto_position(30, duration=0.1, wait=True) 
           
                #self.my_robot.m21.goto_position(90, duration=0.1, wait=True) 
                #self.my_robot.m22.goto_position(125, duration=0.1, wait=True) 
                #self.my_robot.m21.goto_position(30, duration=0.1, wait=True) 

   
                #self.my_robot.m11.goto_position(-90, duration=0.1, wait=True) 
                #self.my_robot.m12.goto_position(45, duration=0.1, wait=True) 
                #self.my_robot.m11.goto_position(30, duration=0.1, wait=True) 
         
                #self.my_robot.m31.goto_position(90, duration=0.1, wait=True)
                #self.my_robot.m32.goto_position(125, duration=0.1, wait=True) 
                #self.my_robot.m31.goto_position(30, duration=1.1, wait=True) 
                #mapos={'m11':0,'m12':90,'m13':90,'m21':0,'m22':90,'m23':90,
                #'m31':0,'m32':90,'m33':90,'m41':0,'m42':90,'m43':90}
                #self.my_robot.goto_position(mapos, duration=0.3, wait=True) 
            
            
            
            
            
            
            
            
            
            
                #CAS2
                #time.sleep(0.5) 
                #mapos={'m41':-90,'m42':20,'m21':90,'m22':125}
                #self.my_robot.goto_position(mapos, duration=0.1, wait=True)   
                ##mapos={'m21':30}
                ##self.my_robot.goto_position(mapos, duration=0.1, wait=True)  
                #mapos={'m11':-90,'m12':20,'m31':90,'m32':125}
                #self.my_robot.goto_position(mapos, duration=0.1, wait=True) 
                
       
                #time.sleep(0.5)  
                #mapos={'m11':0,'m12':90,'m13':90,'m31':0,'m32':90,'m33':90}
                #self.my_robot.goto_position(mapos, duration=0.5, wait=True)  
                ##mapos={'m31':30}
                ##self.my_robot.goto_position(mapos, duration=0.1, wait=True)                
             
                #mapos={'m21':0,'m22':90,'m23':90,'m41':0,'m42':90,'m43':90}
                #self.my_robot.goto_position(mapos, duration=0.5, wait=True) 



                #time.sleep(0.5) 
                #mapos={'m41':-90,'m42':20,'m21':90,'m22':125}
                #self.my_robot.goto_position(mapos, duration=0.1, wait=True)   
                ##mapos={'m21':30}
                ##self.my_robot.goto_position(mapos, duration=0.1, wait=True)  
                #mapos={'m11':-90,'m12':20,'m31':90,'m32':125}
                #self.my_robot.goto_position(mapos, duration=0.1, wait=True) 
                
       
                #time.sleep(0.5) 
                #mapos={'m21':0,'m22':90,'m23':90,'m41':0,'m42':90,'m43':90}
                #self.my_robot.goto_position(mapos, duration=0.5, wait=True)    
                #mapos={'m11':0,'m12':90,'m13':90,'m31':0,'m32':90,'m33':90}
                #self.my_robot.goto_position(mapos, duration=0.5, wait=True)  
                ##mapos={'m31':30}
                ##self.my_robot.goto_position(mapos, duration=0.1, wait=True)                
             
              
          



                ###CAS3
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
  

               
        if event.key() == QtCore.Qt.Key_D: 

                print ("right")
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



        if event.key() == QtCore.Qt.Key_Q:
           
               
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



        if event.key() == QtCore.Qt.Key_S: 
            
                print ("down")

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

    #def motoranglechange(self,valeur):
            
    #    self.listepos[valeur]=3
    #    return 0

    
    #def vitessechange():
            
    #    vitesse = 3

    def main(self):
        self.show()
        #print(self.tab1[0]);
 
  
