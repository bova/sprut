__author__ = 'bova'


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sprut.conf import SprutConfig
from sqlalchemy import event

# Workaround for SQLite default behavior with ForeignKey CASCADE deletion
def on_connect(conn, record):
    conn.execute('pragma foreign_keys=ON')

conf = SprutConfig()

db_conn_string = 'sqlite:///%s' % conf.db.path

# Set echo=True for DEBUG db interactions
engine = create_engine(db_conn_string, echo=True)
event.listen(engine, 'connect', on_connect)

Session = sessionmaker(engine)


if __name__ == '__main__':
    print engine
    engine.execute("select 1 from dual").scalar()
    session = Session()
    print session