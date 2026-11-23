from pathlib import Path
import json

json_path = Path(__file__).resolve().parent.parent / 'data'/'student.json'

def get_students_data():
    with json_path.open('r',encoding='utf-8') as file:
        return json.load(file)


def get_student(id):
    data = get_students_data()
    for student in data:
        if student['id'] == id:
            return student
    return None
