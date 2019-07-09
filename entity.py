from sqlalchemy import Column, String, BigInteger, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class File(Base):
    __tablename__ = 'file'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    path = Column(String(200))
    folder = Column(String(100))
    name = Column(String(50))
    extension = Column(String(20))
    size = Column(BigInteger)
    created_at = Column(String(14))
    modified_at = Column(String(14))


