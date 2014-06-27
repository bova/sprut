__author__ = 'bova'

from sprut.db.conn import Session
from sprut.db.schema import SpOraInstance
from sprut.remoting import OraStatusCommand
import time


class OraInstanceChecker(object):
    def __init__(self):
        self.db = Session()

    def get_pmon_status(self, instance):
        rmt_cmd = OraStatusCommand(instance)
        rmt_cmd.run()
        return rmt_cmd.result


    def check_instance_health(self, instance):
        pmon_process_count = self.get_pmon_status(instance)
        print 'pmon_process_count: %s' % pmon_process_count
        if pmon_process_count == 1:
            status = 'OPEN'
        elif pmon_process_count == 0:
            status = 'CLOSED'
        else:
            status = 'N/A'
        instance.status = status
        print 'Instance Status: %s' % status
        self.db.commit()

    def run(self):
        while True:
            instances = self.db.query(SpOraInstance).all()
            for instance in instances:
                print "Start checking instance: %s" % instance.sid
                self.check_instance_health(instance)
            print "Sleep for 60sec..."
            time.sleep(60)


if __name__ == '__main__':
    checker = OraInstanceChecker()
    checker.run()
