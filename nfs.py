# coding: utf-8

from fabkit import *  # noqa
from fablib.base import SimpleBase


class NFS(SimpleBase):
    def __init__(self, enable_services=['.*']):
        self.data_key = 'nfs'
        self.data = {
        }

        self.packages = {
            'CentOS Linux 7.*': [
                'nfs-utils',
            ],
        }

        self.services = ['rpcbind', 'nfs-server']

    def setup(self):
        data = self.init()

        self.install_packages()
        self.start_services().enable_services()

        for export in data['exports']:
            filer.mkdir(export[0])

        if filer.template('/etc/exports', data=data):
            self.handlers['restart_nfs-server'] = True

        self.exec_handlers()
        self.check()

    def check(self):
        data = self.init()
        for export in data['exports']:
            sudo('exportfs | grep "{0} "'.format(export[0]))

        sudo('nfsstat')
