import os
import shutil
import datetime

class Log:

    @staticmethod
    def refresh(text=None):
        # Проверяем файл на лимит по размеру
        # При надобности перемещаем файл в архив и сообщаем об этом в поле лога
        if os.stat('log').st_size >= 5242880:
            try:
                os.mkdir('archive')
            except Exception:
                pass

            shutil.copy2(r'log', r'archive/log_' + str(datetime.datetime.now().strftime("%y.%m.%d")))
            text += "Лог был перемещён в архив, ведение лога начато с начала\n"

        if text is not None:
            f = open('log', 'a')
            f.write(text)
            f.close()

        f = open('log')
        read_text = f.read()
        f.close()
        return read_text
