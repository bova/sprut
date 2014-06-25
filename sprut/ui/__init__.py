__author__ = 'bova'

from flask import Flask, request, redirect, url_for, render_template
import flask.ext.restless

from sprut.db.schema import SpServer, SpOraInstance
from sprut.db.conn import Session
from form import ServerForm, InstanceForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'jopa'
db = Session()

api_manager = flask.ext.restless.APIManager(app, db)
api_manager.create_api(SpServer, methods=['GET', 'POST', 'DELETE', 'PUT', 'PATCH'])
api_manager.create_api(SpOraInstance, methods=['GET', 'POST', 'DELETE', 'PUT', 'PATCH'])

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/server/add', methods=['GET', 'POST'])
def add_server():
    form = ServerForm(request.form)
    if request.method == 'POST' and form.validate():
        server = SpServer(form.hostname.data, form.ip.data, form.ora_user.data, form.ora_pass.data)
        db.add(server)
        db.commit()
        return redirect(url_for('index'))
    else:
        return render_template('/server/add.html', form=form)

# @app.route('/instance', methods=['GET'])
# def instance():
#     pass

@app.route('/instance/add', methods=['GET', 'POST'])
def add_instance():
    form = InstanceForm(request.form)
    if request.method == 'POST' and form.validate():
        instance = SpOraInstance(form.sid.data, form.server_id.data)
        db.add(instance)
        db.commit()
        return redirect('/#/instance')
    else:
        return render_template('/instance/add.html', form=form)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
