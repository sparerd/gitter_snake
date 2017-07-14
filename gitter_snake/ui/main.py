import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, qApp, QAction)
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):

    def __init__(self, icons):
        self.icons = icons
        self.app = QApplication(sys.argv)
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(400, 600)
        self.statusBar().showMessage("Ready")
        self.setWindowIcon(QIcon(self.icons["info"]))

        self.init_menu()
        self.show()

    def init_menu(self):
        exitAction = QAction(QIcon(self.icons["exit"]), "&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit Application")
        exitAction.triggered.connect(qApp.quit)

        fileMenu = self.menuBar().addMenu("&File")
        fileMenu.addAction(exitAction)

    def run(self):
        sys.exit(self.app.exec_())
