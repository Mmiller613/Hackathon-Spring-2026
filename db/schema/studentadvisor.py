from sqlalchemy import Table, Column, Integer, ForeignKey
from db.server import Base

Studentadvisor = Table(
  'studentadvisor',
  Base.metadata,

  Column('StudentID', Integer, ForeignKey('student.StudentID')),
  Column('AdvisorID', Integer, ForeignKey('advisor.AdvisorID'))
)