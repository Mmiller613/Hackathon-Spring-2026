from sqlalchemy import Table, Column, Integer, ForeignKey
from db.server import Base

Studentcourse = Table(
  'studentcourse',
  Base.metadata,

  Column('StudentID', Integer, ForeignKey('student.StudentID')),
  Column('CourseID', Integer, ForeignKey('course.CourseID'))
)