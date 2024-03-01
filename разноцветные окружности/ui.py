from PyQt5 import QtCore, QtGui, QtWidgets

class UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle('Разноцветные окружности')
        MainWindow.resize(400, 400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.resize(400, 400)

        self.button = QtWidgets.QPushButton(self.centralwidget)

        self.scene = QtWidgets.QGraphicsScene(self.centralwidget)
        self.view = QtWidgets.QGraphicsView(self.scene)

        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.view)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Разноцветные окружности"))
        self.button.setText(_translate("MainWindow", "Создать круг"))
        self.button.clicked.connect(self.generate_circle)