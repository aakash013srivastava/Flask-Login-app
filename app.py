from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Welcome Page !</p>"

@app.route("/register")
def register():
    return "<p>Register Page !</p>"

@app.route("/login")
def login():
    return "<p>Login Page !</p>"

if __name__ == "__main__":
    app.run(debug=True,port=8000)