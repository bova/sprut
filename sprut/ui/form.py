__author__ = 'bova'

from wtforms import Form, TextField, validators


class ServerForm(Form):
    hostname = TextField('Hostname', [validators.Required()])
    ip = TextField('IP', [validators.Required()])
    ora_user = TextField('ORA_User')
    ora_pass = TextField('ORA_Pass')