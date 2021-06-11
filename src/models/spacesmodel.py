from src.config.db import DB

class SpacesModel():
    def getall(self):
        cursor = DB.cursor()

        cursor.execute('SELECT academic_spaces.id, CONCAT(periods.year, "(", periods.period, ")") AS period, academic_spaces.name, academic_spaces.semester FROM academic_spaces INNER JOIN periods ON academic_spaces.period_id = periods.id ')

        spaces = cursor.fetchall()

        cursor.close()
        return spaces

    def getone(self, id):
        cursor = DB.cursor()

        cursor.execute('SELECT academic_spaces.id, CONCAT(periods.year, "(", periods.period, ")") AS period, academic_spaces.name, academic_spaces.semester FROM academic_spaces INNER JOIN periods ON academic_spaces.period_id = periods.id WHERE academic_spaces.id = ?', (id,))

        space = cursor.fetchone()

        cursor.close()
        return space


    def create(self, data):
        cursor = DB.cursor()

        cursor.execute('insert into academic_spaces(period_id, name, semester) values(?,?,?)', (data['period_id'], data['name'], data['semester'],))


        cursor.close()


    def edit(self, data):
        cursor = DB.cursor()

        cursor.execute('UPDATE academic_spaces SET period_id=?, name=?, semester=? WHERE id=?', (data['period_id'], data['name'], data['semester'], data['id'],))

        cursor.close()


    def delete(self, id):
        cursor = DB.cursor()

        cursor.execute('DELETE FROM academic_spaces WHERE id=?', (id,))

        cursor.close()