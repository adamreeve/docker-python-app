from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from hello import config


engine = create_engine(config.DB_CONNECTION, convert_unicode=True)
ScopedSession = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

# Base class for declarative ORM models
Base = declarative_base()
Base.query = ScopedSession.query_property()
