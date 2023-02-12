#!/usr/bin/python3
"""
magic method for the models dir
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
