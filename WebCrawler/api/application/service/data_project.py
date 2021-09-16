
from application.models.m_data import list_data_db
from pymongo.message import update
from application.common.JSONEncoder import JSONEncoder
from application.models import MongoDB
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from bson import ObjectId
import json


class DataProjectApi(Resource):
    def get(self):
        pro = list_data_db()
        lists = []
        for item in list(pro):
            lists.append(json.loads(JSONEncoder().encode(item)))
        return {'code': 10000, 'msg': 'get list success', 'data': lists}
