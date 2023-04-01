from flask import Flask, render_template, request
import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="flask"
)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    course = request.form['course']
    semester = request.form['semester']
    feedback = request.form['feedback']

    # Insert the feedback into the MySQL database
    cursor = db.cursor()
    sql = "INSERT INTO demo (name, email, course, semester, feedback) VALUES (%s, %s, %s, %s, %s)"
    val = (name, email, course, semester, feedback)
    cursor.execute(sql, val)
    db.commit()

    return render_template('submit.html', name=name, email=email, course=course, semester=semester, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
