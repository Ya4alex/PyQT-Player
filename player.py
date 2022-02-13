# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 470)
        MainWindow.setMinimumSize(QtCore.QSize(558, 469))
        MainWindow.setMaximumSize(QtCore.QSize(560, 470))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 561, 471))
        self.label.setMinimumSize(QtCore.QSize(561, 471))
        self.label.setMaximumSize(QtCore.QSize(561, 471))
        self.label.setStyleSheet("background-color: rgb(183, 206, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.add_track = QtWidgets.QPushButton(self.centralwidget)
        self.add_track.setGeometry(QtCore.QRect(380, 400, 81, 23))
        self.add_track.setStyleSheet("background-color: rgb(255, 255, 198);\n"
"font: 10pt \"MV Boli\";")
        self.add_track.setObjectName("add_track")
        self.paus = QtWidgets.QPushButton(self.centralwidget)
        self.paus.setGeometry(QtCore.QRect(80, 400, 51, 31))
        self.paus.setStyleSheet("font: 16pt \"MV Boli\";\n"
"background-color: rgb(252, 165, 255);")
        self.paus.setObjectName("paus")
        self.befour = QtWidgets.QPushButton(self.centralwidget)
        self.befour.setGeometry(QtCore.QRect(10, 400, 61, 31))
        self.befour.setStyleSheet("font: 16pt \"MV Boli\";\n"
"background-color: rgb(252, 165, 255);")
        self.befour.setObjectName("befour")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(140, 400, 61, 31))
        self.next.setStyleSheet("font: 16pt \"MV Boli\";\n"
"background-color: rgb(252, 165, 255);")
        self.next.setObjectName("next")
        self.volume = QtWidgets.QDial(self.centralwidget)
        self.volume.setGeometry(QtCore.QRect(210, 380, 71, 71))
        self.volume.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.volume.setStyleSheet("background-color: rgb(155, 170, 255);")
        self.volume.setObjectName("volume")
        self.timeline = QtWidgets.QSlider(self.centralwidget)
        self.timeline.setGeometry(QtCore.QRect(10, 440, 131, 22))
        self.timeline.setStyleSheet("")
        self.timeline.setOrientation(QtCore.Qt.Horizontal)
        self.timeline.setObjectName("timeline")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label_3.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.new_playlist = QtWidgets.QPushButton(self.centralwidget)
        self.new_playlist.setGeometry(QtCore.QRect(10, 370, 91, 23))
        self.new_playlist.setStyleSheet("background-color: rgb(255, 255, 198);\n"
"font: 10pt \"MV Boli\";")
        self.new_playlist.setObjectName("new_playlist")
        self.wichlist = QtWidgets.QLabel(self.centralwidget)
        self.wichlist.setGeometry(QtCore.QRect(290, 0, 221, 31))
        self.wichlist.setStyleSheet("font: 12pt \"MV Boli\";")
        self.wichlist.setObjectName("wichlist")
        self.playlists = QtWidgets.QListWidget(self.centralwidget)
        self.playlists.setGeometry(QtCore.QRect(10, 30, 271, 331))
        self.playlists.setStyleSheet("background-color: rgb(222, 255, 243);\n"
"font: 10pt \"MV Boli\";")
        self.playlists.setObjectName("playlists")
        self.tracks = QtWidgets.QListWidget(self.centralwidget)
        self.tracks.setGeometry(QtCore.QRect(290, 30, 261, 361))
        self.tracks.setStyleSheet("background-color: rgb(222, 255, 243);\n"
"font: 10pt \"MV Boli\";")
        self.tracks.setObjectName("tracks")
        self.question = QtWidgets.QPushButton(self.centralwidget)
        self.question.setGeometry(QtCore.QRect(520, 0, 31, 23))
        self.question.setStyleSheet("background-color: rgba(255, 0, 0, 0);\n"
"font: 14pt \"MV Boli\";")
        self.question.setObjectName("question")
        self.volume_label = QtWidgets.QLabel(self.centralwidget)
        self.volume_label.setGeometry(QtCore.QRect(250, 440, 31, 31))
        self.volume_label.setStyleSheet("font: 9pt \"MV Boli\";")
        self.volume_label.setObjectName("volume_label")
        self.timeline_label = QtWidgets.QLabel(self.centralwidget)
        self.timeline_label.setGeometry(QtCore.QRect(140, 440, 81, 21))
        self.timeline_label.setStyleSheet("font: 12pt \"MV Boli\";")
        self.timeline_label.setObjectName("timeline_label")
        self.Track_name = QtWidgets.QLabel(self.centralwidget)
        self.Track_name.setGeometry(QtCore.QRect(290, 430, 261, 31))
        self.Track_name.setStyleSheet("font: 12pt \"MV Boli\";\n"
"background-color: rgb(255, 215, 249);")
        self.Track_name.setText("")
        self.Track_name.setObjectName("Track_name")
        self.label_q = QtWidgets.QLabel(self.centralwidget)
        self.label_q.setEnabled(True)
        self.label_q.setGeometry(QtCore.QRect(20, 40, 521, 311))
        self.label_q.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.label_q.setMouseTracking(True)
        self.label_q.setStyleSheet("font: 12pt \"MV Boli\";\n"
"background-color: rgb(255, 215, 249);")
        self.label_q.setScaledContents(False)
        self.label_q.setWordWrap(False)
        self.label_q.setObjectName("label_q")
        self.delete_track = QtWidgets.QPushButton(self.centralwidget)
        self.delete_track.setGeometry(QtCore.QRect(470, 400, 81, 23))
        self.delete_track.setStyleSheet("background-color: rgb(255, 183, 183);\n"
"font: 10pt \"MV Boli\";")
        self.delete_track.setObjectName("delete_track")
        self.delete_playlist = QtWidgets.QPushButton(self.centralwidget)
        self.delete_playlist.setGeometry(QtCore.QRect(110, 370, 91, 23))
        self.delete_playlist.setStyleSheet("background-color: rgb(255, 183, 183);\n"
"font: 10pt \"MV Boli\";")
        self.delete_playlist.setObjectName("delete_playlist")
        self.save_changes = QtWidgets.QPushButton(self.centralwidget)
        self.save_changes.setGeometry(QtCore.QRect(290, 400, 81, 23))
        self.save_changes.setStyleSheet("font: 10pt \"MV Boli\";\n"
"background-color: rgb(188, 255, 180);")
        self.save_changes.setObjectName("save_changes")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 365, 71, 21))
        self.label_4.setStyleSheet("font: 10pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_track.setText(_translate("MainWindow", "add track"))
        self.paus.setText(_translate("MainWindow", "||"))
        self.befour.setText(_translate("MainWindow", "<<"))
        self.next.setText(_translate("MainWindow", ">>"))
        self.label_3.setText(_translate("MainWindow", "Playlists:"))
        self.new_playlist.setText(_translate("MainWindow", "new playlist"))
        self.wichlist.setText(_translate("MainWindow", "Tracks:"))
        self.question.setText(_translate("MainWindow", "?"))
        self.volume_label.setText(_translate("MainWindow", "100"))
        self.timeline_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">00:00:00</p></body></html>"))
        self.label_q.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MV Boli\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Hi, there will be a little instruction here:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  1. the player does not save tracks, if you delete a track on your computer,</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  it will be deleted on the player too</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  2. to add a track to the playlist, select it in the dialog box in mp3 format</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  3. With a double click you can open a playlist or turn on a track</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  4. To delete a track or playlist, select it with a mouse click and press</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  Backspase</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  5. to switch between tracks you can use buttons or spacebar and arrows</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  6. &lt;there will probably be something else&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"><br /> P.S. to close the hint click on &quot;?&quot; again</span></p></body></html>"))
        self.delete_track.setText(_translate("MainWindow", "delete"))
        self.delete_playlist.setText(_translate("MainWindow", "delete list"))
        self.save_changes.setText(_translate("MainWindow", "save"))
        self.label_4.setText(_translate("MainWindow", "Volume:"))
