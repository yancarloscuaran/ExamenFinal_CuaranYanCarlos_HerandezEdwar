from flask import Flask, request, jsonify, url_for
from src import app 
from src.models.spacesmodel import SpacesModel
from src.config.db import DB

@app.route("/spaces", methods=["GET"])
def gets_spaces():
    spacesModel = SpacesModel() 
    spaces = spacesModel.getall()

    return jsonify({
        'message': 'list academic spaces',
        'students': spaces
    })

@app.route("/spaces", methods=["POST"])
def create_spaces():
    createspace = SpacesModel()

    data={
        'period_id': request.json["period_id"],
        'name': request.json["name"],
        'semester': request.json["semester"]
    }

    createspace.create(data)
    spaces = createspace.getall()

    return jsonify({
        'message': 'add space',
        'spaces': spaces
    })

@app.route("/spaces/<id>", methods=["PUT"])
def edit_space(id):
    editspace = SpacesModel()

    data={
        'id': request.json['id'],
        'period_id': request.json["period_id"],
        'name': request.json["name"],
        'semester': request.json["semester"]
    }
    
    editspace.edit(data)
    space = editspace.getone(id)

    return jsonify({
        'message': 'update academic space',
        'space': space
    })

@app.route("/spaces/<id>", methods=["DELETE"])
def delete_space(id):
    deletespace = SpacesModel()
    getdelete = deletespace.getone(id)
    deletespace.delete(id)
    
    return jsonify({
        'message': 'Delete academic space',
        'space': getdelete
    })
