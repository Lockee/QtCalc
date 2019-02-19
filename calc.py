import sys
import PyQt5.QtWidgets as qt


class QCalc(qt.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        self.fileMenu = qt.QMenu(self)
        self.b = qt.QPushButton("Test", self)
        self.b.show()
        self.fileMenu.show()
        self.show()

app = qt.QApplication(sys.argv)
q = QCalc()
sys.exit(app.exec_())