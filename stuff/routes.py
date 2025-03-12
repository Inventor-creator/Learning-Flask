from niggas import app
from niggas import db
from sqlalchemy import text
from flask import render_template 
from flask import request



@app.route("/")
def student():

    #students and gpa 
    query = db.session.execute(text("SELECT studentName AS name , GPA from Student  , Students WHERE Student.studentId = Students.StudentId ORDER BY name ASC ;"))
    
    return render_template('hello.html' , query = query)



@app.route("/form" , methods = ['GET' , 'POST'])
def form():
    #checking username pass
    query = db.session.execute(text("SELECT username , password FROM userPass ORDER BY username;"))
    
    userpass = {}
    for i in query:
        userpass[i[0]] = i[1]
    
    print(userpass)
    
    if request.method == "GET":
        return render_template('form.html')
    elif request.method == "POST":
    
        username = request.form.get('username')
        password = request.form.get('password')

        try:
            if userpass[username] == password:
                return "user pass combo valid"
            else:
                return "user pass combo not valid"
        except:
            return "user pass combo not found"
        
        
        
    




