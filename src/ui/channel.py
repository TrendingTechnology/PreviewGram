from os import terminal_size
from typing import Text, Tuple
from PySide6.QtWidgets import (
    QComboBox, QFormLayout, QLabel, QScrollArea, QStackedLayout, QVBoxLayout, QWidget, QHBoxLayout, QPushButton,
    QDialog, QGroupBox, QLineEdit, QMessageBox
)
from PySide6.QtCore import QRegularExpression, Qt 
from PySide6.QtGui import QCursor, QRegularExpressionValidator

from functools import partial


class Update(QWidget):

    def __init__(self, parent, mainWin):
        super().__init__(parent)
        self.mainWin = mainWin
        self.chan = QLineEdit()
        self.url = QLineEdit()
        self.submitBtn = QPushButton("Submit")

        self.layout = QFormLayout(self)
        self.__input_config()
        self.__layout()

        self.__action()
        

    def __input_config(self):
        self.chan.setMaxLength(20)
        self.url.setMaxLength(256)
       

    def __layout(self):
        self.layout.addRow("Channel:", self.chan)
        self.layout.addRow("Url:", self.url)
        self.layout.addRow(self.submitBtn)
        self.layout.addRow(QLabel("Close this window to update!"))

    def __action(self):
        self.submitBtn.clicked.connect(
            lambda: self.mainWin.check(self.chan.text(), self.url.text())
            )





class Remove(QWidget):

    def __init__(self, parent, mainWin):
        super().__init__(parent)
        self.mainWin = mainWin
        self.mainWin.get_channels()
        self.channels = self.mainWin.channels

        self.layout = QVBoxLayout(self)
        self.wid = QWidget()
        self.wid_layout = QVBoxLayout()
        self.scroll = QScrollArea()

        self.__gen_layout()
        self.wid.setLayout(self.wid_layout)

        self.__config_scroll()
        self.__config_layout()
        self.layout.addWidget(self.scroll)

    def __config_scroll(self):
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.wid)

    def __config_layout(self):
        self.wid_layout.addStretch()

    def __gen_layout(self):

        for chan in self.channels:

            btn = QPushButton("Delete "+chan, self)
            btn.setMaximumHeight(300)
            btn.setMinimumHeight(50)
            btn.setCursor(QCursor(Qt.PointingHandCursor))
            btn.clicked.connect(partial(self.mainWin.delete_chan, chan))
            btn.clicked.connect(partial(self.destroy_self, btn))
            self.wid_layout.addWidget(btn, Qt.AlignBottom)

    def destroy_self(self, btn):
        btn.setEnabled(False)
            
        




class ChannelDialog(QDialog):

    def __init__(self, parent):
        super().__init__(parent)
        self.mainWin = parent

        self.setAttribute(Qt.WA_DeleteOnClose, True)

        self.layout = QVBoxLayout(self)
        self.pageCombo = QComboBox()
        self.stackedLayout = QStackedLayout()

        self.ui()
    

    def ui(self):

        self.setWindowTitle("Channels")
        self.setSizeGripEnabled(True) 
        self.__combo_page()
        self.__stacked_layout()
        self.layout.addWidget(self.pageCombo)
        self.layout.addLayout(self.stackedLayout)

    def __combo_page(self):
        
        self.pageCombo.addItems(["Add", "Delete"])
        self.pageCombo.activated.connect(self.switch_page)

    def __stacked_layout(self):
        
        self.stackedLayout.addWidget(Update(self, self.mainWin))
        self.stackedLayout.addWidget(Remove(self, self.mainWin))
        

    def switch_page(self):
        self.stackedLayout.setCurrentIndex(self.pageCombo.currentIndex())


