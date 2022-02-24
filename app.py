from enum import unique
from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///demoProject.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Demo(db.Model):
    # sno = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(200),unique = True,primary_key=True)
    password = db.Column(db.String(200),nullable = False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self)->str:
        return f"{self.email}-{self.password}"


@app.route("/",methods=['GET','POST'])
def hello_world():
    allRegistered = Demo.query.all()
    print(allRegistered)
    #return render_template("index.html",allRegistered = allRegistered)
    if request.method == "POST":
        
        # sno = len(allRegistered)+1
        email = request.form['Email1']
        pwd = request.form['password']

        # for x in allRegistered:
        #     if email == x.email:
        #         return render_template("index.html",allRegistered = allRegistered,msg="Email already exists")
        #     else:
        try:
            demo = Demo(email = email,password=pwd)
            db.session.add(demo)
            db.session.commit()
            msg = 'Email registered successfully'
            return redirect('/login')
            return render_template("login.html",allRegistered = allRegistered,msg=msg)
        except exc.IntegrityError:
            db.session.rollback()
            msg = "Email already exists"
            return render_template("index.html",allRegistered = allRegistered,msg=msg)
    else:
        return render_template("index.html",allRegistered = allRegistered)
    
    # "<p>Welcome Page !</p>"

@app.route("/login",methods=['GET','POST'])
def login():
    allRegistered = Demo.query.all()
    print(allRegistered)
    
    if request.method == "POST":
        email = request.form['Email1']
        pwd = request.form['password']
        match = None
        for x in allRegistered:
            print((x.email))
            print((x.password))
            if x.email == email and x.password == pwd:
                return render_template("index.html",allRegistered = allRegistered,loggedIn=True)
                match = "Done"

            else:
                match = None
            # return render_template("login.html",allRegistered = allRegistered,loggedIn=False,msg='Wrong email/password combination')

            if match == None:
                return render_template("login.html",allRegistered = allRegistered,loggedIn=False,msg='Wrong email/password combination')
    else:
        return render_template("login.html",allRegistered = allRegistered,loggedIn=True)

@app.route("/logout",methods=['GET'])
def logout():
    allRegistered = Demo.query.all()
    return redirect('/')
    return render_template("index.html",allRegistered = allRegistered,loggedIn=False,msg='Logged Out')
if __name__ == "__main__":
    app.run(debug=True,port=8000)