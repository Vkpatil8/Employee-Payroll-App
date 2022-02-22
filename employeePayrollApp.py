"""
@Author: Vishal Patil
@Date: 16-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 22-02-2022 15:30:00
@Title : create app for Employee Payroll App
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import model
from database import engine, SessionLocal
from schema import User

fake_users_db = {
    "vishal": {
        "username": "vishal",
        "password": "Vkpatil8@"
    }
}
model.Base.metadata.create_all(engine)


def get_db():
    """
    desc: get database
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
        Description: checking validation of gender
        :param form_data: get data from request form
        Return: sting (accesses token name & token type)
    """
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user_dict1 = fake_users_db.get(form_data.password)
    if not user_dict1:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user_dict, "token_type": "bearer"}


@app.get("/")
def home():
    """
    Description: Showing Welcome msg
    Return: Welcome msg
    """
    return {"Welcome in Employee Payroll App"}


@app.get("/dashboard")
def all_users(db: Session = Depends(get_db)):
    """
    Description: Showing Users data
    Return: Dictionary
    """

    blogs = db.query(model.User).all()
    return blogs


@app.post("/create-user/{user_id}")
def create_user(user_id: int, user: User, auth: User = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Description: Creating user according to give data
    :param db:
    :param auth: for authentication
    :param user: creating object of user
    :type user_id: giving user id
    Return: string
    """
    new_user = model.User(id=user_id, name=user.name, gender=user.gender, department=user.department,
                          salary=user.salary, start_date=user.start_date, notes=user.notes)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {f"User created with name as {user.name}"}


@app.delete('/delete/{user_id}')
def delete(user_id: int, auth: User = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    :param auth: for authentication
    :param user_id:
    :param db: get data from database
    :return: string
    """
    user = db.query(model.User).filter(model.User.id == user_id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {user_id} not found")

    user.delete(synchronize_session=False)
    db.commit()
    return {"delete successfully"}


@app.put('/update/{user_id}', status_code=status.HTTP_202_ACCEPTED)
def update(user_id: int, user1: User, auth: User = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    :param user_id: get user id
    :param user1: create users object
    :param auth: for authentication
    :param db: data base connection
    :return: string
    """
    user = db.query(model.User).filter(model.User.id == user_id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {user_id} not found")
    if user1.name is not None:
        user.update({"name": user1.name})
    if user1.gender is not None:
        user.update({"gender": user1.gender})
    if user1.department is not None:
        user.update({"department": user1.department})
    if user1.salary is not None:
        user.update({"salary": user1.salary})
    if user1.start_date is not None:
        user.update({"start_date": user1.start_date})
    if user1.notes is not None:
        user.update({"notes": user1.notes})
    db.commit()
    return {f"User update with id as {user_id}"}
