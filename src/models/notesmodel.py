from src.config.db import DB

class NotesModel():

    def getall(self):
        cursor = DB.cursor()

        cursor.execute('SELECT students_notes.id, performed_activities.name AS Activities, students.name AS students , students_notes.note AS notes, students_notes.observation FROM students_notes INNER JOIN performed_activities  ON students_notes.performed_activity_id = performed_activities.id INNER JOIN students ON students_notes.student_id = students.id')

        notes = cursor.fetchall()

        cursor.close()
        return notes


    def getone(self, id):
        cursor = DB.cursor()

        cursor.execute('SELECT students_notes.id, performed_activities.name AS Activities, students.name AS students , students_notes.note AS notes, students_notes.observation FROM students_notes INNER JOIN performed_activities  ON students_notes.performed_activity_id = performed_activities.id INNER JOIN students ON students_notes.student_id = students.id WHERE students_notes.id = ?', (id,))

        note = cursor.fetchone()

        cursor.close()
        return note


    def create(self, data):
        cursor = DB.cursor()

        cursor.execute('insert into students_notes(performed_activity_id, student_id, note, observation) values(?,?,?,?)', (data['performed_activity_id'], data['student_id'], data['note'], data['observation'],))


        cursor.close()


    def edit(self, data):
        cursor = DB.cursor()

        cursor.execute('UPDATE students_notes SET performed_activity_id=?, student_id=?, note=?, observation=?  WHERE id=?', (data['performed_activity_id'], data['student_id'], data['note'], data['observation'], data['id'],))

        cursor.close()


    def delete(self, id):
        cursor = DB.cursor()

        cursor.execute('DELETE FROM students_notes WHERE id=?', (id,))

        cursor.close()