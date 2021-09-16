
import datetime
from application.models import MongoDB


def list_project(pageNo, pageSize):
    return MongoDB['project'].find().limit(int(pageSize)).skip(int(pageNo))


def list_project_count():
    return MongoDB['project'].find().count()


def get_project(query):
    return MongoDB['project'].find_one(query)


def add_project(data):
    MongoDB['project'].insert(data)


def update_project(query, data):
    # project = MongoDB['project'].find_one(query)
    MongoDB['project'].update(query,  data)


def delete_project(query):
    MongoDB['project'].find_one_and_delete(query)
