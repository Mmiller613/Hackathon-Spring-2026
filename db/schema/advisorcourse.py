from sqlalchemy import Table, Column, Integer, ForeignKey
from db.server import Base

Advisorcourse = Table(
  'advisorcourse',
  Base.metadata,

  Column('AdvisorID', Integer, ForeignKey('advisor.AdvisorID')),
  Column('CourseID', Integer, ForeignKey('course.CourseID'))
)