import sys
from maket import *
from settings import SettingsDialog
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui
from workthread import WorkThread
from log import Log


class MainWindow:

    # Инициируем класс и запускаем основное окно программы
    def __init__(self):
        super().__init__()
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        self.main_window.show()

        # Инициируем класс работы с потоками и передаём текущий класс для обратной связи
        self.workthread = WorkThread()
        self.workthread.setMainWindow(self)

        # Навешиваем на кнопку из верхнего меню открытие дополнительного окна
        self.ui.settings.triggered.connect(self.open_settings)

        # Отмечаем в логах, что запустили программу
        self.ui.textEdit.setText(Log.read())
        self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)

    def run(self):
        self.workthread.start()

    def open_settings(self):
        self.settings_window = SettingsDialog()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()

    # Устанавливаем таймер для опроса биржи каждые три секунды
    timer = QTimer()
    timer.timeout.connect(window.run)
    timer.start(3000)

    sys.exit(app.exec_())
