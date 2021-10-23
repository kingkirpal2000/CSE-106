import json
from flask import Flask
from flask import abort
from flask import request

app = Flask(__name__)

@app.route('/grades')
def get_grades():
    with open("grades.txt", "r") as file:
        readString = ""
        for lines in file:
            readString += lines.strip()
    grades_dict = json.loads(readString)
    return grades_dict

@app.route('/grades/<sname>')
def find_grade(sname):
    with open("grades.txt", "r") as file:
        readString = ""
        for lines in file:
            readString += lines.strip()
    grades_dict = json.loads(readString)
    if sname in grades_dict:
        return grades_dict[sname]
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




if __name__ == '__main__':
    app.run()