from settingsmaket import Ui_Dialog as Settings_UI_Dialog
from PyQt5 import QtWidgets
from bot import Bot


class SettingsDialog:

    # Инициируем класс и запускаем основное окно программы
    def __init__(self):
        super().__init__()
        self.settings_window = QtWidgets.QDialog()
        self.settingsui = Settings_UI_Dialog()
        self.settingsui.setupUi(self.settings_window)
        self.settings_window.show()

        # Устанавливаем связь с классом бота
        self.bot = Bot()

        # Заполняем поле выбора бота
        self.fillup()

        # Навешиваем обработчик на выбор бота
        self.settingsui.comboBox.currentIndexChanged.connect(self.fillbotinfo)

        # Навешиваем обработчик на сохранение бота
        self.settingsui.pushButton.clicked.connect(self.savebotinfo)

    # Заполняем пустые поля данными из базы
    def fillup(self):
        self.settingsui.comboBox.addItem('Выберите бота')
        all_bot_info = self.bot.get_all()
        for row in all_bot_info:
            self.settingsui.comboBox.addItem(row[1])

    # Заполняем поля информацией о боте
    def fillbotinfo(self):
        self.bot.name = self.settingsui.comboBox.currentText()
        botinfo = self.bot.get_info()
        self.settingsui.lineEdit.setText(botinfo[1] if botinfo[1] != 'None' else '')
        self.settingsui.lineEdit_2.setText(botinfo[2] if botinfo[2] != 'None' else '')
        self.settingsui.lineEdit_3.setText(str(botinfo[3]) if str(botinfo[3]) != 'None' else '')
        self.settingsui.lineEdit_4.setText('{0:.11f}'.format(botinfo[10]) if str(botinfo[10]) != 'None' else '')

    # Сохраняем изменения для бота
    def savebotinfo(self):
        # Собираем информацию для обновления бота

        # Старое название бота
        self.bot.name = self.settingsui.comboBox.currentText()

        # Новый тип бота
        self.bot.bot_type = self.settingsui.lineEdit_2.text()

        # Новое депо бота
        self.bot.depo = self.settingsui.lineEdit_3.text()

        # Новое значени процента до профита у бота
        self.bot.percent_to_profit = self.settingsui.lineEdit_4.text()

        error = False
        error_text = None

        # Проводим валидацию полей перед сохранением
        if self.settingsui.comboBox.currentIndex() == 0:
            error = True
            error_text = "Не выбран бот для которого требуется произвести сохранение"

        if not self.settingsui.lineEdit.text() and not error:
            error = True
            error_text = 'Не заполнено поле "Название"'

        if not self.settingsui.lineEdit_2.text() and not error:
            error = True
            error_text = 'Не заполнено поле "Тип Бота"'

        if not self.settingsui.lineEdit_3.text() and not error:
            error = True
            error_text = 'Не заполнено поле "Депо"'

        if not self.settingsui.lineEdit_3.text() and not error:
            error = True
            error_text = 'Не заполнено поле "Профит (в %)"'

        if error:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText(error_text)
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        else:
            # Запускаем процедуру записи изменений для бота
            if self.bot.update(self.settingsui.lineEdit.text()):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Информация удачно сохранена')
                msg.setWindowTitle("Успех")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()