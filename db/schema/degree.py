from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.server import Base
from db.schema.studentdegree import Studentdegree


class Degree(Base):
    __tablename__ = 'degree'
    DegreeID = Column(Integer,primary_key=True,autoincrement=True)
    DegreeName = Column(String(40))

    Student = relationship('Student', secondary = Studentdegree, back_populates = 'Degree')

    def __repr__(self):
        return f"""
            "FIRST NAME: {self.DegreeName}
        """
    
    def __repr__(self):
        return self.__repr__()