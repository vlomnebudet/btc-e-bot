from PyQt5.QtCore import QThread, pyqtSignal
from hostchecker import *


class WorkThread(QThread):
    # Обозначаем свойство как сигнал
    runrepeater = pyqtSignal()
    mainwindow = None

    def __init__(self, parent=None):
        super(WorkThread, self).__init__(parent)

        # Метод - точка запуска очередной итерации по таймеру
    def repeater(self):
        available = self.hostchecker()
        if available:
            self.mainwindow.ui.label.setStyleSheet("background-color: rgb(0, 170, 0);")
        else:
            self.mainwindow.ui.label.setStyleSheet("background-color: rgb(170, 0, 0);")

    # Метод обёртка для метода проверки доступности биржи
    def hostchecker(self):
        return HostChecker.ping('btc-e.nz')

    def run(self):
        # Вызываем срабатывание сигнала
        # self.runrepeater.emit()
        self.repeater()

    def setMainWindow(self, mainWindowClass):
        self.mainwindow = mainWindowClass