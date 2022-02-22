"""
@Author: Vishal Patil
@Date: 16-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 22-02-2022 15:30:00
@Title : create app for Employee Payroll App
"""

from datetime import date
from typing import Optional
from fastapi import HTTPException
from pydantic import BaseModel, validator


class User(BaseModel):
    """
    desc: for creating pydentic schema
    """
    name: Optional[str] = None
    gender: Optional[str] = None
    department: Optional[str] = None
    salary: Optional[float] = None
    start_date: Optional[date] = None
    notes: Optional[str] = None

    @validator("gender")
    @classmethod
    def gender_valid(cls, gender):
        """
        Description: checking validation of gender
        :type gender: Gender input for checking
        Return: gender object or http exception
        """
        char = ["Male", "Female", "male", "female"]
        if gender in char:
            return gender
        raise HTTPException(status_code=422, detail="Enter valid gender")

    @validator("department")
    @classmethod
    def department_valid(cls, department):
        """
        Description: checking validation of department
        :type department: department input for checking
        Return: department object or http exception
        """
        char = ["HR", "Sales", "Finance", "Engineer", "Others"]
        if department in char:
            return department
        raise HTTPException(status_code=422, detail="Enter valid Department")
