import sqlite3


class Bot:
    id = None
    name = None
    bot_type = None
    depo = None
    percent_to_profit = None
    plan = None

    def __init__(self):
        super().__init__()

        # Соединяемся с базой
        self.conn = sqlite3.connect('bot')

    def get_info(self):
        botinfo = self.conn.execute('SELECT * FROM hunkies WHERE name = \'' + str(self.name) + '\'')
        return botinfo.fetchone()

    def get_all(self):
        return self.conn.execute('SELECT * FROM hunkies ORDER BY Id')

    def update(self, new_bot_name):
        set_string = "name = '" + new_bot_name + "'"
        set_string += ", bot_type = '" + self.bot_type + "'"
        set_string += ", depo = " + str(float(self.depo))
        set_string += ", percent_to_profit = " + str(float(self.percent_to_profit))
        try:
            self.conn.execute("UPDATE hunkies SET " + set_string + " WHERE name = '" + self.name + "'")
            self.conn.commit()
            self.name = new_bot_name
            return True
        except Exception:
            return False

    def __del__(self):
        self.conn.close()
