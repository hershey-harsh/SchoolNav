from flask import Blueprint, render_template, abort, request
from data.course_data import course_data
from jinja2 import TemplateNotFound

courses_api = Blueprint('courses_api', __name__, template_folder='templates')

@courses_api.route('/api/courses/pathway_creator/select', methods=['POST'])
def pathway_creator_select(grade_level):
    english = {}
    math = {}
    science = {}
    social_studies = {}
    world_language = {}

    for course_category, courses in course_data.items():
        for course_name, course_info in courses.items():
            if "Grade_Level" in course_info:
                course_grades = course_info["Grade_Level"].split("/")
                if str(grade_level) in course_grades:
                    if course_category == "English":
                        if course_info["Elective"] == "No":
                            english[course_name] = course_info
                    elif course_category == "Math":
                        if course_info["Elective"] == "No":
                            math[course_name] = course_info
                    elif course_category == "Science":
                        if course_info["Elective"] == "No":
                            science[course_name] = course_info
                    elif course_category == "Social Studies":
                        if course_info["Elective"] == "No":
                            social_studies[course_name] = course_info
                    elif course_category == "World Language":
                        if course_info["Elective"] == "No":
                            world_language[course_name] = course_info

    return list(english.keys()), list(math.keys()), list(science.keys()), list(social_studies.keys()), list(world_language.keys())

