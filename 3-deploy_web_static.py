#!/usr/bin/python3
# Fabric script that generates a .tgz archive
# from the contents of the web_static folder
from datetime import datetime
from fabric.api import local, put, run, env
from os.path import exists
env.hosts = ['54.87.205.91', '54.87.240.9']


def do_pack():
    """This function generates a tgz archive"""
    try:
        date_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(date_time)

        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_path))

        return archive_path
    except Exception as e:
        return None


def do_deploy(archive_path):
    if not isfile(archive_path):
        return False
    try:

        # Upload the archive
        put(archive_path, '/tmp/')

        # Extract the filename without extension
        file_name = archive_path.split("/")[-1]
        name = file_name.split(".")[0]

        # Define the directories
        remote_path = "/data/web_static/releases/"

        # Create directory
        run("mkdir -p {}{}".format(remote_path, name))

        # Uncompress the archive
        run("tar -xzf /tmp/{} -C {}{}".format(file_name, remote_path, name))

        run("rm /tmp/{}".format(file_name))

        # Move web static content
        run("mv {0}{1}/web_static/* {0}{1}/".format(remote_path, name))
        # Remove the original folder
        run("rm -rf {}{}/web_static".format(remote_path, name))

        # Delete the symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new one
        run("ln -s {}{}/ /data/web_static/current".format(remote_path, name))
        return True
    except Exception as e:
        return False


def deploy():
    """deploy"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
