__author__ = 'bova'

from sqlalchemy import Column, Sequence, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class SpServer(Base):
    __tablename__ = 'sp_server'
    id = Column(Integer, Sequence('sp_server_id_seq'), primary_key=True)
    hostname = Column(String(256))
    ip = Column(String(50))
    ora_user = Column(String(128))
    ora_pass = Column(String(128))
    instances = relationship('SpOraInstance')


class SpOraInstance(Base):
    __tablename__ = 'sp_ora_instance'
    id = Column(Integer, Sequence('sp_ora_instance_id_seq'), primary_key=True)
    sid = Column(String(50))
    server_id = Column(Integer, ForeignKey('sp_server.id', ondelete='CASCADE'))


    def __init__(self, sid):
        self.sid = sid

    def __repr__(self):
        pass