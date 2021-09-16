
from pymongo.message import update
from application.common.JSONEncoder import JSONEncoder
from application.models.m_project import delete_project, list_project, add_project, list_project_count, update_project
from application.models import MongoDB
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from bson import ObjectId
import json


class ProjectApi(Resource):
    def get(self):
        pageNo = request.args.get("pageNo")
        pageSize = request.args.get("pageSize")
        pro = list_project(pageNo, pageSize)
        lists = []
        for item in list(pro):
            lists.append(json.loads(JSONEncoder().encode(item)))
        count = list_project_count()
        return {'code': 10000, 'msg': 'get list success', 'data': lists, 'total': count}

    def post(self):
        json_data = request.get_json()
        print(json_data)
        result = add_project(json_data)
        return {'code': 10000, 'msg': 'add project success', 'data': JSONEncoder().encode(result)}

    def put(self):
        json_data = request.get_json()
        id = request.args.get("id")
        result = update_project(
            {'_id':  ObjectId(id)}, json_data)
        return {'code': 10000, 'msg': 'update project success', 'data': JSONEncoder().encode(result)}

    def delete(self):
        id = request.args.get("id")
        result = delete_project({'_id': ObjectId(id)})
        return {'code': 10000, 'msg': 'delete project success', 'data': JSONEncoder().encode(result)}
