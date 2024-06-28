# Extract course names and IDs from course_data
from helpers.data import course_data

course_ids = {}
for subject, courses in course_data.items():
    for course_name, course_details in courses.items():
        course_id = course_details["Course ID"]
        course_ids[course_name] = course_id

# Define the filename to save the course IDs
output_file = "course_ids.py"

# Write the course IDs to the output file
with open(output_file, "w") as file:
    file.write("course_ids = {\n")
    for course_name, course_id in course_ids.items():
        file.write(f'    "{course_name}": "{course_id}",\n')
    file.write("}")
