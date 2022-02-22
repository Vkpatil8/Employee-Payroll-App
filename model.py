"""
@Author: Vishal Patil
@Date: 16-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 22-02-2022 15:30:00
@Title : create app for Employee Payroll App
"""

from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text, Date
from database import Base


class User(Base):
    """
    desc: for creating table in data base
    """
    __tablename__ = "User_info"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    gender = Column(String(20))
    department = Column(String(20))
    salary = Column(Integer())
    start_date = Column(Date())
    notes = Column(Text())
