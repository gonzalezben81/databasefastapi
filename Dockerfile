###Get the Python 3.7 Docker Image
FROM python:3.7

###Install the necessary Python 3.7 libraries
RUN pip install fastapi uvicorn numpy sqlalchemy psycopg2

###Expost port 80880
EXPOSE 8080

###Copy everything from the sql_app folder and place in on the server
COPY ./sql_app /sql_app

###Start up FastAPI utilizing uvicorn and run it on port 8080
CMD ["uvicorn", "sql_app.main:app", "--host", "0.0.0.0", "--port", "8080"]