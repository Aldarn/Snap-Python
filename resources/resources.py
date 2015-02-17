import os

resourceDirectory = os.path.dirname(os.path.abspath(__file__))

def getResourcePath(path):
	return os.path.join(resourceDirectory, path)