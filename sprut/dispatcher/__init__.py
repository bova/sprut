__author__ = 'bova'

from sprut.db.conn import Session
from sprut.db.schema import SpOraInstance
from sprut.remoting import RemoteCommand
import time


class Dispatcher(object):
    def __init__(self):
        self.db = Session()

    def run(self):
        while True:
            instances = self.db.query(SpOraInstance).filter(SpOraInstance.command.isnot(None)).all()
            print 'Selected %s instances' % len(instances)
            if instances:
                for instance in instances:
                    print 'Run command: %s on host: %s with sid: %s' % (instance.command,
                                                                        instance.server.hostname,
                                                                        instance.sid)
                    rmt_cmd = RemoteCommand(instance)
                    rmt_cmd.run()
                    instance.command = None
                    self.db.commit()
            else:
                print 'Sleeping on 3sec...'
                time.sleep(3)


if __name__ == '__main__':
    dispatcher = Dispatcher()
    dispatcher.run()