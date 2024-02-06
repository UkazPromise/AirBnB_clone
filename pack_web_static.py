!/usr/bin/python3
"""A module for Fabric script that generates a .tgz archive."""
import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """Archives the static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")

    current_time = datetime.now()
    output = f"versions/web_static_{current_time:%Y%m%d%H%M%S}.tgz"

    try:
        print(f"Packing web_static to {output}")
        local(f"tar -cvzf {output} web_static")
        size = os.stat(output).st_size
        print(f"web_static packed: {output} -> {size} Bytes")
    except FileNotFoundError:
        print("Error: Unable to find the 'web_static' directory.")
        output = None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        output = None

    return output
