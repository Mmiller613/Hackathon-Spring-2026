from sqlalchemy import Table, Column, Integer, String, ForeignKey
from db.server import Base

Studentadvisor = Table(
  'studentadvisor',
  Base.metadata,

  Column('StudentID', String, ForeignKey('student.StudentID')),
  Column('AdvisorID', String, ForeignKey('advisor.AdvisorID'))
)