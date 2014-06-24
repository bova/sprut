__author__ = 'bova'


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sprut.conf import SprutConfig

conf = SprutConfig()

db_conn_string = 'sqlite:///%s' % conf.db.path

# Set echo=True for DEBUG db interactions
engine = create_engine(db_conn_string, echo=False)
Session = sessionmaker(engine)


if __name__ == '__main__':
    print engine
    engine.execute("select 1 from dual").scalar()
    session = Session()
    print session