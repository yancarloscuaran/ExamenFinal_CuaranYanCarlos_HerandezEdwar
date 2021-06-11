from flask import Flask, request, jsonify, url_for
from src import app 
from src.models.notesmodel import NotesModel
from src.config.db import DB

@app.route("/notes", methods=["GET"])
def gets_studentsnotes():
    notesModel = NotesModel()
 
    notes = notesModel.getall()

    return jsonify({
        'message': 'list students notes',
        'notes': notes
    })

@app.route("/notes", methods=["POST"])
def create_studentnote():
    createnote = NotesModel()

    data={
        'performed_activity_id': request.json["performed_activity_id"],
        'student_id': request.json["student_id"],
        'note': request.json["note"],
        'observation': request.json["observation"]
    }

    createnote.create(data)
    notes = createnote.getall()

    return jsonify({
        'message': 'add student note',
        'notes': notes
    })

@app.route("/notes/<id>", methods=["PUT"])
def edit_studentnote(id):
    editnote = NotesModel()

    data={
        'id': request.json['id'],
        'performed_activity_id': request.json["performed_activity_id"],
        'student_id': request.json["student_id"],
        'note': request.json["note"],
        'observation': request.json["observation"]
    }
    
    editnote.edit(data)
    note = editnote.getone(id)

    return jsonify({
        'message': 'update student note',
        'note': note
    })

@app.route("/notes/<id>", methods=["DELETE"])
def delete_studentnote(id):
    deletestudentnote = NotesModel()
    getdelete = deletestudentnote.getone(id)
    deletestudentnote.delete(id)
    
    return jsonify({
        'message': 'Delete student note',
        'note': getdelete
    })