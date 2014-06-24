__author__ = 'bova'

import ConfigParser


class Database(object):
    path = ''


class SprutConfig():
    def __init__(self):
        self.cfg = ConfigParser.ConfigParser()
        self.cfg.read(['/etc/sprut/sprut.conf', 'c:/tmp/sprut.conf'])
        self.init_variables()
        self.populate_variables()

    def init_variables(self):
        self.db = Database()

    def populate_variables(self):
        self.db.path = self.cfg.get('database', 'path')
