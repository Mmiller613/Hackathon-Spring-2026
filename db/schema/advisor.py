from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.server import Base
from db.schema.studentadvisor import Studentadvisor
from db.schema.advisorcourse import Advisorcourse

class Advisor(Base):
    __tablename__ = 'advisor'
    AdvisorID = Column(Integer,primary_key=True,autoincrement=True)
    FName = Column(String(40))
    LName = Column(String(40))
    Email = Column(String(40))

    Student = relationship('Student', secondary = Studentadvisor, back_populates = 'Advisor')
    Course = relationship('Course', secondary = Advisorcourse, back_populates = 'Advisor')

    def __repr__(self):
        return f"""
            "FIRST NAME: {self.FName},
             LAST NAME: {self.LName},
             Email: {self.Email}
        """
    
    def __repr__(self):
        return self.__repr__()