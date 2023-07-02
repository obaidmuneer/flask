from flask import Flask , render_template , url_for , jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
import gspread
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
db = PyMongo(app).db

gc = gspread.service_account(filename='service_account.json')
sh = gc.open("Untitled spreadsheet")
worksheet = sh.worksheet("Sheet1")
values_list = worksheet.row_values(1)
col_list = worksheet.col_values(1)
record = worksheet.get_all_records()


# print(values_list)
print(record)


# class Todo(db.Model):


@app.post('/')
def post():
    data = json.loads(request.data)
    print(data)
    result = db.student.insert_one({"name":data['name']})
    print(result)
    return jsonify({
    "msg":'Your data has been added'
    })
    
@app.get('/')
def get():
    return render_template('index.html')


@app.route('/update_student', methods=['POST'] )
def update_std():
    record = json.loads(request.data)
    print(record)
    return jsonify({
        "msg":"Your data has been updated",
        "name":record["name"]
    })


if __name__ == "__main__":
    app.run(debug=True)
