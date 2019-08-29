# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker, scoped_session
from howarddb.howard_db import engine

session_factory = sessionmaker(bind=engine)
ScopedSession = scoped_session(session_factory)


