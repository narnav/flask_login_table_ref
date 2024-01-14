import json
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class Car(db.Model):
    id = db.Column('car_id', db.Integer, primary_key = True)
    model = db.Column(db.Integer)
    student_id = db.Column(db.Integer, db.ForeignKey("student.student_id"))
    def __init__(self, model,student_id=-1):
        self.student_id=student_id
        self.model=model

class Student(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))
    # cars=db.relationship("Car",backref="Student")
    cars = db.relationship("Car", backref=db.backref("Student", lazy=True))
    def __init__(self, name, city, addr,pin=0):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

@app.route('/')
def show_all():
    res=[]
    for student in Student.query.all():
        res.append({"addr":student.addr,"city":student.city,"id":student.id,"name":student.name,"pin":student.pin})
    return  (json.dumps(res))

@app.route('/get_student')
def show_student():
    res=[]
    stu= Student.query.filter_by(id=2).first()
    print( stu.cars[0].model)
    for car in stu.cars:
        res.append({"model":car.model})
    return  (json.dumps(res))

@app.route('/new_student', methods = ['GET', 'POST'])
def new_student():
    
    request_data = request.get_json()
    print("--------------------------------------------------------------------------------")
    # print(request_data['city'])
    city = request_data['city']
    name= request_data["name"]
    addr= request_data["addr"]
    pin= request_data["pin"]
 
    newStudent= Student(name,city,addr,pin)
    db.session.add (newStudent)
    db.session.commit()
    return "a new rcord was create"

@app.route('/new_car', methods = ['GET', 'POST'])
def new_car():
    # getting data from user (axios...)
    request_data = request.get_json()
    model = request_data['model']
    student_id = request_data['student_id']
    # create a new car
    newCar= Car(model=model, student_id=student_id)
    # add the new car tomy DB
    db.session.add (newCar)
    db.session.commit()
    return "a new car was create"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
