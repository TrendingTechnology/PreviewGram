from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QScrollArea)
from PySide6.QtGui import QColor, QCursor
from PySide6.QtCore import QPoint, QUrl, Qt
from functools import partial


class ChannelList(QWidget):

    def __init__(self, parent, channels:dict) -> None:
        super().__init__(parent)

        self.channels = channels
        self.parent = parent

        self.layout = QVBoxLayout(self)
        self.wid = QWidget()
        self.wid_layout = QVBoxLayout()
        self.scroll = QScrollArea()

        self.__gen_buttons()
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

    def __gen_fixed_buttons(self):

        btn_test = QPushButton("Test privacy!", self)
        btn_test.setMaximumHeight(300)
        btn_test.setMinimumHeight(50)
        btn_test.setStyleSheet("background-color: #448aff; color: #fff")
        btn_test.setCursor(QCursor(Qt.PointingHandCursor))
        btn_test.clicked.connect(partial(self.parent.open_url, "https://www.whatismybrowser.com/"))

        official_channel = QPushButton("Official Channel", self)
        official_channel.setMaximumHeight(300)
        official_channel.setMinimumHeight(50)
        official_channel.setStyleSheet("background-color: #448aff; color: #fff")
        official_channel.setCursor(QCursor(Qt.PointingHandCursor))
        official_channel.clicked.connect(partial(self.parent.open_url, "https://t.me/s/previewgram"))

        self.wid_layout.addWidget(btn_test, Qt.AlignBottom)
        self.wid_layout.addWidget(official_channel, Qt.AlignBottom)

    def __gen_buttons(self):

        self.__gen_fixed_buttons()        

        for chan in self.channels:

            btn = QPushButton(chan, self)
            btn.setMaximumHeight(300)
            btn.setMinimumHeight(50)
            btn.setCursor(QCursor(Qt.PointingHandCursor))
            btn.clicked.connect(partial(self.parent.open_url, self.channels[chan]))
            self.wid_layout.addWidget(btn, Qt.AlignBottom)