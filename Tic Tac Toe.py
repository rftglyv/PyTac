from PySide6.QtWidgets import *
from PySide6 import QtGui
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys, os

basedir = os.path.dirname(__file__)

try:
    from ctypes import windll
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass



class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		
		self.setWindowTitle("Tic Tac Toe")
		self.setGeometry(100, 100, 300, 400)
		self.gameWindow()
		self.show()


	def gameWindow(self):

		self.turn = 0
		self.times = 0
		self.btnList = []

		for p in range(3):
			temp = []
			for p in range(3):
				temp.append((QPushButton(self)))
			self.btnList.append(temp)

		x = 90
		y = 90

		for i in range(3):
			for j in range(3):

				self.btnList[i][j].setGeometry(x*i + 20,y*j + 20, 80, 80)
				self.btnList[i][j].setFont(QFont(QFont('Times', 20, weight=QtGui.QFont.Bold)))
				self.btnList[i][j].clicked.connect(self.btnClicked)

		self.label = QLabel(self)
		self.label.setGeometry(20, 280, 260, 60)
		self.label.setAlignment(Qt.AlignCenter)
		self.label.setFont(QFont(QFont('Quicksand', 10)))
		self.resetBtn = QPushButton('Yenidən başla',self)
		self.resetBtn.setFont(QFont(QFont('Quicksand', 13, weight=QtGui.QFont.Bold)))
		self.resetBtn.setGeometry(75, 335, 150, 40)
		self.resetBtn.clicked.connect(self.reset)
		self.resetBtn.setEnabled(False)


	def reset(self):
	
		self.turn = 0
		self.times = 0
		self.label.setText("")
		self.resetBtn.setEnabled(False)
		
		for buttons in self.btnList:
			for button in buttons:
				button.setEnabled(True)
				button.setText("")


	def btnClicked(self):

		self.times += 1
		button = self.sender()
		button.setEnabled(False)

		if self.turn == 0:
			button.setText("X")
			self.turn = 1
		else:
			button.setText("O")
			self.turn = 0

		win = self.mainEngine()

		text = ""

		if win == True:
			if self.turn == 0:
				text = "O Qazandı"
				
			else:
				text = "X Qazandı"

			for buttons in self.btnList:
				for push in buttons:
					push.setEnabled(False)
			self.resetBtn.setEnabled(True)		

		elif self.times == 9:
			text = "Heç - heçə"
			self.resetBtn.setEnabled(True)
		self.label.setText(text)
			

	def mainEngine(self):


		for i in range(3):
			if self.btnList[0][i].text() == self.btnList[1][i].text() and self.btnList[0][i].text() == self.btnList[2][i].text() and self.btnList[0][i].text() != "":
				return True

		for i in range(3):
			if self.btnList[i][0].text() == self.btnList[i][1].text() and self.btnList[i][0].text() == self.btnList[i][2].text() and self.btnList[i][0].text() != "":
				return True

		if self.btnList[0][0].text() == self.btnList[1][1].text() and self.btnList[0][0].text() == self.btnList[2][2].text() and self.btnList[0][0].text() != "":
			return True

		if self.btnList[0][2].text() == self.btnList[1][1].text() and self.btnList[1][1].text() == self.btnList[2][0].text() and self.btnList[0][2].text() != "":
			return True

		return False


if __name__ == '__main__':
	App = QApplication(sys.argv)
	App.setWindowIcon(QtGui.QIcon(os.path.join(basedir, 'icon.ico')))
	window = Window()
	sys.exit(App.exec())
