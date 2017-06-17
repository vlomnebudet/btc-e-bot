from platform import system as system_name # Возвращает название операционной системы
from os import system as system_call       # Исполняет команду оболочки


class HostChecker:
    @staticmethod
    def ping(host):

        # Параметры пинга в завичимости от операцмонной системы
        parameters = "-n 1" if system_name().lower()=="windows" else "-c 1"

        # Пингуем и возвращаем результат
        return system_call("ping " + parameters + " " + host) == 0
