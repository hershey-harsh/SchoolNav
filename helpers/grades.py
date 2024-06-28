from PIL import Image, ImageDraw, ImageFont
import random
import os

scaled_grades = {
    "100": {"CP": 4.3, "Honors": 4.8, "AP": 5.3},
    "99": {"CP": 4.3, "Honors": 4.8, "AP": 5.3},
    "98": {"CP": 4.2, "Honors": 4.7, "AP": 5.2},
    "97": {"CP": 4.2, "Honors": 4.7, "AP": 5.2},
    "96": {"CP": 4.1, "Honors": 4.6, "AP": 5.1},
    "95": {"CP": 4, "Honors": 4.5, "AP": 5},
    "94": {"CP": 4, "Honors": 4.5, "AP": 5},
    "93": {"CP": 3.9, "Honors": 4.4, "AP": 4.9},
    "92": {"CP": 3.8, "Honors": 4.3, "AP": 4.8},
    "91": {"CP": 3.7, "Honors": 4.2, "AP": 4.7},
    "90": {"CP": 3.6, "Honors": 4.1, "AP": 4.6},
    "89": {"CP": 3.4, "Honors": 3.9, "AP": 4.4},
    "88": {"CP": 3.3, "Honors": 3.8, "AP": 4.3},
    "87": {"CP": 3.2, "Honors": 3.7, "AP": 4.2},
    "86": {"CP": 3.1, "Honors": 3.6, "AP": 4.1},
    "85": {"CP": 3, "Honors": 3.5, "AP": 4},
    "84": {"CP": 2.9, "Honors": 3.4, "AP": 3.9},
    "83": {"CP": 2.8, "Honors": 3.3, "AP": 3.8},
    "82": {"CP": 2.7, "Honors": 3.2, "AP": 3.7},
    "81": {"CP": 2.6, "Honors": 3.1, "AP": 3.6},
    "80": {"CP": 2.4, "Honors": 2.9, "AP": 3.4},
    "79": {"CP": 2.3, "Honors": 2.8, "AP": 3.3},
    "78": {"CP": 2.2, "Honors": 2.7, "AP": 3.2},
    "77": {"CP": 2.1, "Honors": 2.6, "AP": 3.1},
    "76": {"CP": 2, "Honors": 2.5, "AP": 3},
    "75": {"CP": 1.9, "Honors": 2.4, "AP": 2.9},
    "74": {"CP": 1.8, "Honors": 2.3, "AP": 2.8},
    "73": {"CP": 1.7, "Honors": 2.2, "AP": 2.7},
    "72": {"CP": 1.6, "Honors": 2.1, "AP": 2.6},
    "71": {"CP": 1.4, "Honors": 1.9, "AP": 2.4},
    "70": {"CP": 1.3, "Honors": 1.8, "AP": 2.3},
    "69": {"CP": 1.2, "Honors": 1.7, "AP": 2.2},
    "68": {"CP": 1.1, "Honors": 1.6, "AP": 2.1},
    "67": {"CP": 0.9, "Honors": 1.4, "AP": 1.9},
    "66": {"CP": 0.8, "Honors": 1.3, "AP": 1.8},
    "65": {"CP": 0.7, "Honors": 1.2, "AP": 1.7},
}

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

    # Calculate the required final grade for the provided target_grade
    required_final_grade = (target_grade - (1 - final_weight) * current_grade) / final_weight
    if required_final_grade < 0:
        required_final_grade = 0
    results['required_final_grade'] = f'{round(required_final_grade, 4)}%'

    return results