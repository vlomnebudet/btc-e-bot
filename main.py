from maket import *


class MainWindow:

    def __init__(self):
        super().__init__()
        self.MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(self.MainWindow)
        self.MainWindow.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
