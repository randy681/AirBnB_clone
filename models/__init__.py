#!/usr/bin/python3
""" __init__.py method for model package """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
