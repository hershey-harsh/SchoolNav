from flask import Blueprint, render_template, abort, request, url_for, json
from api_routes.courses import pathway_creator_select
from helpers.helpers import truncateDescription
from helpers.helpers import format_course_names
from helpers.languages import english_to_spanish
from data.course_data import course_data
from jinja2 import TemplateNotFound

courses_page = Blueprint('courses_page', __name__, template_folder='templates')

@courses_page.route('/courses')
def courses_view():
    return render_template('templates_english/courses_home.html')

@courses_page.route('/courses/catalog')
def course_catalog_view():
    selected_language = request.cookies.get('selected_language')
    if selected_language == "Spanish":
        return render_template('templates_spanish/course_catalog.html', course_data=course_data, truncateDescription=truncateDescription, english_to_spanish=english_to_spanish)
    return render_template('templates_english/courses/course_catalog.html', course_data=course_data, truncateDescription=truncateDescription)

@courses_page.route('/courses/pathway_creator', methods=['POST', 'GET'])
def pathway_creator():
    return render_template('templates_english/pathway_creator/1.html')

@courses_page.route('/courses/pathway_creator/select', methods=['POST', 'GET'])
def current_and_taken_courses_select():
    grade_level = request.form.get('yog')
    english, math, science, social_studies, world_language = pathway_creator_select(int(grade_level))
    formatted_lists = format_course_names([english, math, science, social_studies, world_language])

    return render_template('templates_english/pathway_creator/2.html',
        english_classes=formatted_lists[0],
        math_classes=formatted_lists[1],
        science_classes=formatted_lists[2],
        history_classes=formatted_lists[3],
        language_classes=formatted_lists[4],
    )

@courses_page.route('/courses/builder', methods=['POST', 'GET'])
def course_builder_tool():
    return render_template('templates_english/courses/builder.html', course_data=course_data, truncateDescription=truncateDescription)

@courses_page.route('/courses/builder/9th', methods=['POST', 'GET'])
def course_builder_tool_9th():
    return render_template('templates_english/courses/builder/builder9.html', course_data=course_data, truncateDescription=truncateDescription)

@courses_page.route('/courses/builder/10th', methods=['POST', 'GET'])
def course_builder_tool_10th():
    return render_template('templates_english/courses/builder/builder10.html', course_data=course_data, truncateDescription=truncateDescription)

@courses_page.route('/courses/builder/11th', methods=['POST', 'GET'])
def course_builder_tool_11th():
    return render_template('templates_english/courses/builder/builder11.html', course_data=course_data, truncateDescription=truncateDescription)

@courses_page.route('/courses/builder/12th', methods=['POST', 'GET'])
def course_builder_tool_12th():
    return render_template('templates_english/courses/builder/builder12.html', course_data=course_data, truncateDescription=truncateDescription)