"""
@Author: Vishal Patil
@Date: 16-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 16-02-2022 11:30:00
@Title : create app for Employee Payroll App
"""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI()


class User(BaseModel):
    name: Optional[str] = None
    gender: Optional[str] = None
    department: Optional[str] = None
    salary: Optional[float] = None
    start_date: Optional[datetime] = None
    notes: Optional[str] = None


inventory = {}


@app.get("/")
def home():
    """"
    Description: Showing Welcome msg
    Return: Welcome msg
    """
    return {"Welcome in Employee Payroll App"}


@app.post("/create-user/{user_id}")
def create_user(user_id: int, user: User):
    """"
    Description: Creating user according to give data
    :param user: creating object of user
    :type user_id: giving user id
    Return: string
    """
    if user_id in inventory:
        return {"Error": "Item Id already exists "}
    inventory[user_id] = {"Name": user.name, "Gender": user.gender, "Department": user.department,
                          "Salary": user.salary, "Start_Date": user.start_date, "Notes": user.notes}
    return {f"User created with name as {user.name}"}


@app.get("/dashboard")
def dashboard():
    """"
    Description: Showing Users data
    Return: Dictionary
    """
    return inventory


@app.put("/update-item/{user_id}")
def update_user(user_id: int, user: User):
    """"
    Description: Updating user data
    :param user: accessing object of user
    :type user_id: giving user id 
    Return: string
    """
    if user_id not in inventory:
        return {"Error": "Not Found"}
    if user.name is not None:
        inventory[user_id]["Name"] = user.name
    if user.gender is not None:
        inventory[user_id]["Gender"] = user.gender
    if user.department is not None:
        inventory[user_id]["Department"] = user.department
    if user.salary is not None:
        inventory[user_id]["Salary"] = user.salary
    if user.start_date is not None:
        inventory[user_id]["Start_Date"] = user.start_date
    if user.notes is not None:
        inventory[user_id]["Notes"] = user.notes

    return {f"User update with name as {user.name}"}
