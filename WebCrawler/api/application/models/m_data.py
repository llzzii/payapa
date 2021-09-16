
import datetime
from application.models import MongoDB


def list_data_db():
    return MongoDB.list_collection_names()


def list_data_by_project(project, pageNo, pageSize):
    return MongoDB[project].find().limit(int(pageSize)).skip(int(pageNo))


def list_data_count(project):
    return MongoDB[project].find().count()
