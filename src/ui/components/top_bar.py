from PySide6.QtWidgets import (
    QLabel, QWidget, QHBoxLayout, QPushButton
)
from PySide6.QtCore import Qt 
from PySide6.QtGui import QCursor
import os, sys

class Title(QLabel):

    def __init__(self, mainWin) -> None:
        super().__init__()
        self.mainWin = mainWin
        self.size = 35
        self.setText("Private Previewgram")
        self.__config()

    def __config(self):
        self.setFixedHeight(35)
        self.setAlignment(Qt.AlignCenter)

class Github(QPushButton):

    def __init__(self, mainWin) -> None:
        super().__init__()
        self.mainWin = mainWin
        self.size = 35

        self.__config()
        self.__action()
    
    def __config(self):
        self.setText('Visit Us on Github!')
        self.setStyleSheet(
            "border: none;"+
            "background-color: #448aff; color: #fff;"+
            "padding: 0; margin: 0 36px 0 0;"
            )
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def __action(self):
        self.clicked.connect(self.openGithub)

    def openGithub(self):
        repo_link = "https://github.com/RickBarretto/PreviewGram"
        command = "explorer "+repo_link
        if sys.platform == "MacOSX":
            command = "open "+repo_link
        os.system(command)

class CloseBtn(QPushButton):

    def __init__(self, mainWin) -> None:
        super().__init__()
        self.mainWin = mainWin
        self.size = 35

        self.__config()
        self.__action()
    
    def __config(self):
        self.setText('X')
        self.setFixedSize(self.size, self.size)
        self.setStyleSheet(
            "background-color: red;"+
            "border: none;"+
            "color: white;"+
            "padding: 0;"+
            "margin: 0")
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def __action(self):
        self.clicked.connect(self.mainWin.closeWindow)

class MinBtn(QPushButton):

    def __init__(self, mainWin) -> None:
        super().__init__()
        self.mainWin = mainWin
        self.size = 35

        self.__config()
        self.__action()
    
    def __config(self):
        self.setText('_')
        self.setFixedSize(self.size, self.size)
        self.setStyleSheet(
            "border: none;"+
            "background-color: #448aff; color: #fff;"+
            "padding: 0;"+
            "margin: 0")
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def __action(self):
        self.clicked.connect(self.mainWin.minWindow())


class TopBar(QWidget):
    """It will change the default Windows's title bar
    param:
    - parent: QWidget 
    """

    def __init__(self, parent:QWidget, mainWin) -> None:
        super().__init__(parent)

        self.layout = QHBoxLayout(self)
        self.mainWin = mainWin

        self.__config_widget()
        self.__add_widgets()
        self.__config_layout()

    def __config_widget(self):
        self.setFixedHeight(35)
        self.setWhatsThis("Hello")
        self.setStyleSheet("padding: 0 15px 0 0; margin: 0;")
        self.setContentsMargins(13, 0, 13, 0)

    def __config_layout(self):
        self.layout.setContentsMargins(0, 0, 0, 10)

    def __add_widgets(self):
        self.layout.addWidget(Github(self))
        self.layout.addWidget(Title(self.mainWin))
        self.layout.addWidget(MinBtn(self.mainWin))
        self.layout.addWidget(CloseBtn(self.mainWin))
            