__author__ = 'bova'

from wtforms import Form, TextField, SelectField, validators
from sprut.db.schema import SpServer
from sprut.db.conn import Session

db = Session()

class ServerForm(Form):
    hostname = TextField('Hostname', [validators.Required()])
    ip = TextField('IP', [validators.Required()])
    ora_user = TextField('ORA_User')
    ora_pass = TextField('ORA_Pass')

class InstanceForm(Form):
    servers = db.query(SpServer).all()
    choices = [(s.id, s.hostname) for s in servers]
    print "Choices: %s" % choices
    sid = TextField('SID', [validators.Required()])
    server_id = SelectField('Server ID', choices=choices, coerce=int)