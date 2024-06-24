from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

gpa_page = Blueprint('gpa_page', __name__, template_folder='templates')

@gpa_page.route('/grades/gpa/calculator')
def gpa_calculator_view():
    return render_template('grades/gpa.html')

@gpa_page.route('/grades/fgc')
def final_grade_calculator_view():
    return render_template('grades/finalgrade.html')
