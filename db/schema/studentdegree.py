from sqlalchemy import Table, Column, Integer, ForeignKey
from db.server import Base

Studentdegree = Table(
  'studentdegree',
  Base.metadata,

  Column('StudentID', Integer, ForeignKey('student.StudentID')),
  Column('DegreeID', Integer, ForeignKey('degree.DegreeID'))
)