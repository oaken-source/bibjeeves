
'''
This module contains the batabase models used by bibjeeves.
'''

from sqlalchemy import Table, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


BaseModel = declarative_base()


class Citation(BaseModel):

    __tablename__ = 'citations'

    citer = Column(Integer, ForeignKey('documents.id'), primary_key=True)
    citee = Column(Integer, ForeignKey('documents.id'), primary_key=True)


class Document(BaseModel):

    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True)
    title = Column(String(256))
    abstract = Column(Text)

    citees = relationship("Association", backref='citers', primaryjoin=id==Citation.citer)

