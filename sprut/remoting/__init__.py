__author__ = 'bova'

import paramiko


class RemoteCommand(object):
    def __init__(self, instance):
        self.instance = instance
        self.server = instance.server
        self.command = instance.command
        self.init()

    def init(self):
        self.client = paramiko.client.SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())

    def connect(self):
        self.client.connect(self.server.ip,
                       username=self.server.ora_user,
                       password=self.server.ora_pass)

    def execute(self):
        print 'Instance.sid: %s' % self.instance.sid
        print 'Command: %s' % self.command
        self.cmd = ('. /home/oracle/%s.env;sqlplus / as sysdba<<EOF\n'
        '%s;\n'
        'EOF' % (self.instance.sid, self.command))
        print self.cmd
        stdin, stdout, stderr = self.client.exec_command(self.cmd)

    def run(self):
        self.connect()
        self.execute()


class OraStatusCommand(RemoteCommand):
    def __init__(self, instance):
        self.result = ''
        super(OraStatusCommand, self).__init__(instance)

    def execute(self):
        self.cmd = 'ps -ef|grep pmon_%s|grep -v grep|wc -l' % self.instance.sid
        stdin, stdout, stderr = self.client.exec_command(self.cmd)
        pmon_process_count = int(stdout.readlines()[0].lstrip('\n'))
        self.result = pmon_process_count

if __name__ == '__main__':
    class Server(object):
        hostname = 'xe-test.fido.uz'
        ora_user = 'oracle'
        ora_pass = 'oracle11g'

    class Instance(object):
        sid = 'xe'
        server = ''
        command = ''

    command1 = 'SHUTDOWN IMMEDIATE'
    command2 = 'STARTUP'
    server = Server()
    instance = Instance()
    instance.server = server
    instance.command = command1

    print "Start"
    rmt_cmd = OraStatusCommand(instance)
    rmt_cmd.run()
    print rmt_cmd.result
    print "Finish"