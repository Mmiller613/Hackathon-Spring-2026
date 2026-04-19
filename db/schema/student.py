from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from db.server import Base
from db.schema.studentadvisor import Studentadvisor
from db.schema.studentcourse import Studentcourse
from db.schema.studentdegree import Studentdegree
from db.schema.studentminor import Studentminor

class Student(Base):
    __tablename__ = 'student'
    StudentID = Column(Integer,primary_key=True,autoincrement=True)
    FName = Column(String(40))
    LName = Column(String(40))
    Email = Column(String(40))
    PWord = Column(String(100))
    Email = Column(String(40))
    Gender = Column(String(10))
    DOB = Column(String(20))
    GPA = Column (Numeric(1,3))
    Level = Column (String(20))

    Advisor = relationship('Advisor', secondary = Studentadvisor, back_populates = 'Student')
    Course = relationship ('Course', secondary = Studentcourse, back_populates = 'Student')
    Degree = relationship ('Degree', secondary = Studentdegree, back_populates = 'Student')
    Minor = relationship ('Minor', secondary = Studentminor, back_populates = 'Student')

    def __repr__(self):
        return f"""
            "FIRST NAME: {self.FName},
             LAST NAME: {self.LName},
             PASSWORD: {self.PWord},
             EMAIL: {self.Email},
             Gender: {self.Gender},
             DOB: {self.DOB},
             GPA: {self.GPA},
             LEVEL: {self.Level}
        """
    
    def __repr__(self):
        return self.__repr__()