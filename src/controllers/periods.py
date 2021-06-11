from flask import Flask, request, jsonify, url_for
from src import app 
from src.models.periodsmodel import PeriodsModel
from src.config.db import DB

@app.route("/periods", methods=["GET"])
def gets_periods():
    periodsModel = PeriodsModel()
    
    periods = periodsModel.getall()

    return jsonify({
        'message': 'list periods',
        'periods': periods
    })

@app.route("/periods", methods=["POST"])
def create_period():
    createperiod = PeriodsModel()

    data={
        'year': request.json["year"],
        'period': request.json["period"],
    }

    createperiod.create(data)
    periods = createperiod.getall()

    return jsonify({
        'message': 'add period',
        'periods': periods
    })

@app.route("/periods/<id>", methods=["PUT"])
def edit_period(id):
    editperiod = PeriodsModel()

    data={
        'id': request.json['id'],
        'year': request.json['year'],
        'period': request.json["period"],
    }
    
    editperiod.edit(data)
    period = editperiod.getone(id)

    return jsonify({
        'message': 'update period',
        'period': period
    })

@app.route("/periods/<id>", methods=["DELETE"])
def delete_period(id):
    deleteperiod = PeriodsModel()
    getdelete = deleteperiod.getone(id)
    deleteperiod.delete(id)
    
    return jsonify({
        'message': 'Delete period',
        'period': getdelete
    })

