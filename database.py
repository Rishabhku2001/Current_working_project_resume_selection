from sqlalchemy import create_engine, text
from sqlalchemy.engine.result import FilterResult
import pandas as pd
import csv
import os

# Replace 'your_username', 'your_password', 'your_host' and 'your_database' with your PostgreSQL credentials
db_username = 'rishabh_career_user'
db_password = 'Rcpc9xzQ8MHNvanYaGh6UjDS0IqwIWz4'
db_host = 'singapore-postgres.render.com'
db_name = 'rishabh_career'

# Create a connection string
connection_string = f'postgresql+psycopg2://{db_username}:{db_password}@{db_host}/{db_name}'

# Create an SQLAlchemy engine
engine = create_engine(connection_string)

def upload_csv_file_to_database():
    df = pd.read_csv(r'C:/Users/risha/Desktop/Project1/static/resume_data.csv',encoding="ISO-8859-1")
    table_name = 'resume'
    df.to_sql(table_name, engine, index=False, if_exists='replace')


def load_resume_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from resume"))

    resume = []
    for row in result.all():
      resume.append(row._asdict())

    return resume
  
def add_to_DB(data):
    with engine.connect() as conn:
        resume_id = data.get('resume_id')
        classs = data.get('class')
        resume_text = data.get('resume_text')
        query = text(
        f"INSERT INTO resume (resume_id, class,resume_text) VALUES ('{resume_id}', '{classs}' ,'{resume_text}')")
        print(query)
        conn.execute(query)
        conn.commit()
     

