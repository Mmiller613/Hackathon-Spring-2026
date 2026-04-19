from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.server import Base
from db.schema.studentminor import Studentminor


class Minor(Base):
    __tablename__ = 'minor'
    MinorID = Column(Integer,primary_key=True,autoincrement=True)
    MinorName = Column(String(40))

    Student = relationship('Student', secondary = Studentminor, back_populates = 'Advisor')

    def __repr__(self):
        return f"""
            MinorName: {self.MinorName}
        """
    
    def __repr__(self):
        return self.__repr__()