"""
@Author: Vishal Patil
@Date: 16-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 16-02-2022 11:20:00
@Title : create app for Employee Payroll App
"""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI()


class Item(BaseModel):
    name: Optional[str] = None
    gender: Optional[str] = None
    department: Optional[str] = None
    salary: Optional[float] = None
    start_date: Optional[datetime] = None
    notes: Optional[str] = None


inventory = {}


@app.get("/")
def home():
    return {"Welcome in Employee Payroll App"}


@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item Id already exists "}
    inventory[item_id] = {"Name": item.name, "Gender": item.gender, "Department": item.department,
                          "Salary": item.salary, "Start_Date": item.start_date, "Notes": item.notes}
    return {f"User created with name as {item.name}"}



