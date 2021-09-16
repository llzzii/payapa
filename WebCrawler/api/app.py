from application.service.data_project import DataProjectApi
from application.service.data import DataApi
from application.service.project import ProjectApi
from application.crawler.action import ActionApi
from application.crawler.crawler.spiders.project_crawler import ProjectCrawlerSpider

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from scrapy.crawler import CrawlerRunner


flask_app = Flask(__name__)
flask_api = Api(flask_app)


flask_api.add_resource(ProjectApi, '/api/project')
flask_api.add_resource(ActionApi, '/api/project/action')
flask_api.add_resource(DataApi, '/api/data')
flask_api.add_resource(DataProjectApi, '/api/data_project')


if __name__ == '__main__':
    flask_app.run(debug=True)
