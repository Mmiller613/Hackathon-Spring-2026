from sqlalchemy import Table, Column, Integer, ForeignKey
from db.server import Base

Studentminor = Table(
  'studentminor',
  Base.metadata,

  Column('StudentID', Integer, ForeignKey('student.StudentID')),
  Column('MinorID', Integer, ForeignKey('minor.MinorID'))
)