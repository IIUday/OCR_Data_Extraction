from sqlalchemy import create_engine, Column, Integer, String, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    dob = Column(String)

class FormData(Base):
    __tablename__ = 'forms_data'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    form_json = Column(JSON)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

def connect_db(db_url):
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    return engine, session

def create_tables(engine):
    Base.metadata.create_all(engine)

def insert_data(session, data):
    patient = Patient(name=data.get("patient_name"), dob=data.get("dob"))
    session.add(patient)
    session.commit()
    form_data = FormData(patient_id=patient.id, form_json=data)
    session.add(form_data)
    session.commit()
