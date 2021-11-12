# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 11:51:28 2021

@author: asus
"""


from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog
from skimage.io import imread
from skimage.color import rgb2grey
from skimage.filters import threshold_mean
import numpy as np
import cv2
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB 
import timeit


gauss=''
berno=''
multin=''
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        

        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(900, 300, 181, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton"
                                      "{"
                                      
                                      "}"
                                      "QPushButton::pressed"
                                      "{"
                                      "background-color:white;"
                                      "}"
                                      )
        
        
        
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(470, 630, 181, 31))
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.setStyleSheet(
                                      "{"
                                      
                                      "}"
                                     
                                      "{"
                                      "background-color:white;"
                                      "}"
                                      )
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(470, 680, 181, 31))
        self.pushButton3.setObjectName("pushButton")
        self.pushButton3.setStyleSheet("QPushButton"
                                      "{"
                                      
                                      "}"
                                      "QPushButton::pressed"
                                      "{"
                                      "background-color:white;"
                                      "}"
                                      )
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(470, 730, 181, 31))
        self.pushButton4.setObjectName("pushButton")
        self.pushButton4.setStyleSheet("QPushButton"
                                      "{"
                                      
                                      "}"
                                      "QPushButton::pressed"
                                      "{"
                                      "background-color:white;"
                                      "}"
                                      )
        #****** label *****
        self.ImageOrigine = QtWidgets.QLabel(self.centralwidget)
        self.ImageOrigine.setGeometry(QtCore.QRect(350, 370, 450, 231))
        self.ImageOrigine.setText("")
        self.ImageOrigine.setObjectName("label_3")
        

        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 10, 911, 81))
        font=QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(440, 760, 351, 131))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        font=QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label")
        
        
        #***label table***
        self.labe1 = QtWidgets.QLabel(self.centralwidget)
        self.labe1.setGeometry(QtCore.QRect(50, 80, 140, 51))
        self.labe1.setStyleSheet("border: 1px solid black;padding:10px")
        font=QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        font.setWeight(75)
        self.labe1.setFont(font)
        self.labe1.setObjectName("label")
        
        self.labe2 = QtWidgets.QLabel(self.centralwidget)
        self.labe2.setGeometry(QtCore.QRect(190, 80, 210, 51))
        self.labe2.setStyleSheet("border: 1px solid black;padding:10px")
        font=QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        font.setWeight(75)
        self.labe2.setFont(font)
        self.labe2.setObjectName("label")
        
        self.labe3 = QtWidgets.QLabel(self.centralwidget)
        self.labe3.setGeometry(QtCore.QRect(400, 80, 300, 51))
        self.labe3.setStyleSheet("border: 1px solid black;padding:10px")
        font=QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        font.setWeight(75)
        self.labe3.setFont(font)
        self.labe3.setObjectName("label")
        
        self.labe4 = QtWidgets.QLabel(self.centralwidget)
        self.labe4.setGeometry(QtCore.QRect(700, 80, 300, 51))
        self.labe4.setStyleSheet("border: 1px solid black;padding:10px")
        font=QtGui.QFont()
        font.setPointSize(7)
        font.setItalic(True)
        font.setWeight(75)
        self.labe4.setFont(font)
        self.labe4.setObjectName("label")
        
        self.labe5 = QtWidgets.QLabel(self.centralwidget)
        self.labe5.setGeometry(QtCore.QRect(50, 130, 140, 51))
        self.labe5.setStyleSheet("border: 1px solid black; padding:10px")
        font=QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        font.setWeight(75)
        self.labe5.setFont(font)
        self.labe5.setObjectName("label")
        
        self.labe6 = QtWidgets.QLabel(self.centralwidget)
        self.labe6.setGeometry(QtCore.QRect(190, 130, 210, 51))
        self.labe6.setStyleSheet("border: 1px solid black;")
        font=QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        font.setWeight(45)
        self.labe6.setFont(font)
        self.labe6.setObjectName("label")
        
        self.labe7 = QtWidgets.QLabel(self.centralwidget)
        self.labe7.setGeometry(QtCore.QRect(400,130, 300, 51))
        self.labe7.setStyleSheet("border: 1px solid black;")
        font=QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        font.setWeight(45)
        self.labe7.setFont(font)
        self.labe7.setObjectName("label")
        
        self.labe8 = QtWidgets.QLabel(self.centralwidget)
        self.labe8.setGeometry(QtCore.QRect(700, 130, 300, 51))
        self.labe8.setStyleSheet("border: 1px solid black;")
        font=QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        font.setWeight(45)
        self.labe8.setFont(font)
        self.labe8.setObjectName("label")
        
        self.labe9 = QtWidgets.QLabel(self.centralwidget)
        self.labe9.setGeometry(QtCore.QRect(50, 180, 140, 51))
        self.labe9.setStyleSheet("border: 1px solid black;padding:10px")
        font=QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        font.setWeight(75)
        self.labe9.setFont(font)
        self.labe9.setObjectName("label")
        
        self.labe10= QtWidgets.QLabel(self.centralwidget)
        self.labe10.setGeometry(QtCore.QRect(190, 180, 210, 51))
        self.labe10.setStyleSheet("border: 1px solid black;")
        font=QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        font.setWeight(45)
        self.labe10.setFont(font)
        self.labe10.setObjectName("label")
        
        self.labe11 = QtWidgets.QLabel(self.centralwidget)
        self.labe11.setGeometry(QtCore.QRect(400, 180, 300, 51))
        self.labe11.setStyleSheet("border: 1px solid black;")
        font=QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        font.setWeight(45)
        self.labe11.setFont(font)
        self.labe11.setObjectName("label")
        
        self.labe12 = QtWidgets.QLabel(self.centralwidget)
        self.labe12.setGeometry(QtCore.QRect(700, 180, 300, 51))
        self.labe12.setStyleSheet("border: 1px solid black;")
        font=QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        font.setWeight(45)
        self.labe12.setFont(font)
        self.labe12.setObjectName("label")
        
        self.labe13 = QtWidgets.QLabel(self.centralwidget)
        self.labe13.setStyleSheet("border: 1px solid black;padding:10px")
        self.labe13.setGeometry(QtCore.QRect(50, 230, 140, 51))
        font=QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        font.setWeight(75)
        self.labe13.setFont(font)
        self.labe13.setObjectName("label")
        
        self.labe14 = QtWidgets.QLabel(self.centralwidget)
        self.labe14.setGeometry(QtCore.QRect(190, 230, 210, 51))
        self.labe14.setStyleSheet("border: 1px solid black;")
        font=QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        font.setWeight(45)
        self.labe14.setFont(font)
        self.labe14.setObjectName("label")
        
        self.labe15 = QtWidgets.QLabel(self.centralwidget)
        self.labe15.setGeometry(QtCore.QRect(400, 230, 300, 51))
        self.labe15.setStyleSheet("border: 1px solid black;")
        font=QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        font.setWeight(45)
        self.labe15.setFont(font)
        self.labe15.setObjectName("label")
        
        self.labe16 = QtWidgets.QLabel(self.centralwidget)
        self.labe16.setGeometry(QtCore.QRect(700, 230, 300, 51))
        self.labe16.setStyleSheet("border: 1px solid black;")
        font=QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        font.setWeight(45)
        self.labe16.setFont(font)
        self.labe16.setObjectName("label")
        
        
        
        
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        


        
       
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reconnaissance des Images"))
               
        self.pushButton.setText(_translate("MainWindow", "Ouvrir image"))
        self.pushButton2.setText(_translate("MainWindow", "Gaussian"))
        self.pushButton3.setText(_translate("MainWindow", "Bernoulli"))
        self.pushButton4.setText(_translate("MainWindow", "Multinomial"))
        self.label.setText(_translate("MainWindow", "Comparaison Bayes Naîf:"))
        
        
        self.labe1.setText(_translate("MainWindow", "Classifier"))
        self.labe2.setText(_translate("MainWindow", "Temps d'execution"))
        self.labe3.setText(_translate("MainWindow", "Taux de reconnaissance %"))
        self.labe4.setText(_translate("MainWindow", "Précision de la classification sur le test"))
        self.labe5.setText(_translate("MainWindow", "Gaussian"))
        self.labe6.setText(_translate("MainWindow", str(t_g.timeit(1))))
        self.labe7.setText(_translate("MainWindow", str(gauss.score(x1,y1)*100)))
        self.labe8.setText(_translate("MainWindow", str(gauss.score(x2,y2)*100)))
        self.labe9.setText(_translate("MainWindow", "Bernoulli"))
        self.labe10.setText(_translate("MainWindow",str(t_b.timeit(1))))
        self.labe11.setText(_translate("MainWindow", str(berno.score(x1,y1)*100)))
        self.labe12.setText(_translate("MainWindow", str(berno.score(x2,y2)*100)))
        self.labe13.setText(_translate("MainWindow", "Multinomial"))
        self.labe14.setText(_translate("MainWindow", str(t_m.timeit(1))))
        self.labe15.setText(_translate("MainWindow", str(multin.score(x1,y1)*100)))
        self.labe16.setText(_translate("MainWindow", str(multin.score(x2,y2)*100)))
        self.pushButton.clicked.connect(self.openFile)
        self.pushButton2.clicked.connect(self.Gaussien)
        self.pushButton3.clicked.connect(self.bern)
        self.pushButton4.clicked.connect(self.multinm)
       
       
      
    def openFile(self):

        nom_fichier = QFileDialog.getOpenFileName(None, 'Open file', '', "Image files (*.BMP *.jpg *.gif *.png)")
        self.path = nom_fichier[0]
        pathx = self.path
        pixmap = QtGui.QPixmap(pathx)
        imageTestRGB = imread(self.path)
        imageTest = rgb2grey(imageTestRGB)
        thresh = threshold_mean(imageTest)
        binaryTest = imageTest > thresh
        binaryTest = binaryTest * 1
        self.imageTest = np.ravel(binaryTest)
        self.ImageOrigine.setPixmap(pixmap)
        self.ImageOrigine.setScaledContents(1)

        
    def Gaussien(self):
        y_predg = gauss.predict([self.imageTest])
        y_predg = np.int(y_predg[0])
        self.label_7.setText("Resultat gaussian : " + alphabet[y_predg - 1])


   
    def bern(self):
        y_predb = berno.predict([self.imageTest])
        y_predb = np.int(y_predb[0])
        self.label_7.setText("Resultat bernoulli : " + alphabet[y_predb - 1])
        
        
    
    def multinm(self):
        y_predm = multin.predict([self.imageTest])
        y_predm = np.int(y_predm[0])
        self.label_7.setText("Resultat multinomial : " + alphabet[y_predm - 1])


def gaussian(images,y):
       global gauss
       gauss = GaussianNB()
       gauss.fit(images,y)
       return gauss
   
def bernoulli(images,y):
       global berno
       berno = BernoulliNB(alpha=0.01)
       berno.fit(images,y)
       return berno
   
def multinomial(images,y):
       global multin
       multin = MultinomialNB(alpha=0.5)
       multin.fit(images,y)   
       return multin
       



def charger_images():

 # 5a-3b-3c-2d-3e-3f-2g-3h-4i-3j-2k-2l-2m-3n-3o-3p-2q-2r-3s-2t-3u-2v-2w-2x-2y-2z
 y = np.array([1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26])
 images = []
 for i in range(1, 63):
     img = "C:/Users/asus/Desktop/master_sir/s8/TAAD/tp3/images/apprentissage/"+str(i)+".png"
     imageRGB = imread(img)
     #rendre les images binaires
     image = rgb2grey(imageRGB)
     thresh = threshold_mean(image)
     binary = image > thresh
     binary = binary * 1
     images.append(np.ravel(binary))
     
       
 return images, y
      
      
      
def temp_Apprendre()  :     
       temp_gauss = timeit.Timer('gaussian(x1,y1)','from __main__ import gaussian, x1, y1')

       temp_ber = timeit.Timer('bernoulli(x1,y1)','from __main__ import bernoulli, x1, y1')
     
       temp_multi = timeit.Timer('multinomial(x1,y1)','from __main__ import multinomial, x1, y1')
       
       return temp_gauss,temp_ber,temp_multi
       
       
 
     




def image_test():
 images=[]
 y = np.array([1,1,2,2,3,3,4,4,5,5,6,6,7,8,8,9,9,10,10,11,12,13,13,14,14,15,15,16,16,17,18,19,19,20,21,21,22,23,24,25,26])

 for i in range(1,42):
     img = "C:/Users/asus/Desktop/master_sir/s8/TAAD/tp3/images/TEST/"+str(i)+".png"
     
          
     img = cv2.imread(img,0)
          
     th2 = cv2.adaptiveThreshold(img,1,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
                
     Xi=th2.flatten()
     images.append(Xi)
     
 return images, y
    

        
    
    
if __name__ == "__main__":
    import sys
    
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]


    x1, y1 = charger_images()
    x2, y2 = image_test()
    
    gauss=gaussian(x1,y1)
    berno=bernoulli(x1,y1)
    multin=multinomial(x1,y1)

    t_g,t_b,t_m=temp_Apprendre()
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_()) 


