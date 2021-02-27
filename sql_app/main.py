from typing import List
from fastapi import Depends, FastAPI, HTTPException, Response
from sqlalchemy.orm import Session
###Import the crud, models, and schemas python files
from . import crud, models, schemas
from .database import SessionLocal, engine
###Import HTMLResponse to allow HTML Responses from the API
from fastapi.responses import HTMLResponse

models.Base.metadata.create_all(bind=engine)

###Create an object called app to use with the endpoints
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


###Create an endpoint called detroit that returns the detroit table
@app.get("/detroit/", response_model=List[schemas.Detroit])
def read_Detroit(db: Session = Depends(get_db)):
    users = crud.get_detroit(db)
    return users


###Create an endpoint called student that returns the student table
@app.get("/student/", response_model=List[schemas.Student])
def read_student(db: Session = Depends(get_db)):
    items = crud.get_student(db)
    return items

    
###Create an endpoint called items that returns an HTML response
@app.get("/items/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """

###Create an endpoint called legacy that returns an XML response    
@app.get("/legacy/")
def get_legacy_data():
    data = """<?xml version="1.0"?>
    <shampoo>
    <Header>
        Apply shampoo here.
    </Header>
    <Body>
        You'll have to use soap here.
    </Body>
    </shampoo>
    """
    return Response(content=data, media_type="application/xml")
