from data.scaled_grades import scaled_grades

def weighted_gpa(grades_dictonary):
    print(grades_dictonary)
    total_scaled_gpa = []
    total_credits = []

    for course in grades_dictonary:
        scaled_gpa = scaled_grades[str(grades_dictonary[course]["grade"])][grades_dictonary[course]["course_type"]]
        gpa = float(scaled_gpa) * float(grades_dictonary[course]["credits"])
        total_credits.append(int(grades_dictonary[course]["credits"]))
        total_scaled_gpa.append(int(gpa))

    total_scaled_gpa = sum(total_scaled_gpa)
    total_credits = sum(total_credits)

    return round(total_scaled_gpa / total_credits, 2)

def unweighted_gpa(grades_dictonary):
    total_scaled_gpa = []
    total_credits = []

    for course in grades_dictonary:
        scaled_gpa = scaled_grades[str(grades_dictonary[course]["grade"])]["CP"]
        gpa = float(scaled_gpa) * float(grades_dictonary[course]["credits"])
        total_credits.append(int(grades_dictonary[course]["credits"]))
        total_scaled_gpa.append(int(gpa))

    total_scaled_gpa = sum(total_scaled_gpa)
    total_credits = sum(total_credits)

    return round(total_scaled_gpa / total_credits, 2)

def calculate_required_final_grade(data):
    term_1 = float(data['term_1'])
    term_2 = float(data['term_2'])
    term_3 = float(data['term_3'])
    term_4 = float(data['term_4'])
    midterm_exam = float(data['midterm_exam'])
    target_grade = float(data['target_grade'])
    
    term_weight = 0.2
    midterm_weight = 0.1
    final_weight = 0.1

    current_grade = ((term_1 + term_2 + term_3 + term_4) * term_weight + (midterm_exam * midterm_weight)) / 0.90

    results = {}
    target_grades = [90, 89, 88, 87, 86, 85]

    for grade in target_grades:
        required_final_grade = (grade - (1 - final_weight) * current_grade) / final_weight
        if required_final_grade < 0:
            required_final_grade = 0
        results[f"{grade}"] = round(required_final_grade, 4)

    required_final_grade = (target_grade - (1 - final_weight) * current_grade) / final_weight
    if required_final_grade < 0:
        required_final_grade = 0
    results['required_final_grade'] = f'{round(required_final_grade, 4)}%'

    return results
