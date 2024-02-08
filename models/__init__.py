#!/usr/bin/python3
from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

# Use a dictionary for storage types
storage_types = {
    "file": FileStorage(),
    "db": DBStorage(),
}

# Get the storage type from the environment variable (default to "file")
storage_type = getenv("HBNB_TYPE_STORAGE", "file").lower()

# Choose the appropriate storage instance
storage = storage_types.get(storage_type, FileStorage())

# Reload the storage
storage.reload()
