from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

grades_page = Blueprint('grades_page', __name__, template_folder='templates')

@grades_page.route('/grades')
def grades_view():
    return render_template('templates_english/grades_home.html')

@grades_page.route('/grades/gpa/calculator')
def gpa_calculator_view():
    return render_template('templates_english/grades/gpa.html')

@grades_page.route('/grades/fgc')
def final_grade_calculator_view():
    return render_template('templates_english/grades/finalgrade.html')