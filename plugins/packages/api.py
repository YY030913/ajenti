from aj.api import *


class Package (object):
    def __init__(self, manager):
        self.manager = manager
        self.id = None
        self.name = None
        self.version = None
        self.description = None
        self.is_installed = None
        self.is_upgradeable = None
        self.installed_version = None


@interface
class PackageManager (object):
    id = None
    name = None

    def __init__(self, context):
        self.context = context

    def list(self):
        raise NotImplementedError

    def get(self, id):
        raise NotImplementedError