from src.config.db import DB

class ActivitiesModel():
    def getall(self):
        cursor = DB.cursor()

        cursor.execute('SELECT performed_activities.id, academic_spaces.name, CONCAT("cut", " (", performed_activities.cut,")") AS cuts, performed_activities.name, performed_activities.average_cut FROM performed_activities INNER JOIN academic_spaces ON performed_activities.academic_space_id = academic_spaces.id')

        activities = cursor.fetchall()

        cursor.close()
        return activities

    def getone(self, id):
        cursor = DB.cursor()

        cursor.execute('SELECT performed_activities.id, academic_spaces.name, CONCAT("cut", " (", performed_activities.cut,")") AS cuts, performed_activities.name, performed_activities.average_cut FROM performed_activities INNER JOIN academic_spaces ON performed_activities.academic_space_id = academic_spaces.id WHERE performed_activities.id = ?', (id,))

        activity = cursor.fetchone()

        cursor.close()
        return activity


    def create(self, data):
        cursor = DB.cursor()

        cursor.execute('insert into performed_activities(academic_space_id, cut, name, average_cut) values(?,?,?,?)', (data['academic_space_id'], data['cut'], data['name'], data['average_cut'],))


        cursor.close()


    def edit(self, data):
        cursor = DB.cursor()

        cursor.execute('UPDATE performed_activities SET academic_space_id=?, cut=?, name=?, average_cut=? WHERE id=?', (data['academic_space_id'], data['cut'], data['name'], data['average_cut'], data['id'],))

        cursor.close()


    def delete(self, id):
        cursor = DB.cursor()

        cursor.execute('DELETE FROM performed_activities WHERE id=?', (id,))

        cursor.close()