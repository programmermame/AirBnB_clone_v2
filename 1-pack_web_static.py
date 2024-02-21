#!/usr/bin/python3
"""a fabric script to create an archive file"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ a method to compress a file and return it's path """

    """saving the current timestamp and creatinf filename"""
    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(time_now)

    try:
        """create a directory called versions"""
        local("mkdir -p versions")

        """create an archive file"""
        local("tar -cvzf {} web_static/".format(file_path))

        """return the path to the archive file created"""
        return "{}".format(file_path)

        """return none if an error occurs"""
    except Exception as e:
        return None
