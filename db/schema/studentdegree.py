from sqlalchemy import Table, Column, Integer, String, ForeignKey
from db.server import Base

Studentdegree = Table(
  'studentdegree',
  Base.metadata,

  Column('StudentID', String, ForeignKey('student.StudentID')),
  Column('DegreeID', Integer, ForeignKey('degree.DegreeID'))
)