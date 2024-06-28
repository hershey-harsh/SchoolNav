from helpers.data import course_data
from course_ids import course_ids

# Function to get course IDs from course names
# Your existing data
# (Including course_ids and course_data)

import re

def extract_course_names(text):
    # Define a regex pattern to match course names
    pattern = r'Completion of ((?:\b(?:\w+\s?-?\w*)+\b)(?:,?\s?(?:and|,)\s(?:\b(?:\w+\s?-?\w*)+\b))*)'
    
    # Use findall to extract all matching patterns
    matches = re.findall(pattern, text)
    
    # Return the extracted course names
    return matches

for subject, courses in course_data.items():
    for course_name, course_info in courses.items():
        prerequisites = course_info.get("Prerequisite")
        if prerequisites.lower() == "none":
            prerequisite_ids_list = "None"
        else:
            if "and" in prerequisites:
                prerequisite_ids_list = [[],[]]
            else:
                prerequisite_ids_list = "None"

        
        course_info["Multiple Prerequisites"] = prerequisite_ids_list

# Printing the modified course_data
import json
print(json.dumps(course_data, indent=4)) 
