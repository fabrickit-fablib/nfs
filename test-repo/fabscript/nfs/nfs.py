# coding: utf-8

from fabkit import task
from fablib.nfs import NFS


@task
def setup():
    nfs = NFS()
    nfs.setup()
