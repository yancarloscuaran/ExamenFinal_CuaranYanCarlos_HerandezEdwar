from src.config.db import DB

class StudentsModel():
    def getall(self):
        cursor = DB.cursor()

        cursor.execute('SELECT students.id, students.identification, students.name, students.surname, students.phone, students.email, students.semester, CONCAT(periods.year, "(", periods.period, ")") AS periods FROM students INNER JOIN periods ON students.period_id = periods.id')

        students = cursor.fetchall()

        cursor.close()
        return students


    def getone(self, id):
        cursor = DB.cursor()

        cursor.execute('SELECT students.id, students.identification, students.name, students.surname, students.phone, students.email, students.semester, CONCAT(periods.year, "(", periods.period, ")") AS periods FROM students INNER JOIN periods ON students.period_id = periods.id WHERE students.id = ?', (id,))

        student = cursor.fetchone()

        cursor.close()
        return student


    def create(self, data):
        cursor = DB.cursor()

        cursor.execute('insert into students(identification, name, surname, phone, email, semester, period_id) values(?,?,?,?,?,?,?)', (data['identification'], data['name'], data['surname'], data['phone'], data['email'], data['semester'], data['period_id'],))


        cursor.close()


    def edit(self, data):
        cursor = DB.cursor()

        cursor.execute('UPDATE students SET identification=?, name=?, surname=?, phone=?, email=?, semester=?, period_id=?  WHERE id=?', (data['identification'], data['name'], data['surname'], data['phone'], data['email'], data['semester'], data['period_id'], data['id'],))

        cursor.close()


    def delete(self, id):
        cursor = DB.cursor()

        cursor.execute('DELETE FROM students WHERE id=?', (id,))

        cursor.close()



