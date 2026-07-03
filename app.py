from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, flash,session
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)
app.secret_key = "studentportal123"

# -----------------------------
# MongoDB Connection
# -----------------------------
client = MongoClient("mongodb+srv://lorditshis_db_user:StudentPortal23@cluster0.xla1byc.mongodb.net/?appName=Cluster0")

db = client["studentportal"]

students = db["students"]
users = db["users"]


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():

    total_students = students.count_documents({})

    total_branches = len(
        students.distinct("branch")
    )

    return render_template(
        "index.html",
        total_students=total_students,
        total_branches=total_branches
    )
# -------------------------------
# Register Page
# -------------------------------

@app.route("/register")
def register():

    return render_template("register.html")
# -------------------------------
# Save User
# -------------------------------

@app.route("/register-user", methods=["POST"])
def register_user():

    user = {

        "username": request.form["username"],

        "password": generate_password_hash(request.form["password"])

    }

    users.insert_one(user)

    flash("✅ Registration Successful!", "success")

    return redirect("/register")
# -------------------------------
# Students Page
# -------------------------------


# -------------------------------
# Login Page
# -------------------------------

@app.route("/login")
def login():

    return render_template("login.html")
# -------------------------------
# Login User
# -------------------------------

@app.route("/login-user", methods=["POST"])
def login_user():

    username = request.form["username"]

    password = request.form["password"]

    user = users.find_one({

        "username": username

    })
    if user and check_password_hash(user["password"], password):
        session["username"] = username

        flash("✅ Login Successful!", "success")

        return redirect("/")

    else:

        flash("❌ Invalid Username or Password!", "error")

        return redirect("/login")    
        

# -----------------------------
# Add Student Page
# -----------------------------
@app.route("/add-student")
def add_student():
    return render_template("add_student.html")


# -----------------------------
# Save Student
# -----------------------------
@app.route("/save-student", methods=["POST"])
def save_student():

    student = {
        "name": request.form["name"],
        "age": request.form["age"],
        "branch": request.form["branch"]
    }

    students.insert_one(student)

    flash("✅ Student added successfully!", "success")

    return redirect("/students")


# -----------------------------
# Students Page
# -----------------------------
# -----------------------------
# Students Page + Search
# -----------------------------
@app.route("/students")
def students_page():

    # Get the search text from the URL
    search = request.args.get("search", "")

    # If user typed something
    if search:

        all_students = students.find(
            {
                "name": {
                    "$regex": search,
                    "$options": "i"
                }
            }
        )

    # Otherwise show all students
    else:

        all_students = students.find()

    return render_template(
        "students.html",
        students=all_students,
        search=search
    )


# -----------------------------
# Edit Student Page
# -----------------------------
@app.route("/edit-student/<student_id>")
def edit_student(student_id):

    student = students.find_one(
        {"_id": ObjectId(student_id)}
    )

    return render_template(
        "edit_student.html",
        student=student
    )


# -----------------------------
# Update Student
# -----------------------------
@app.route("/update-student/<student_id>", methods=["POST"])
def update_student(student_id):

    students.update_one(

        {"_id": ObjectId(student_id)},

        {
            "$set": {
                "name": request.form["name"],
                "age": request.form["age"],
                "branch": request.form["branch"]
            }
        }

    )

    flash("✏️ Student updated successfully!", "success")

    return redirect("/students")


# -----------------------------
# Delete Student
# -----------------------------
@app.route("/delete-student/<student_id>")
def delete_student(student_id):

    students.delete_one(
        {
            "_id": ObjectId(student_id)
        }
    )

    flash("🗑 Student deleted successfully!", "success")

    return redirect("/students")
@app.route("/logout")
def logout():

    session.pop("username", None)

    flash("Logged Out Successfully")

    return redirect("/login")


# -----------------------------
# Run Flask App
# -----------------------------


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
   
   
   
   
   