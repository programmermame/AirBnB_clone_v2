#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['34.234.203.81', '174.129.183.12']


def do_deploy(archive_path):
  """
  distributes an archive to the web servers
  """
  if not exists(archive_path):
    return False
  try:
    file_name = archive_path.split("/")[-1]
    no_ext = file_name.split(".")[0]
    path = "/data/web_static/releases/"

    # Upload archive
    warn(f"Uploading archive to {env.host}...")
    put(archive_path, '/tmp/')

    # Create directory
    puts(f"Creating directory on {env.host}: {path}{no_ext}")
    run('mkdir -p {}{}/'.format(path, no_ext))

    # Uncompress archive
    puts(f"Uncompressing archive on {env.host}...")
    run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_ext))

    # Remove temporary archive
    puts(f"Removing temporary archive on {env.host}...")
    run('rm /tmp/{}'.format(file_name))

    # Move extracted files
    puts(f"Moving files on {env.host}...")
    run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))

    # Remove old web_static directory
    puts(f"Removing old web_static directory on {env.host}...")
    run('rm -rf {}{}/web_static'.format(path, no_ext))

    # Remove current symlink
    puts(f"Removing current symlink on {env.host}...")
    run('rm -rf /data/web_static/current')

    # Create new symlink
    puts(f"Creating new symlink on {env.host}...")
    run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))

    return True
  except:
    return False
