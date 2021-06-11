from flask import Flask, request, jsonify, url_for
from src import app 
from src.models.activitiesmodel import ActivitiesModel
from src.config.db import DB

@app.route("/activities", methods=["GET"])
def gets_activities():
    activitiesModel = ActivitiesModel() 
    
    activities = activitiesModel.getall()

    return jsonify({
        'message': 'list performed activities',
        'pf_activities': activities
    })

@app.route("/activities", methods=["POST"])
def create_activity():
    createactivity = ActivitiesModel()

    data={
        'academic_space_id': request.json["academic_space_id"],
        'cut': request.json["cut"],
        'name': request.json["name"],
        'average_cut': request.json["average_cut"]
    }

    createactivity.create(data)
    activities = createactivity.getall()

    return jsonify({
        'message': 'add performed activities',
        'pf_activities': activities
    })

@app.route("/activities/<id>", methods=["PUT"])
def edit_activity(id):
    editactivity = ActivitiesModel()

    data={
        'id': request.json['id'],
        'academic_space_id': request.json["academic_space_id"],
        'cut': request.json["cut"],
        'name': request.json["name"],
        'average_cut': request.json["average_cut"]
    }
    
    editactivity.edit(data)
    activity = editactivity.getone(id)

    return jsonify({
        'message': 'update activity',
        'pf_activity': activity
    })

@app.route("/activities/<id>", methods=["DELETE"])
def delete_activity(id):
    deleteactivity = ActivitiesModel()
    getdelete = deleteactivity.getone(id)
    deleteactivity.delete(id)
    
    return jsonify({
        'message': 'Delete activity',
        'pf_activity': getdelete
    })
