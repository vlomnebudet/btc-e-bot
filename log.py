import os
import shutil
import datetime

class Log:

    @staticmethod
    def refresh(text=None):
        clearlog = False
        # Проверяем файл на лимит по размеру
        # При надобности перемещаем файл в архив и сообщаем об этом в поле лога
        if os.stat('log').st_size >= 5242880:
            try:
                os.mkdir('archive')
            except Exception:
                pass

            shutil.copy2(r'log', r'archive/log_' + str(datetime.datetime.now().strftime("%y.%m.%d")))

            #   Удаляем содержимое файла
            with open('log', 'w'):
                pass
            clearlog = True

        if text is not None:
            if clearlog:
                text = "Лог был перемещён в архив, ведение лога начато с начала\n" + text
            text = str(datetime.datetime.now().strftime("%y.%m.%d %H:%M:%S")) + " : " + text + "\n"
            f = open('log', 'a')
            f.write(text)
            f.close()

        f = open('log', 'r')
        read_text = f.read()
        f.close()
        return read_text
