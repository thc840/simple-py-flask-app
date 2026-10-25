from flask import Flask, render_template

app = Flask(__name__)

# Mock student data dictionary
STUDENTS = [
    {"id": 101, "name": "Shyam", "dept": "Computer Science", "gpa": 7.8},
    {"id": 102, "name": "Ram", "dept": "Data Science", "gpa": 8.5},
    {"id": 103, "name": "Pradip", "dept": "Mechanical Engineering", "gpa": 7.9},
    {"id": 104, "name": "Rekha", "dept": "Cybersecurity", "gpa": 9.7},
]


@app.route("/")
def home():
    return render_template("index.html", student_list=STUDENTS)


if __name__ == "__main__":
    app.run()
