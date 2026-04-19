from sqlalchemy import Table, Column, Integer, String, ForeignKey
from db.server import Base

Advisorcourse = Table(
  'advisorcourse',
  Base.metadata,

  Column('AdvisorID', String, ForeignKey('advisor.AdvisorID')),
  Column('CourseID', Integer, ForeignKey('course.CourseID'))
)