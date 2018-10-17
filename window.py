# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from clase_poste import *
from clase_disco import *
from clase_jugador import *
from clase_reporte import *
from time import sleep

class Ui_MainWindow(object):
    def __init__(self):
        global ultima_seleccion1
        global ultima_seleccion2
        global validacion_de_juego
        global Y_posicion
        global p1, p2, p3
        global player
        global M
        M = True
        ultima_seleccion1 = 0
        ultima_seleccion2 = 0
        validacion_de_juego = 0
        Y_posicion = (320, 295, 270, 245, 220, 195, 170, 145)
        player = Jugador()
        p1 = Poste(1)
        p2 = Poste(2)
        p3 = Poste(3)

        d1 = Disco(1)
        d2 = Disco(2)
        d3 = Disco(3)
        d4 = Disco(4)
        d5 = Disco(5)
        d6 = Disco(6)
        d7 = Disco(7)
        d8 = Disco(8)

        p1.setDiscos(d8, d7, d6, d5, d4, d3, d2, d1)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 550)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 950, 400))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 70, 30, 275))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(1)
        self.label.setText("")
        self.label.setObjectName("poste1")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(485, 70, 30, 275))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(1)
        self.label.setText("")
        self.label.setObjectName("poste2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(810, 70, 30, 275))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(1)
        self.label.setText("")
        self.label.setObjectName("poste3")

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(155, 145, 40, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label1.setFont(font)
        self.label1.setAutoFillBackground(True)
        self.label1.setFrameShape(QtWidgets.QFrame.Box)
        self.label1.setLineWidth(1)
        self.label1.setText("")
        self.label1.setStyleSheet("QLabel {background-color: gray;}")
        self.label1.setObjectName("disco1")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(140, 170, 70, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label2.setFont(font)
        self.label2.setAutoFillBackground(True)
        self.label2.setFrameShape(QtWidgets.QFrame.Box)
        self.label2.setLineWidth(1)
        self.label2.setText("")
        self.label2.setStyleSheet("QLabel {background-color: gray;}")
        self.label2.setObjectName("disco2")

        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(125, 195, 100, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label3.setFont(font)
        self.label3.setAutoFillBackground(True)
        self.label3.setFrameShape(QtWidgets.QFrame.Box)
        self.label3.setLineWidth(1)
        self.label3.setText("")
        self.label3.setStyleSheet("QLabel {background-color: gray;}")
        self.label3.setObjectName("disco3")

        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(110, 220, 130, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label4.setFont(font)
        self.label4.setAutoFillBackground(True)
        self.label4.setFrameShape(QtWidgets.QFrame.Box)
        self.label4.setLineWidth(1)
        self.label4.setText("")
        self.label4.setStyleSheet("QLabel {background-color: gray;}")
        self.label4.setObjectName("disco4")

        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(95, 245, 160, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label5.setFont(font)
        self.label5.setAutoFillBackground(True)
        self.label5.setFrameShape(QtWidgets.QFrame.Box)
        self.label5.setLineWidth(1)
        self.label5.setText("")
        self.label5.setStyleSheet("QLabel {background-color: gray;}")
        self.label5.setObjectName("disco5")

        self.label6 = QtWidgets.QLabel(self.centralwidget)
        self.label6.setGeometry(QtCore.QRect(80, 270, 190, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label6.setFont(font)
        self.label6.setAutoFillBackground(True)
        self.label6.setFrameShape(QtWidgets.QFrame.Box)
        self.label6.setLineWidth(1)
        self.label6.setText("")
        self.label6.setStyleSheet("QLabel {background-color: gray;}")
        self.label6.setObjectName("disco6")

        self.label7 = QtWidgets.QLabel(self.centralwidget)
        self.label7.setGeometry(QtCore.QRect(65, 295, 220, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label7.setFont(font)
        self.label7.setAutoFillBackground(True)
        self.label7.setFrameShape(QtWidgets.QFrame.Box)
        self.label7.setLineWidth(1)
        self.label7.setText("")
        self.label7.setStyleSheet("QLabel {background-color: gray;}")
        self.label7.setObjectName("disco7")

        self.label8 = QtWidgets.QLabel(self.centralwidget)
        self.label8.setGeometry(QtCore.QRect(50, 320, 250, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label8.setFont(font)
        self.label8.setAutoFillBackground(True)
        self.label8.setFrameShape(QtWidgets.QFrame.Box)
        self.label8.setLineWidth(1)
        self.label8.setText("")
        self.label8.setStyleSheet("QLabel {background-color: gray;}")
        self.label8.setObjectName("disco8")

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(15, 414, 80, 50))#(145, 360, 80, 50)
        self.pushButton1.setObjectName("pushButton1")

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(95, 414, 80, 50))#(470, 360, 80, 50)
        self.pushButton2.setObjectName("pushButton2")

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(175, 414, 80, 50))#(795, 360, 80, 50)
        self.pushButton3.setObjectName("pushButton3")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(13, 460, 150, 32))#330,440
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setEnabled(False)

        self.pushButtonR = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonR.setGeometry(QtCore.QRect(13, 488, 150, 32))
        self.pushButtonR.setObjectName("pushButton_regresar")
        self.pushButtonR.setEnabled(False)

        self.pushButtonM = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonM.setGeometry(QtCore.QRect(160, 461, 60, 60))
        self.pushButtonM.setObjectName("pushButtonM")
        self.pushButtonM.setIcon(QtGui.QIcon(QtGui.QPixmap("iconoM.png")))

        self.NoJugadas = QtWidgets.QLabel(self.centralwidget)
        self.NoJugadas.setGeometry(QtCore.QRect(830, 510, 150, 16))
        self.NoJugadas.setObjectName("NoJugadas")

        self.mensaje_error = QtWidgets.QLabel(self.centralwidget)
        self.mensaje_error.setGeometry(QtCore.QRect(260, 430, 150, 16))
        self.mensaje_error.setStyleSheet("color: red")
        self.mensaje_error.setObjectName("mensaje_error")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 995, 22))
        self.menubar.setObjectName("menubar")
        self.menuTorres = QtWidgets.QMenu(self.menubar)
        self.menuTorres.setObjectName("menuTorres")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuTorres.menuAction())

        self.pushButton.clicked.connect(self.reiniciar_seleccion)
        self.pushButtonR.clicked.connect(self.regresar)
        self.pushButtonM.clicked.connect(lambda: self.tobar(p1))
        self.pushButton1.clicked.connect(lambda: self.funcion_juego(p1))
        self.pushButton2.clicked.connect(lambda: self.funcion_juego(p2))
        self.pushButton3.clicked.connect(lambda: self.funcion_juego(p3))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def funcion_juego(self, poste):
        global validacion_de_juego
        global seleccion1
        global ultima_seleccion1
        global ultima_seleccion2
        global M
        seleccion2 = 0

        if validacion_de_juego == 0:
            if M:
                self.pushButton.setEnabled(True)
            validacion_de_juego += 1
            seleccion1 = poste
            if len(seleccion1.getDiscos()) != 0:
                disco_temp = seleccion1.getDiscos()[-1]
                tamanio_temp = disco_temp.getTamanio()
                if tamanio_temp == 1:
                    self.label1.setStyleSheet("QLabel {background-color: red;}")
                elif tamanio_temp == 2:
                    self.label2.setStyleSheet("QLabel {background-color: red;}")
                elif tamanio_temp == 3:
                    self.label3.setStyleSheet("QLabel {background-color: red;}")
                elif tamanio_temp == 4:
                    self.label4.setStyleSheet("QLabel {background-color: red;}")
                elif tamanio_temp == 5:
                    self.label5.setStyleSheet("QLabel {background-color: red;}")
                elif tamanio_temp == 6:
                    self.label6.setStyleSheet("QLabel {background-color: red;}")
                elif tamanio_temp == 7:
                    self.label7.setStyleSheet("QLabel {background-color: red;}")
                else:
                    self.label8.setStyleSheet("QLabel {background-color: red;}")
        else:
            seleccion2 = poste
            if player.mover_disco(seleccion1, seleccion2):
                self.mensaje_error.setText(" ")

                jugadas_realizadas = len(player.getJugadas())
                self.NoJugadas.setText("Jugadas realizadas: {}".format(jugadas_realizadas))

                disco_temp = seleccion2.getDiscos()[-1]
                tamanio_temp = disco_temp.getTamanio()
                posicion_temp = seleccion2.getDiscos().index(disco_temp)
                if seleccion2 == p1:
                    X = 0
                elif seleccion2 == p2:
                    X = 325
                else:
                    X = 650
                
                Y = Y_posicion[posicion_temp]

                if tamanio_temp == 1:
                    self.label1.move(155 + X, Y)
                elif tamanio_temp == 2:
                    self.label2.move(140 + X, Y)
                elif tamanio_temp == 3:
                    self.label3.move(125 + X, Y)
                elif tamanio_temp == 4:
                    self.label4.move(110 + X, Y)
                elif tamanio_temp == 5:
                    self.label5.move(95 + X, Y)
                elif tamanio_temp == 6:
                    self.label6.move(80 + X, Y)
                elif tamanio_temp == 7:
                    self.label7.move(65 + X, Y)
                else:
                    self.label8.move(50 + X, Y)

                validacion_de_juego = 0
                self.reiniciar_seleccion()
                if M:
                    self.pushButtonR.setEnabled(True)
                self.pushButton.setEnabled(False)
                self.pushButtonM.setEnabled(False)


                ultima_seleccion1 = seleccion1
                ultima_seleccion2 = seleccion2

                if len(p3.getDiscos()) == 8:
                    movimientos = player.getJugadas()
                    PDF = MiReporte("reporte_jugadas")
                    PDF.iniciarReporte()
                    PDF.iniciarTabla()
                    for i in movimientos:
                        PDF.escribirFila(i)
                    PDF.terminarTabla()
                    PDF.terminarReporte()
                    PDF.compilarReporte()
                    subprocess.call(["open", PDF.getNombre().replace('.tex','.pdf')])

            else:
                self.mensaje_error.setText("¡Movimiento invalido!")
                validacion_de_juego = 0
                self.reiniciar_seleccion()

    def reiniciar_seleccion(self):
        global validacion_de_juego
        validacion_de_juego = 0
        self.label1.setStyleSheet("QLabel {background-color: gray;}")
        self.label2.setStyleSheet("QLabel {background-color: gray;}")
        self.label3.setStyleSheet("QLabel {background-color: gray;}")
        self.label4.setStyleSheet("QLabel {background-color: gray;}")
        self.label5.setStyleSheet("QLabel {background-color: gray;}")
        self.label6.setStyleSheet("QLabel {background-color: gray;}")
        self.label7.setStyleSheet("QLabel {background-color: gray;}")
        self.label8.setStyleSheet("QLabel {background-color: gray;}")
        self.pushButtonR.setEnabled(False)
    
    def regresar(self):
        global validacion_de_juego

        player.mover_disco(ultima_seleccion2, ultima_seleccion1)
        player.getJugadas().pop()
        player.getJugadas().pop()
        disco_temp = ultima_seleccion1.getDiscos()[-1]
        tamanio_temp = disco_temp.getTamanio()
        posicion_temp = ultima_seleccion1.getDiscos().index(disco_temp)
        if ultima_seleccion1 == p1:
            X = 0
        elif ultima_seleccion1 == p2:
            X = 325
        else:
            X = 650
        
        Y = Y_posicion[posicion_temp]

        if tamanio_temp == 1:
            self.label1.move(155 + X, Y)
        elif tamanio_temp == 2:
            self.label2.move(140 + X, Y)
        elif tamanio_temp == 3:
            self.label3.move(125 + X, Y)
        elif tamanio_temp == 4:
            self.label4.move(110 + X, Y)
        elif tamanio_temp == 5:
            self.label5.move(95 + X, Y)
        elif tamanio_temp == 6:
            self.label6.move(80 + X, Y)
        elif tamanio_temp == 7:
            self.label7.move(65 + X, Y)
        else:
            self.label8.move(50 + X, Y)

        validacion_de_juego = 0
        self.reiniciar_seleccion()
        self.pushButtonR.setEnabled(False)

        jugadas_realizadas = len(player.getJugadas())
        self.NoJugadas.setText("Jugadas realizadas: {}".format(jugadas_realizadas))

    def tiempo(self, t):
        loop = QtCore.QEventLoop()
        QtCore.QTimer.singleShot(t, loop.quit)
        loop.exec_()

    def automata(self, poste1, poste2):
        self.funcion_juego(poste1)
        self.tiempo(400)#900
        self.funcion_juego(poste2)
        self.tiempo(325)#800

    def tobar(self, postei):
        self.pushButton.setEnabled(False)
        self.pushButton1.setEnabled(False)
        self.pushButton2.setEnabled(False)
        self.pushButton3.setEnabled(False)
        self.pushButtonR.setEnabled(False)
        self.pushButtonM.setEnabled(False)
        global M
        M = False

        jugadas =\
        (12, 13, 23, 12, 31, 32, 12, 13, 23, 21, 31, 23, 12, 13, 23, 12,\
         31, 32, 12, 31, 23, 21, 31, 32, 12, 13, 23, 12, 31, 32, 12, 13,\
         23, 21, 31, 23, 12, 13, 23, 21, 31, 32, 12, 31, 23, 21, 31, 23,\
         12, 13, 23, 12, 31, 32, 12, 13, 23, 21, 31, 23, 12, 13, 23, 12,\
         31, 32, 12, 31, 23, 21, 31, 32, 12, 13, 23, 12, 31, 32, 12, 31,\
         23, 21, 31, 23, 12, 13, 23, 21, 31, 32, 12, 31, 23, 21, 31, 32,\
         12, 13, 23, 12, 31, 32, 12, 13, 23, 21, 31, 23, 12, 13, 23, 12,\
         31, 32, 12, 31, 23, 21, 31, 32, 12, 13, 23, 12, 31, 32, 12, 13,\
         23, 21, 31, 23, 12, 13, 23, 21, 31, 32, 12, 31, 23, 21, 31, 23,\
         12, 13, 23, 12, 31, 32, 12, 13, 23, 21, 31, 23, 12, 13, 23, 21,\
         31, 32, 12, 31, 23, 21, 31, 32, 12, 13, 23, 12, 31, 32, 12, 31,\
         23, 21, 31, 23, 12, 13, 23, 21, 31, 32, 12, 31, 23, 21, 31, 23,\
         12, 13, 23, 12, 31, 32, 12, 13, 23, 21, 31, 23, 12, 13, 23, 12,\
         31, 32, 12, 31, 23, 21, 31, 32, 12, 13, 23, 12, 31, 32, 12, 13,\
         23, 21, 31, 23, 12, 13, 23, 21, 31, 32, 12, 31, 23, 21, 31, 23,\
         12, 13, 23, 12, 31, 32, 12, 13, 23, 21, 31, 23, 12, 13, 23)

        for j in jugadas:
            js = str(j)
            j1 = int(js[0])
            j2 = int(js[1])
            if j1 == 1:
                j1 = p1
            elif j1 == 2:
                j1 = p2
            else:
                j1 = p3

            if j2 == 1:
                j2 = p1
            elif j2 == 2:
                j2 = p2
            else:
                j2 = p3

            self.automata(j1, j2)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Torres de Hanói"))
        self.NoJugadas.setText(_translate("MainWindow", "Jugadas realizadas: 0"))
        self.pushButton.setText(_translate("MainWindow", "Cambiar selección"))
        self.pushButtonR.setText(_translate("MainWindow", "Regresar un paso"))
        self.pushButton1.setText(_translate("MainWindow","Poste 1"))
        self.pushButton2.setText(_translate("MainWindow","Poste 2"))
        self.pushButton3.setText(_translate("MainWindow","Poste 3"))
        self.mensaje_error.setText(_translate("MainWindow"," "))
        self.menuTorres.setTitle(_translate("MainWindow", "Torres"))