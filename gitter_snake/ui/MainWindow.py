import sys
from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QApplication, QMainWindow, qApp, QListView, QAction)
from PyQt5.QtGui import QIcon
import images_rc

icon_info = ":/images/information.png"
icon_exit = ":/images/door_out.png"


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(400, 600)
        self.statusBar().showMessage("Ready")
        self.setWindowIcon(QIcon(icon_info))

        self.init_menu()

        self.list_view = QListView()

        self.h_box = QHBoxLayout()
        self.h_box.addWidget(self.list_view)

        self.v_box = QVBoxLayout()
        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)
        self.show()

    def init_menu(self):
        exitAction = QAction(QIcon(icon_exit), "&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit Application")
        exitAction.triggered.connect(qApp.quit)

        fileMenu = self.menuBar().addMenu("&File")
        fileMenu.addAction(exitAction)

    def run(self):
        app = QApplication(sys.argv)
        sys.exit(app.exec_())
