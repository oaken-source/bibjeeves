
'''
This module contains the batabase models used by bibjeeves.
'''

from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class BaseModel(declarative_base()):
    '''
    the base model - to be extended by the models
    '''
    __abstract__ = True


class Citation(BaseModel):
    '''
    association table for documents
    '''
    __tablename__ = 'citations'

    citer = Column(Integer, ForeignKey('documents.id'), primary_key=True)
    citee = Column(Integer, ForeignKey('documents.id'), primary_key=True)


class Document(BaseModel):
    '''
    representations of documents in the database
    '''
    __tablename__ = 'documents'

    document_id = Column(Integer, primary_key=True)
    title = Column(String(256))
    abstract = Column(Text)

    citees = relationship(
        "Association",
        backref='citers',
        primaryjoin=(document_id == Citation.citer)
    )

