import sys
import random
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QGraphicsScene, QGraphicsView,
                             QGraphicsEllipseItem)
from PyQt5.QtGui import QColor
from PyQt5 import uic

class CircleGenerator(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        Form, Base = uic.loadUiType('Ui.ui')
        self.ui = Form()
        self.ui.setupUi(self)

        self.ui.button.clicked.connect(self.generate_circle)

        self.scene = QGraphicsScene(self)
        self.ui.view.setScene(self.scene)

    def generate_circle(self):
        diameter = random.randint(10, 100)
        color = QColor(225, 225, 0)

        circle = QGraphicsEllipseItem(0, 0, diameter, diameter)
        circle.setPos(random.randint(0, 400 - diameter), random.randint(0, 400 - diameter))
        circle.setBrush(color)


        self.scene.addItem(circle)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleGenerator()
    window.show()
    sys.exit(app.exec_())