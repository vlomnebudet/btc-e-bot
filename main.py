from maket import *
from PyQt5.QtCore import QTimer
from hostchecker import *


class MainWindow:

    # Инициируем класс и запускаем основное окно программы
    def __init__(self):
        super().__init__()
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        self.main_window.show()

    # Метод - точка запуска очередной итерации по таймеру
    def repeater(self):
        available = self.hostchecker()
        if available:
            self.ui.label.setStyleSheet("background-color: rgb(0, 170, 0);")
        else:
            self.ui.label.setStyleSheet("background-color: rgb(170, 0, 0);")

    # Метод обёртка для метода проверки доступности биржи
    def hostchecker(self):
        return HostChecker.ping('btc-e.nz')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()

    # Устанавливаем таймер для опроса биржи каждые три секунды
    timer = QTimer()
    timer.timeout.connect(window.repeater)
    timer.start(3000)

    sys.exit(app.exec_())
