from src.config.db import DB

class AssistsModel():
    def getall(self):
        cursor = DB.cursor()

        cursor.execute('SELECT assists.id, sessions.date, students.name, assists.assistance FROM assists INNER JOIN sessions ON assists.session_id = sessions.id INNER JOIN students ON assists.student_id = students.id')

        assists = cursor.fetchall()

        cursor.close()
        return assists

    def getone(self, id):
        cursor = DB.cursor()

        cursor.execute('SELECT assists.id, sessions.date, students.name, assists.assistance FROM assists INNER JOIN sessions ON assists.session_id = sessions.id INNER JOIN students ON assists.student_id = students.id WHERE assists.id = ?', (id,))

        assistance = cursor.fetchone()

        cursor.close()
        return assistance


    def create(self, data):
        cursor = DB.cursor()

        cursor.execute('insert into assists(session_id, student_id, assistance) values(?,?,?)', (data['session_id'], data['student_id'], data['assistance'],))


        cursor.close()


    def edit(self, data):
        cursor = DB.cursor()

        cursor.execute('UPDATE assists SET session_id=?, student_id=?, assistance=? WHERE id=?', (data['session_id'], data['student_id'], data['assistance'], data['id'],))

        cursor.close()


    def delete(self, id):
        cursor = DB.cursor()

        cursor.execute('DELETE FROM assists WHERE id=?', (id,))

        cursor.close()