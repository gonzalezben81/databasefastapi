###Import the necessary libraries to create the schemas
from typing import List, Optional

from pydantic import BaseModel

###Create the schema for the detroit table
class DetroitBase(BaseModel):
    Year:   int
    FTP:    int
    UEMP:   int
    MAN:    int
    LIC:    int
    GR:     int
    CLEAR:  int
    WM:     int
    NMAN:   int
    GOV:    int
    HE:     int
    WE:     int
    HOM:    int
    ACC:    int
    ASR:    int

class Config:
    orm_mode = True


class Detroit(DetroitBase):
    Year:   int
    FTP:    int
    UEMP:   int
    MAN:    int
    LIC:    int
    GR:     int
    CLEAR:  int
    WM:     int
    NMAN:   int
    GOV:    int
    HE:     int
    WE:     int
    HOM:    int
    ACC:    int
    ASR:    int

class Config:
    orm_mode = True
    
###Create the schema for the studen table
class StudentBase(BaseModel):

    school: str
    sex:    str
    age:    int
    address:    str
    famsize:    str
    Pstatus:    str
    Medu:   float
    Fedu:   float
    Mjob:   str
    Fjob:   str
    reason: str
    guardian:   str
    traveltime: int
    studytime:  int
    failures:   int
    schoolsup:  str
    famsup:     str
    paid:       str
    activities: str
    nursery:    str
    higher:     str
    internet:   str
    romantic:   str
    famrel:     int
    freetime:   int
    goout:      int
    Dalc:       int
    Walc:       int
    health:     int
    absences:   int
    G1:     int
    G2:     int
    G3:     int

class Config:
    orm_mode = True
    

class Student(StudentBase):

    school: str
    sex:    str
    age:    int
    address:    str
    famsize:    str
    Pstatus:    str
    Medu:   float
    Fedu:   float
    Mjob:   str
    Fjob:   str
    reason: str
    guardian:   str
    traveltime: int
    studytime:  int
    failures:   int
    schoolsup:  str
    famsup:     str
    paid:       str
    activities: str
    nursery:    str
    higher:     str
    internet:   str
    romantic:   str
    famrel:     int
    freetime:   int
    goout:      int
    Dalc:       int
    Walc:       int
    health:     int
    absences:   int
    G1:     int
    G2:     int
    G3:     int

class Config:
    orm_mode = True
