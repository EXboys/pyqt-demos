# -*- coding: utf-8 -*-
import sys
from PyQt4.Qt import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
# from browser import Ui_HttpWidget
try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Browser(QWidget):

    def __init__(self, parent = None):
        super(Browser, self).__init__(parent)
        #self.url = 'http://yii.kuaxiango.com/backend/web/'
        self.url = 'http://www.hao123.com'
        self.createLayout()
        self.createConnection()
        self.webSettings = self.webView.settings()
        self.webSettings.setAttribute(QWebSettings.PluginsEnabled, True)
        self.webView.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)
        self.webView.page().linkClicked.connect(self.linkClicked)
        self.show()

    def linkClicked(self, url):
        self.addressBar.setText(str(url)[20:-2])
        self.webView.load(url)

    def search(self):
        address = str(self.addressBar.text())
        if address:
            if address.find('://') == -1:
                address = 'http://' + address
            url = QUrl(address)
            self.webView.load(url)

    def back(self):
        self.addressBar.setText(str(self.webView.history().backItem().url())[20:-2])
        self.webView.back()

    def forward(self):
        self.addressBar.setText(str(self.webView.history().forwardItem().url())[20:-2])
        self.webView.forward()

    def createLayout(self):
        self.setWindowTitle("Kuaxian browser")
        icon = QIcon()
        icon.addPixmap(QPixmap(_fromUtf8("icon.jpg")), QIcon.Normal,
                       QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowOpacity(0.95)
        self.addressBar = QLineEdit(self.url)
        self.goButton = QPushButton(u"&进入")
        self.forButton = QPushButton(u"&前进")
        self.backButton = QPushButton(u"&后退")
        bl = QHBoxLayout()
        bl.addWidget(self.goButton);bl.addWidget(self.addressBar)
        bl.addWidget(self.forButton);bl.addWidget(self.backButton)
        self.webView = QWebView()
        layout = QVBoxLayout();layout.addLayout(bl);layout.addWidget(self.webView)
        self.setLayout(layout)
        self.webView.load(QUrl(self.url))


    def createConnection(self):
        self.connect(self.addressBar, SIGNAL('returnPressed()'), self.search)
        self.connect(self.addressBar, SIGNAL('returnPressed()'), self.addressBar, SLOT('selectAll()'))
        self.connect(self.goButton, SIGNAL('clicked()'), self.search)
        self.connect(self.goButton, SIGNAL('clicked()'), self.addressBar, SLOT('selectAll()'))
        self.connect(self.forButton, SIGNAL('clicked()'), self.forward)
        self.connect(self.forButton, SIGNAL('clicked()'), self.addressBar, SLOT('selectAll()'))
        self.connect(self.backButton, SIGNAL('clicked()'), self.back)
        self.connect(self.backButton, SIGNAL('clicked()'), self.addressBar, SLOT('selectAll()'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    browsers = Browser()
    browsers.show()
    sys.exit(app.exec_())