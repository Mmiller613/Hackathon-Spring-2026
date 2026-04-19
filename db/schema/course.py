from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.server import Base
from db.schema.studentcourse import Studentcourse
from db.schema.advisorcourse import Advisorcourse


class Course(Base):
    __tablename__ = 'course'
    CourseID = Column(Integer,primary_key=True,autoincrement=True)
    CourseName = Column(String(40))
    CreditHours = Column(Integer)

    Student = relationship('Student', secondary = Studentcourse, back_populates = 'Course')
    Advisor = relationship('Advisor', secondary = Advisorcourse, back_populates = 'Course')

    def __repr__(self):
        return f"""
            "COURSE NAME: {self.CourseName},
             CREDIT HOURS: {self.CreditHours}
        """
    
    def __repr__(self):
        return self.__repr__()