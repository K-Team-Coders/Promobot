from sqlalchemy import Column, Integer, Text, DateTime

from .sqlalchemy import bbase

class MessagesModel(bbase):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    message = Column(Text)
    organisation = Column(Text)
    theme = Column(Text)
    group = Column(Text)
    date = Column(DateTime)
    ner = Column(Text)
    coords = Column(Text)