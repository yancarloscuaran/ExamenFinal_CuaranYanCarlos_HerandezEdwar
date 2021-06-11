from src.config.db import DB

class SessionsModel():
    def getall(self):
        cursor = DB.cursor()

        cursor.execute('SELECT sessions.id, academic_spaces.name, CONCAT("cut", " (", sessions.cut,")") AS cuts, sessions.date, sessions.start_time, sessions.end_time FROM sessions INNER JOIN academic_spaces ON sessions.academic_space_id = academic_spaces.id')

        sessions = cursor.fetchall()

        cursor.close()
        return sessions

    def getone(self, id):
        cursor = DB.cursor()

        cursor.execute('SELECT sessions.id, academic_spaces.name, CONCAT("cut", " (", sessions.cut,")") AS cuts, sessions.date, sessions.start_time, sessions.end_time FROM sessions INNER JOIN academic_spaces ON sessions.academic_space_id = academic_spaces.id WHERE sessions.id = ?', (id,))

        session = cursor.fetchone()

        cursor.close()
        return session


    def create(self, data):
        cursor = DB.cursor()

        cursor.execute('insert into sessions(academic_space_id, cut, date, start_time, end_time) values(?,?,?,?,?)', (data['academic_space_id'], data['cut'], data['date'], data['start_time'], data['end_time'],))


        cursor.close()


    def edit(self, data):
        cursor = DB.cursor()

        cursor.execute('UPDATE sessions SET academic_space_id=?, cut=?, date=?, start_time=?, end_time=?  WHERE id=?', (data['academic_space_id'], data['cut'], data['date'], data['start_time'], data['end_time'], data['id'],))

        cursor.close()


    def delete(self, id):
        cursor = DB.cursor()

        cursor.execute('DELETE FROM sessions WHERE id=?', (id,))

        cursor.close()

