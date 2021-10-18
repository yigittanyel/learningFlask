from flask import Flask,url_for,redirect

app=Flask(__name__)

@app.route("/")
def index():
    return "Main Page"


@app.route("/admin")
def hello_admin():
    return "Hello Admin"

@app.route("/guest/<guest>")
def hello_guest(guest):
    return "Hello %s guest" %guest

@app.route("/user/<user>")
def hello_user(user):
    if user=='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=user))
        
if __name__=='__main__':
    app.run(debug=True)
