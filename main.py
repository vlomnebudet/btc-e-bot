from maket import *
from PyQt5.QtCore import QTimer


class MainWindow:
    schet = "1";

    def __init__(self):
        super().__init__()
        self.main_window = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(self.main_window)
        self.main_window.show()

    def local_button_handler(self):
        self.main_window.setWindowTitle("Лошадь со скальпелем" + self.schet)
        self.schet += "1"


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()

    # Устанавливаем таймер для опроса биржи каждые три секунды
    timer = QTimer()
    timer.timeout.connect(window.local_button_handler)
    timer.start(3000)

    sys.exit(app.exec_())
