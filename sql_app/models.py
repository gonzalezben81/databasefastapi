###Import the correct python libraries
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class Detroit(Base):
    __tablename__ = "detroit"
    ###Primary Key is required for the table to populate
    Year = Column(Integer, primary_key=True, index=True)
    FTP = Column(Integer)
    UEMP = Column(Integer)
    MAN = Column(Integer)
    LIC = Column(Integer)
    GR = Column(Integer)
    CLEAR = Column(Integer)
    WM = Column(Integer)
    NMAN = Column(Integer)
    GOV = Column(Integer)
    HE = Column(Integer)
    WE = Column(Integer)
    HOM = Column(Integer)


class Student(Base):
    __tablename__ = "student"
    """###Primary Key is required for the table to populate"""
    """###Set the Column(Type) to what is in your database e.g. Integer, String, etc."""
    school = Column(String)
    sex = Column(String)
    age = Column(Integer, primary_key=True, index=True)
    address = Column(String)
    famsize = Column(String)
    Pstatus = Column(String)
    Medu = Column(Integer)
    Fedu = Column(Integer)
    Mjob = Column(String)
    Fjob = Column(String)
    reason = Column(String)
    guardian = Column(String)
    traveltime = Column(Integer)
    studytime = Column(Integer)
    failures = Column(Integer)
    schoolsup = Column(String)
    famsup = Column(String)
    paid = Column(String)
    activities = Column(String)
    nursery = Column(String)
    higher = Column(String)
    internet = Column(String)
    romantic = Column(String)
    famrel = Column(Integer)
    freetime = Column(Integer)
    goout = Column(Integer)
    Dalc = Column(Integer)
    Walc = Column(Integer)
    health = Column(Integer)
    absences = Column(Integer)
    G1 = Column(Integer)
    G2 = Column(Integer)
    G3 = Column(Integer)
    
