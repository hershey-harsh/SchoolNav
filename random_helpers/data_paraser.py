import json
import re

def convert_course_description(text):
    course_info = {}
    courses = text.split("\n\n")  # Split the text into individual course descriptions
    for course in courses:
        lines = course.split("\n")
        if len(lines) < 2:
            continue
        header = lines[0].split(" - ")
        if len(header) < 2:
            continue
        course_id, title = header[0], header[1]
        description = "\n".join(lines[1:])
        match = re.search(r'(\d+)\s+([A-Z\s]+)\s(\d+)\s+CREDITS\s+\(Open to students in grades (\d+)-(\d+) as elective, fulfills one-year of World Lang requirement\)', description)
        if match:
            course_info[f"{title.strip()} {match.group(5)}"] = {
                "Description": description[match.end():].strip(),
                "Credits": match.group(3).strip(),
                "Course ID": course_id.strip(),
                "Grade_Level": f"{match.group(4)}-{match.group(5)}",
                "Academic_Level": match.group(7).strip(),
                "Prerequisite": "None",
                "Elective": "Yes",
                "Prerequisite IDs": "None",
                "Multiple Prerequisites": "None"
            }
    return {"Class": course_info}

# Input text containing multiple course descriptions
input_text = """
411 HONORS FRENCH 1 - 6 CREDITS 
(Open to students in grades 9-12 as elective, fulfills one-year of World Lang requirement)
This course is intended for above average students who have an interest in learning about the French language and culture. The basics of French grammar and vocabulary will be emphasized and students will study aspects of the culture. Upon completion of this course, the student will have developed solid written and verbal skills to prepare them for Honors French 2.

410 CP FRENCH 1 - 6 CREDITS 
(Open to students in Grades 9-12 as elective, fulfills one-year of World Lang requirement)
In this introductory course, students will develop the fundamentals of the four linguistic skills of listening, speaking, reading, and writing. Students will use a variety of print and audio visual materials to discover the geography and cultural richness of the Francophone world.
"""

# Convert the input text to JSON
json_output = json.dumps(convert_course_description(input_text), indent=4)
print(json_output)
