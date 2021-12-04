from PySide6.QtGui import QIcon, QCursor
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt

class AddBtn(QPushButton):

    def __init__(self, parent, mainWin):
        # parent = Container(QWidget)
        super().__init__(parent)

        self.mainWin = mainWin
        self.__config()
        self.__action()

    def __config(self):
        self.setText("+")
        self.setGeometry(740, 450, 50, 50)
        self.setStyleSheet(
            """
            color: #fff; background-color: #448aff;
            """)
        self.setCursor(QCursor(Qt.PointingHandCursor))


    def __action(self):
        self.clicked.connect(self.mainWin.channelDialog)
