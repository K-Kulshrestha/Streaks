from flask import Flask, render_template, request, url_for, redirect, session
import pymongo
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
app.secret_key = "testing"
client = pymongo.MongoClient("mongodb+srv://kshitijkuls6:WSjgz5wStXTzYAMF@cluster0.3tngdoy.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('Streaks')
collection = db.posts
records = db.users

@app.route("/", methods=['post', 'get'])
def index():
    message = ''
    if "email" in session:
        return redirect(url_for("logged_in"))
    if request.method == "POST":
        user = request.form.get("fullname")
        email = request.form.get("email")
        
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        user_found = records.find_one({"name": user})
        email_found = records.find_one({"email": email})
        if user_found:
            message = 'There already is a user by that name'
            return render_template('index.html', message=message)
        if email_found:
            message = 'This email already exists in database'
            return render_template('index.html', message=message)
        if password1 != password2:
            message = 'Passwords should match!'
            return render_template('index.html', message=message)
        else:
            hashed = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt())
            user_input = {'name': user, 'email': email, 'password': hashed}
            records.insert_one(user_input)
            
            user_data = records.find_one({"email": email})
            new_email = user_data['email']
   
            return render_template('logged_in.html', email=new_email)
    return render_template('index.html')

#end of code to run it
if __name__ == "__main__":
  app.run(debug=True)

@app.route('/logged_in')
def logged_in():
    if "email" in session:
        email = session["email"]
        posts = list(collection.find({}))
        for post in posts:
            post['_id'] = str(post['_id'])
        return render_template('logged_in.html', email=email, posts=posts)
    else:
        return redirect(url_for("login"))
    
@app.route("/login", methods=["POST", "GET"])
def login():
    message = 'Please login to your account'
    if "email" in session:
        return redirect(url_for("logged_in"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        email_found = records.find_one({"email": email})
        if email_found:
            email_val = email_found['email']
            passwordcheck = email_found['password']
            
            if bcrypt.checkpw(password.encode('utf-8'), passwordcheck):
                session["email"] = email_val
                return redirect(url_for('logged_in'))
            else:
                if "email" in session:
                    return redirect(url_for("logged_in"))
                message = 'Wrong password'
                return render_template('login.html', message=message)
        else:
            message = 'Email not found'
            return render_template('login.html', message=message)
    return render_template('login.html', message=message)

@app.route("/logout", methods=["POST", "GET"])
def logout():
    if "email" in session:
        session.pop("email", None)
        return redirect(url_for("index"))
    else:
        return render_template('index.html')
    
@app.route("/add", methods=["POST", "GET"])
def add():
    if "email" in session:
         email = session["email"]
         imageUrl = request.form.get("imageurl")
         caption = request.form.get("caption")
         task = request.form.get("task")
         user_input = {'userId': email, 'imageUrl' : imageUrl, 'caption' : caption , 'task' : task}
         collection.insert_one(user_input)
         return render_template("add.html")
    return render_template('add.html')
