from flask import Flask, request, jsonify, url_for
from src import app 
from src.models.assistsmodel import AssistsModel
from src.config.db import DB

@app.route("/assists", methods=["GET"])
def gets_assists():
    assistsModel = AssistsModel()
    
    assists = assistsModel.getall()

    return jsonify({
        'message': 'list assists',
        's_assists': assists
    })

@app.route("/assists", methods=["POST"])
def create_assistance():
    createassistance = AssistsModel()

    data={
        'session_id': request.json["session_id"],
        'student_id': request.json["student_id"],
        'assistance': request.json["assistance"]
    }

    createassistance.create(data)
    assists = createassistance.getall()

    return jsonify({
        'message': 'add assistance',
        's_assits': assists
    })

@app.route("/assists/<id>", methods=["PUT"])
def edit_assistance(id):
    editassistance = AssistsModel()

    data={
        'id': request.json['id'],
        'session_id': request.json["session_id"],
        'student_id': request.json["student_id"],
        'assistance': request.json["assistance"]
    }
    
    editassistance.edit(data)
    assistance = editassistance.getone(id)

    return jsonify({
        'message': 'update assistance',
        's_assistance': assistance
    })

@app.route("/assists/<id>", methods=["DELETE"])
def delete_assistance(id):
    deleteassistance = AssistsModel()
    getdelete = deleteassistance.getone(id)
    deleteassistance.delete(id)
    
    return jsonify({
        'message': 'Delete assistance',
        's_assistance': getdelete
    })