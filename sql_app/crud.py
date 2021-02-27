from sqlalchemy.orm import Session
import json
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from . import models, schemas

###Define the get_detroit function for returning all of the data
def get_detroit(db: Session):
    ###Query the data from the database
    lists = db.query(models.Detroit).all()
    ###Convert the data to a jsonable list
    data = jsonable_encoder(lists)
    ###return the response to the end user
    return JSONResponse(content=data)


###Define the get_student function for returning all of the data
def get_student(db: Session):
    ###Query the data from the database
    lists = db.query(models.Student).all()
    ###Convert the data to a jsonable list
    data = jsonable_encoder(lists)
    ###return the response to the end user
    return JSONResponse(content=data)

