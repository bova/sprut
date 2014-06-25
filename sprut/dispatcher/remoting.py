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
        self.client.connect(self.server.hostname,
                       username=self.server.ora_user,
                       password=self.server.ora_pass)
        stdin, stdout, stderr = self.client.exec_command('. /home/oracle/%s.env;sqlplus / as sysdba<<EOF\n'
        '%s;\n'
        'EOF' % (self.instance.sid, self.command))

    def run(self):
        self.connect()

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
    rmt_cmd = RemoteCommand(instance)
    rmt_cmd.run()
    print "Finish"