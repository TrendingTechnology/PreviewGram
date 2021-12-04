import sys, os

from PySide6.QtCore import Qt, QPoint, QCoreApplication, QFileInfo
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QMessageBox
    )
from PySide6.QtGui import QCursor

from qt_material import apply_stylesheet

from .model.db import Model
from .model.page import Page
from .ui import channel
from .ui.ui import *
from .ui.channel import ChannelDialog, Update
from .ui.components.chan_list import ChannelList as SideBar

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.pressing = False
        self.start = QPoint(0, 0)
        self.channels = {}
        self.path = str(os.path.dirname(os.path.realpath(__file__)))

        self.get_channels()

        self.__config_win()
        self.__add_container()

    def __config_win(self):
        self.setWindowTitle("Private Previewgram")
        self.setFixedWidth(830)
        self.setMinimumHeight(600)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setCursor(QCursor(Qt.OpenHandCursor))
        
    def __add_container(self):
        container = Container(self, self.channels, self.path)
        self.setCentralWidget(container)

    #-- Database
    def channelDialog(self):
        dial = ChannelDialog(self)
        dial.destroyed.connect(self.restart)
        dial.exec()

    def get_channels(self):
        self.channels = Model.get_channels()

    def add_chan(self, chan, url):
        Model.add_channel(chan, url)
        self.added_channel()

    def delete_chan(self, chan):
        Model.del_channel(chan)
        self.get_channels()

    #-- Database :: checking
    def check(self, chan, url):
        
        if (
            url.startswith("@")
            or url.startswith("https://t.me/")
            or url.startswith("https://telegram.me/")
            ):
            result = True 
            print(result)
            self.add_chan(chan, url)
        else:
            result = False
            print(result)
            self.wrong_url()

    def wrong_url(self):
        m = QMessageBox.critical(
            self,
            "Use a valid channel url",
            "Examples are:\nhttps://t.me/channel, https://telegram.me/channel, @channel, https://t.me/s/channel",
            buttons=QMessageBox.Close,
            defaultButton=QMessageBox.Close)

    def added_channel(self):
        m = QMessageBox.critical(
            self,
            "Info!",
            "Channel added to database",
            buttons=QMessageBox.Close,
            defaultButton=QMessageBox.Close)


    #-- Updating Window status
    def closeWindow(self):
        self.close()

    def minWindow(self):
        self.showMinimized()

    #-- Moving Window
    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.position())
        self.pressing = True
        

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.setCursor(QCursor(Qt.ClosedHandCursor))
            self.end = self.mapToGlobal(event.position())
            self.movement = self.end-self.start
            self.setGeometry(
                self.mapToGlobal(self.movement).x(),
                self.mapToGlobal(self.movement).y(),
                self.width(), self.height())
            self.start = self.end
        else:
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False
        self.setCursor(QCursor(Qt.OpenHandCursor))

    #-- Restart
    def restart (self):     
        print("closed!")
        open_win()
        self.destroy()
           
def open_win():
    window = Window()
    window.show()  

def start_app():

    app = QApplication(sys.argv)        
    apply_stylesheet(app, theme='dark_blue.xml')
    open_win()           
    app.exec()            


if __name__ == '__main__':
    
    start_app()