from flask import Blueprint, render_template, abort, jsonify, request
from jinja2 import TemplateNotFound
from helpers.grades import weighted_gpa, unweighted_gpa, calculate_required_final_grade

grades_api = Blueprint('grades_api', __name__, template_folder='templates')

@grades_api.route('/api/grades/gpa/calculator', methods=['POST'])
def gpa_api_calc():
    data = request.get_json()
    print(data)
    weighted_gpa_value = weighted_gpa(data)
    unweighted_gpa_value = unweighted_gpa(data)
    print(weighted_gpa_value)
    print(unweighted_gpa_value)
    return jsonify({"weighted_gpa": weighted_gpa_value, "unweighted_gpa": unweighted_gpa_value})

@grades_api.route('/api/grades/fgc/calculator', methods=['POST'])
def fgc_api_calc():
    data = request.get_json()
    return calculate_required_final_grade(data)