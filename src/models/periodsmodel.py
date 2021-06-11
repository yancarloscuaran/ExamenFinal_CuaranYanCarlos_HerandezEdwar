from src.config.db import DB

class PeriodsModel():
    def getall(self):
        cursor = DB.cursor()

        cursor.execute('SELECT id, year, period FROM periods')

        periods = cursor.fetchall()

        cursor.close()
        return periods

    def getone(self, id):
        cursor = DB.cursor()

        cursor.execute('SELECT id, year, period FROM periods WHERE id=?', (id,))

        period = cursor.fetchone()

        cursor.close()
        return period


    def create(self, data):
        cursor = DB.cursor()

        cursor.execute('insert into periods(year, period) values(?,?)', (data['year'], data['period'],))


        cursor.close()


    def edit(self, data):
        cursor = DB.cursor()

        cursor.execute('UPDATE periods SET year=?, period=? WHERE id=?', (data['year'], data['period'], data['id']))

        cursor.close()


    def delete(self, id):
        cursor = DB.cursor()

        cursor.execute('DELETE FROM periods WHERE id=?', (id,))

        cursor.close()