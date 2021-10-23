import json
from flask import Flask
from flask import abort
from flask import request
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/grades')
def get_grades():
    with open("grades.txt", "r") as file:
        readString = ""
        for lines in file:
            readString += lines.strip()
    grades_dict = json.loads(readString)
    response = jsonify(grades_dict)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/grades/<sname>')
def find_grade(sname):
    with open("grades.txt", "r") as file:
        readString = ""
        for lines in file:
            readString += lines.strip()
    grades_dict = json.loads(readString)
    if sname in grades_dict:
        response = jsonify({sname: str(grades_dict[sname])})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        abort(404)

@app.route('/grades', methods=["POST"])
def input_grades():
    with open("grades.txt", "r") as file:
        readString = ""
        for lines in file:
            readString += lines.strip()
    grades_dict = json.loads(readString)
    grades_dict[request.json["name"]] = request.json["grade"]
    with open("grades.txt", "w") as writer:
        json_dump = json.dumps(grades_dict)
        print(json_dump)
        writer.write(json_dump)
    return grades_dict

@app.route('/grades/<sname>', methods=["PUT"])
def update_grade(sname):
    with open("grades.txt", "r") as file:
        readString = ""
        for lines in file:
            readString += lines.strip()
    grades_dict = json.loads(readString)
    grades_dict[sname] = request.json["grade"]
    with open("grades.txt", "w") as writer:
        json_dump = json.dumps(grades_dict)
        print(json_dump)
        writer.write(json_dump)
    return grades_dict




if __name__ == '__main__':
    app.run()