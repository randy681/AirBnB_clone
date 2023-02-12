#!/usr/bin/python3
"""
Init for filestorage
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
