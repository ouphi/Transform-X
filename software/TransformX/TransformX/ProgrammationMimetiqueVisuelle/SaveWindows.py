
#!/usr/bin/python
import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import SIGNAL
import os 
import sys
import view
import time

class SaveWindowsF(QtGui.QWidget):
      '''This class is an additional windows who permit to save the move you create'''

      def __init__(self, parent=None):
        super(SaveWindowsF, self).__init__(parent)
        self.setWindowTitle(u"Quel client")
        
        # créer un lineEdit
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setText("DonnerUnNom")
        # créer un bouton
        self.bouton = QtGui.QPushButton(u"Ok", self)
        self.bouton.clicked.connect(self.ok_m)
        # positionner les widgets dans la fenêtre
        posit = QtGui.QGridLayout()
        posit.addWidget(self.lineEdit, 0, 0)
        posit.addWidget(self.bouton, 1, 0)
        self.setLayout(posit)
 
      def ok_m(self):
        '''Handle the action when we click on the ok button'''
        # emettra un signal "SaveWindowscloset()" avec l'argument cité
        # fermer la fenêtre
        monnom=self.lineEdit.text()
        if(monnom!="DonnerUnNom "and os.path.exists("MyMovement/"+monnom+".txt")==0):
            os.rename("MyMovement/file_move2.txt","MyMovement/"+ monnom+".txt")
            file_move = open("ListeDesMouvements.txt", "a")
            file_move.write("\n"+ monnom+" "+ monnom +".txt") # python will convert \n to os.linesep
            file_move.close() # you can omit in most cases as the destructor will call it
            self.emit(SIGNAL("fermeture(PyQt_PyObject)"), 1) 

        else :print("error")
        self.close()