from functools import partial

from PySide6.QtCore import (
    QUrl, Qt
    )
from PySide6.QtWidgets import (
    QHBoxLayout, QMainWindow,
    QVBoxLayout, QWidget
    )

from .components.chan_list import ChannelList as SideBar
from .components.top_bar import TopBar
from .components.engine import Engine  
from .components.add_channel import AddBtn   


class Content(QWidget):
    """It's the content's container, that will show the SideBar and the Engine.
    > layout: `HBox`
    params: 
    - parent: QWidget
    - channels: dict

    > ``channels`` must to be returned by the Model.get_channel()
    """

    def __init__(self, parent:QWidget, mainWin, channels:dict, path) -> None:
        super().__init__(parent)

        self.channels = channels
        self.mainWin = mainWin
        self.path = path
        self.eng = Engine(self, self.mainWin, QUrl.fromLocalFile(self.path+"/data/index.html"))
        
        AddBtn(self, mainWin)

        self.layout = QHBoxLayout()

        self.__config_widget()
        self.__config_layout()
        self.__add_widgets()

        self.setLayout(self.layout)

    def __config_widget(self):
        self.setAutoFillBackground(True)
        self.setWhatsThis("Hello")

    def __config_layout(self):
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addStretch(1)

    def __add_widgets(self):
        self.layout.addWidget(SideBar(self, self.channels), 0)
        self.layout.addWidget((self.eng), 1)

    def open_url(self, url):
        print(f'handling url: {url}')
        self.eng.stop()
        self.eng.load(QUrl(url))


class Container(QWidget):
    """It's the main container, that will show the TopBar and Content.
    > layout: `VBox`
    params: 
    - parent: QMainWindow
    - channels: dict

    > ``channels`` must to be returned by the Model.get_channel()
    """

    def __init__(self, parent: QMainWindow, channels: dict, path) -> None:
        super().__init__(parent)
        # Channel param
        self.channels = channels
        self.mainWin = parent
        self.path = path

        # Init layout
        self.layout = QVBoxLayout(self)

        # Configuring
        self.__config_layout()
        self.__add_widgets()

    def __config_layout(self):
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addStretch(1)

    def __add_widgets(self):
        # Adding content
        self.layout.addWidget(TopBar(self, self.mainWin), Qt.AlignTop)
        self.layout.addWidget(Content(self, self.mainWin, self.channels, self.path), Qt.AlignTop)
    



