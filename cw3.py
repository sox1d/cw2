import sys
from random import choice
import io

import PyQt6
from PyQt6 import uic
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from Ui import Ui_MainWindow


class Draw(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drow_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def drow_circle(self, qp):
        qp.setBrush(QColor(choice(range(0, 255)), choice(range(0, 255)), choice(range(0, 255))))
        r = choice(range(10, 100))
        qp.drawEllipse(QPointF(300, 300), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Draw()
    ex.show()
    sys.exit(app.exec())
