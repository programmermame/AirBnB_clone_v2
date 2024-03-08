#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import env, put, run


def do_deploy(archive_path):

  if not exists(archive_path):
    return False

  try:
    filename = archive_path.split("/")[-1]
    dirname = filename.split(".")[0]
    release_path = "/data/web_static/releases/{}".format(dirname)

    put(archive_path, "/tmp/{}".format(filename))
    run("mkdir -p {}".format(release_path))
    run("tar -xzf /tmp/{} -C {}".format(filename, release_path))
    run("rm /tmp/{}".format(filename))
    run("mv {}/* {}".format(release_path, release_path))
    run("rm -rf {}/web_static".format(release_path))
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(release_path))
    return True
  except:
    return False


env.hosts = ["34.234.203.81", "174.129.183.12"]
