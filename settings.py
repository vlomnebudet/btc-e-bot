from settingsmaket import Ui_Dialog as Settings_UI_Dialog
from PyQt5 import QtWidgets
import sqlite3


class SettingsDialog:

    # Инициируем класс и запускаем основное окно программы
    def __init__(self):
        super().__init__()
        self.settings_window = QtWidgets.QDialog()
        self.settingsui = Settings_UI_Dialog()
        self.settingsui.setupUi(self.settings_window)
        self.settings_window.show()

        # Соединяемся с базой
        self.conn = sqlite3.connect('bot')

        # Заполняем поле выбора бота
        self.fillup()

        # Навешиваем обработчик на выбор бота
        self.settingsui.comboBox.currentIndexChanged.connect(self.fillbotinfo)

    # Заполняем пустые поля данными из базы
    def fillup(self):
        self.settingsui.comboBox.addItem('Выберите бота')
        for row in self.conn.execute('SELECT * FROM hunkies ORDER BY Id'):
            self.settingsui.comboBox.addItem(row[1])

    # Заполняем поля информацией о боте
    def fillbotinfo(self):
        botinfo = self.conn.execute('SELECT * FROM hunkies WHERE Id = ' + str(self.settingsui.comboBox.currentIndex()))
        botinfo = botinfo.fetchone()
        self.settingsui.lineEdit.setText(botinfo[1])
        self.settingsui.lineEdit_2.setText(botinfo[2])
        self.settingsui.lineEdit_3.setText(str(botinfo[3]))
        # self.settingsui.lineEdit_4.setText(str(float(botinfo[10])))
        self.settingsui.lineEdit_4.setText('{0:.11f}'.format(botinfo[10]))

    def __del__(self):
        self.conn.close()
