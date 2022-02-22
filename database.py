"""
@Author: Vishal Patil
@Date: 16-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 22-02-2022 15:30:00
@Title : create app for Employee Payroll App
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:root@localhost:3306/employee_info"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
