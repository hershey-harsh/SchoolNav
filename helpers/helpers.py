def truncateDescription(description):
    max_words = 20
    words = description.split()
    truncated_words = words[:max_words]
    truncated_description = ' '.join(truncated_words)

    if len(words) > max_words:
        truncated_description += '...'

    return truncated_description

def format_course_names(course_lists):
    formatted_lists = []
    for course_list in course_lists:
        formatted_courses = []
        for course_name in course_list:
            formatted_name = course_name.replace('College Prep', 'CP').replace('Honors', 'H').replace('Advanced Placement', 'AP')
            formatted_name = formatted_name.replace('CP', 'CP -').replace('H', 'H -').replace('AP', 'AP -')
            formatted_courses.append(formatted_name)
        formatted_lists.append(formatted_courses)
    return formatted_lists