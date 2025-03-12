
from niggas import db

class Students(db.Model):
    __tablename__ = 'Students'
    StudentId = db.Column(db.Integer , primary_key = True)
    studentName  = db.Column(db.String(length = 20))

class Student(db.Model):
    __tablename__ = 'Student'
    studentId = db.Column(db.Integer,db.ForeignKey('Students.StudentId'), primary_key = True, autoincrement = True )
    GPA = db.Column(db.Integer)
    CourseId = db.Column(db.Integer)

class userPass(db.Model):
    __tablename__ = "userPass"
    username = db.Column(db.String(length = 20) , primary_key = True)
    password = db.Column(db.String(length = 20))



