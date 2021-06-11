from flask import Flask, request, jsonify, url_for
from src import app 
from src.models.sessionsmodel import SessionsModel
from src.config.db import DB

@app.route("/sessions", methods=["GET"])
def gets_sessions():
    sessionsModel = SessionsModel()
    
    sessions = sessionsModel.getall()

    return jsonify({
        'message': 'list sessions',
        'sessions': sessions
    })

@app.route("/sessions", methods=["POST"])
def create_session():
    createsession = SessionsModel()

    data={
        'academic_space_id': request.json["academic_space_id"],
        'cut': request.json["cut"],
        'date': request.json["date"],
        'start_time': request.json["start_time"],
        'end_time': request.json["end_time"]
    }

    createsession.create(data)
    sessions = createsession.getall()

    return jsonify({
        'message': 'add sessions',
        'sessions': sessions
    })

@app.route("/sessions/<id>", methods=["PUT"])
def edit_session(id):
    editsession = SessionsModel()

    data={
        'id': request.json['id'],
        'academic_space_id': request.json["academic_space_id"],
        'cut': request.json["cut"],
        'date': request.json["date"],
        'start_time': request.json["start_time"],
        'end_time': request.json["end_time"]
    }
    
    editsession.edit(data)
    session = editsession.getone(id)

    return jsonify({
        'message': 'update session',
        'session': session
    })

@app.route("/sessions/<id>", methods=["DELETE"])
def delete_session(id):
    deletesession =SessionsModel()
    getdelete = deletesession.getone(id)
    deletesession.delete(id)
    
    return jsonify({
        'message': 'Delete session',
        'session': getdelete
    })