from flask import Flask, render_template, request
from database import upload_csv_file_to_database,load_resume_from_db,add_to_DB
from resume_sel import make_png_file

app = Flask(__name__)


@app.route("/")
def hello_world():
  upload_csv_file_to_database()
  resume=load_resume_from_db()
  print("I am here")
  make_png_file()
  print("This also done")
  
  l=len(resume);
  return render_template('home.html',resume=resume,l=l)


@app.route("/apply", methods=['post'])
def apply_to_submitted():
  print("/applyy")
  data = request.form
  add_to_DB(data)
  print("here i am")
  make_png_file(data)
  return render_template('resume_submitted.html',
                         data=data)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)