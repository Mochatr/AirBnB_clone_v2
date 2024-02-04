#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
using the function do_deploy
"""

from fabric.api import env, put, run
from os.path import isfile


env.hosts = ['54.146.83.181', '54.210.196.216']


def do_deploy(archive_path):
    if not isfile(archive_path):
        return False

    # Upload the archive
    put(archive_path, '/tmp/')

    # Extract the filename without extension
    file_name = archive_path.split("/")[-1]
    name = file_name.split(".")[0]

    # Define the directories
    remote_path = "/data/web_static/releases/{}/".format(name)

    # Create directory
    run("mkdir -p {}".format(remote_path))
    # Uncompress the archive
    run("tar -xzf /tmp/{} -C {}".format(file_name, remote_path))
    # Delete archive
    run("rm /tmp/{}".format(file_name))

    # Delete the symbolic link
    run("rm -rf /data/web_static/current")
    # Create a new one
    run("ln -s {} /data/web_static/current".format(remote_path))

    print("New version deployed!")
    return True
