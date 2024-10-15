from flask import Flask, render_template, request, redirect
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pyproject"]
collection = db["students"]

@app.route('/')
def index():
    students = collection.find()
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    age = request.form['age']
    course = request.form['course']
    collection.insert_one({"name": name, "age": int(age), "course": course})
    return redirect('/')

@app.route('/delete/<name>')
def delete_student(name):
    collection.delete_one({"name": name})
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
