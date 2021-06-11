from flask import Flask, request, jsonify, url_for
from src import app 
from src.models.studentsmodel import StudentsModel
from src.config.db import DB

@app.route("/students", methods=["GET"])
def gets_students():
    studentsModel = StudentsModel() 
    
    students = studentsModel.getall()

    return jsonify({
        'message': 'list students',
        'students': students
    })

@app.route("/students", methods=["POST"])
def create_student():
    createstudent = StudentsModel()

    data={
        'identification': request.json["identification"],
        'name': request.json["name"],
        'surname': request.json["surname"],
        'phone': request.json["phone"],
        'email': request.json["email"],
        'semester': request.json["semester"],
        'period_id': request.json["period_id"]
    }

    createstudent.create(data)
    students = createstudent.getall()

    return jsonify({
        'message': 'add student',
        'students': students
    })

@app.route("/students/<id>", methods=["PUT"])
def edit_student(id):
    editstudent = StudentsModel()

    data={
        'id': request.json["id"],
        'identification': request.json["identification"],
        'name': request.json["name"],
        'surname': request.json["surname"],
        'phone': request.json["phone"],
        'email': request.json["email"],
        'semester': request.json["semester"],
        'period_id': request.json["period_id"]
    }
    
    editstudent.edit(data)
    student = editstudent.getone(id)

    return jsonify({
        'message': 'update student',
        'student': student
    })

@app.route("/students/<id>", methods=["DELETE"])
def delete_student(id):
    deletestudent = StudentsModel()
    getdelete = deletestudent.getone(id)
    deletestudent.delete(id)
    
    return jsonify({
        'message': 'Delete student',
        'student': getdelete
    })

# @app.route("/estudiantes/<id>", methods=["GET"])
# def traer_uno(id):
#     buscarestudiante = EstudiantesModel()
#     buscarestudiante.traeruno(id)
#     return jsonify(buscarestudiante)