#-- Importing basic QT modules
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QUrl, Qt

#-- Importing Web QT modules
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings


#-- Widget
class Engine(QWebEngineView):
    """Widget that will render the html file
    params:
    - parent: QWidget
    - url: QUrl 
    """

    #-- Init
    def __init__(self, parent:QWidget, mainWin, url: QUrl):
        super().__init__(parent)

        # Setting parameters
        self.mainWin = mainWin
        self.page()
        self.init_url = url
        self._url = (self.url()).toString() 

        # Configuring Widget
        self.__privacy_config()
        self.__config_widget()

        # Loading start page
        self.load(url)

        # Loading functions
        self.page().loadStarted.connect(self.loading)
        self.page().loadFinished.connect(self.loaded)
        self.page().linkHovered.connect(self.link_hover)
        self.page().urlChanged.connect(self.url_changed)



    #-- Configuring
    def __privacy_config(self):

        self.page().settings().setAttribute(QWebEngineSettings.JavascriptEnabled, False)
        self.page().profile().setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36")

    def __config_widget(self):
        self.setMinimumWidth(600)   



    #-- functions
    def update(self):
        self.reload()


    def loading(self):
        self.mainWin.setCursor(QCursor(Qt.BusyCursor))


    def loaded(self):
        self.mainWin.setCursor(QCursor(Qt.OpenHandCursor))


    def link_hover(self):
        self.setToolTip("[Right Mouse Button] > Copy Link Address")


    def url_changed(self):
        url = self._url
        print("old:",url)

        if url.startswith("https://t.me/"):

            if url.startswith("https://t.me/s/"):
                pass
            else:
                self.stop()
                print("stopped")
                print("new:",    "https://t.me/s/" + "/".join(url.split("/")[3:])  )
                self.load(QUrl(  "https://t.me/s/" + "/".join(url.split("/")[3:])  ))
                
        elif url == "https://www.whatismybrowser.com/":
            pass
        elif url == "about:blank":
            pass
        elif url == "":
            pass
        elif url == self.init_url:
            pass

        else:
            self.stop()
            print("stopped")
            self.load(QUrl("https://t.me/s/previewgram"))
            
