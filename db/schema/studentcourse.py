from sqlalchemy import Table, Column, Integer, String, ForeignKey
from db.server import Base

Studentcourse = Table(
  'studentcourse',
  Base.metadata,

  Column('StudentID', String, ForeignKey('student.StudentID')),
  Column('CourseID', Integer, ForeignKey('course.CourseID'))
)