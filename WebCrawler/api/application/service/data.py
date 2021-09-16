
from application.models.m_data import list_data_by_project, list_data_count
from pymongo.message import update
from application.common.JSONEncoder import JSONEncoder
from application.models import MongoDB
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from bson import ObjectId
import json


class DataApi(Resource):
    def get(self):
        pageNo = request.args.get("pageNo")
        pageSize = request.args.get("pageSize")
        project = request.args.get("project")
        pro = list_data_by_project(project, pageNo, pageSize)
        lists = []
        for item in list(pro):
            lists.append(json.loads(JSONEncoder().encode(item)))
        count = list_data_count(project)
        return {'code': 10000, 'msg': 'get list success', 'data': lists, 'total': count}
