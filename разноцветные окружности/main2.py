import sys
import random
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QGraphicsScene, QGraphicsView,
                             QGraphicsEllipseItem, QMainWindow)
from PyQt5.QtGui import QColor
from ui import UI

class CircleGenerator(QWidget, UI):
    def __init__(self):
        super(CircleGenerator, self).__init__()
        self.setupUi(self)

    def generate_circle(self):
        diameter = random.randint(10, 100)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        circle = QGraphicsEllipseItem(0, 0, diameter, diameter)
        circle.setPos(random.randint(0, 400 - diameter), random.randint(0, 400 - diameter))
        circle.setBrush(color)

        self.scene.addItem(circle)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CircleGenerator()
    w.show()
    sys.exit(app.exec_())