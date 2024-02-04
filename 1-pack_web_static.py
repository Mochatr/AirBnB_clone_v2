#!/usr/bin/python3
# This script generates a .tgz archive
# From the contents of the web_static folder

from fabric.api import local
from datetime import datetime


def do_pack():
    """This function generates a tgz archive"""
    try:
        datetime = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(date_time)

        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_path))

        return archive_path
    except Exception as e:
        return None
