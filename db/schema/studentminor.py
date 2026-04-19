from sqlalchemy import Table, Column, Integer, String, ForeignKey
from db.server import Base

Studentminor = Table(
  'studentminor',
  Base.metadata,

  Column('StudentID', String, ForeignKey('student.StudentID')),
  Column('MinorID', Integer, ForeignKey('minor.MinorID'))
)