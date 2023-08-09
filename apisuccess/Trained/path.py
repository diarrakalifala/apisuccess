import inspect, os
from django.conf import settings
from apisuccess.settings import BASE_DIR

def getJsonPath():
    path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = os.path.join(path, 'dataset/content.json').replace("\\", "/")
    return path

def getPath(file):
    path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = os.path.join(path, file).replace("\\", "/")
    return path

