function evalGPA() {
    console.log('evalGPA function called');
    
    var gpaPlaceholder = document.querySelector('.gpa-placeholder');
    var checkbox = document.querySelector('.peer');
    var courseInputs = document.querySelectorAll('.course-input');
    var alertBox = document.getElementById('alert-1');
    var allFilled = true;

    var data = {
        "course1": {
            "grade": document.getElementById("course-1-final-grade").value,
            "course_name": document.getElementById("course-1-name").value,
            "credits": document.getElementById("course-1-credits").value,
            "course_type": document.getElementById("course-1-level").value,
            "type": document.getElementById("course-1-type").value
        },
        "course2": {
            "grade": document.getElementById("course-2-final-grade").value,
            "course_name": document.getElementById("course-2-name").value,
            "credits": document.getElementById("course-1-credits").value,
            "course_type": document.getElementById("course-2-level").value,
            "type": document.getElementById("course-2-type").value
        },
        "course3": {
            "grade": document.getElementById("course-3-final-grade").value,
            "course_name": document.getElementById("course-3-name").value,
            "credits": document.getElementById("course-3-credits").value,
            "course_type": document.getElementById("course-3-level").value,
            "type": document.getElementById("course-3-type").value
        },
        "course4": {
            "grade": document.getElementById("course-4-final-grade").value,
            "course_name": document.getElementById("course-4-name").value,
            "credits": document.getElementById("course-4-credits").value,
            "course_type": document.getElementById("course-4-level").value,
            "type": document.getElementById("course-4-type").value
        },
        "course5": {
            "grade": document.getElementById("course-5-final-grade").value,
            "course_name": document.getElementById("course-5-name").value,
            "credits": document.getElementById("course-5-credits").value,
            "course_type": document.getElementById("course-5-level").value,
            "type": document.getElementById("course-5-type").value
        },
        "course6": {
            "grade": document.getElementById("course-6-final-grade").value,
            "course_name": document.getElementById("course-6-name").value,
            "credits": document.getElementById("course-6-credits").value,
            "course_type": document.getElementById("course-6-level").value,
            "type": document.getElementById("course-6-type").value
        },
        "course7": {
            "grade": document.getElementById("course-6-final-grade").value,
            "course_name": document.getElementById("course-6-name").value,
            "credits": document.getElementById("course-6-credits").value,
            "course_type": document.getElementById("course-6-level").value,
            "type": document.getElementById("course-6-type").value
        }   
    };

    courseInputs.forEach(function(input) {
        if (input.value.trim() === '' || input.value === 'Select Credits' || input.value === 'Select Course Level' || input.value === 'Select Course Type') {
            allFilled = false;
        }
    });

    if (!allFilled) {
        alertBox.classList.remove('hidden');
        setTimeout(function() {
            alertBox.classList.add('hidden');
        }, 6000);
        return;
    } else {
        alertBox.classList.add('hidden');
    }

    if (gpaPlaceholder && checkbox) {
        fetch('/api/grades/gpa/calculator', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            var gpaValues = {
                "weighted_gpa": data.weighted_gpa,
                "unweighted_gpa": data.unweighted_gpa
            };

            if (checkbox.checked) {
                gpaPlaceholder.textContent = `${gpaValues.unweighted_gpa}`;
            } else {
                gpaPlaceholder.textContent = `${gpaValues.weighted_gpa}`;
            }

            checkbox.addEventListener('click', evalGPA);
            checkbox.addEventListener('change', evalGPA);
        })
        .catch(error => {
            console.error('Error fetching GPA data:', error);
        });
    } else {
        console.error('GPA placeholder or checkbox element not found');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    var alertCloseButton = document.querySelector('#alert-1 [data-dismiss-target]');

    if (alertCloseButton) {
        alertCloseButton.addEventListener('click', function() {
            var alertBox = document.getElementById('alert-1');
            alertBox.classList.add('hidden');
        });
    }
});




function evalFGC() {
    const term1 = document.getElementById('term1-input').value;
    const term2 = document.getElementById('term2-input').value;
    const midterm = document.getElementById('midterm-input').value;
    const term3 = document.getElementById('term3-input').value;
    const term4 = document.getElementById('term4-input').value;
    const targetGrade = document.getElementById('grade-want-input').value;

    const data = {
        term_1: term1,
        term_2: term2,
        "midterm_exam": midterm,
        term_3: term3,
        term_4: term4,
        target_grade: targetGrade
    };

    fetch('/api/grades/fgc/calculator', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        document.getElementById('final-grade-display').innerText = data.required_final_grade;

        // Update table with new values
        const tableBody = document.getElementById('grade-table-body');
        tableBody.innerHTML = '';  // Clear existing rows

        const grades = ['90', '89', '88', '87', '86', '85'];
        grades.forEach(grade => {
            const row = document.createElement('tr');
            row.className = 'bg-blue-500 border-b border-blue-400';

            const cell1 = document.createElement('th');
            cell1.scope = 'row';
            cell1.className = 'px-2 py-1 font-medium text-blue-50 whitespace-nowrap dark:text-blue-100';
            cell1.innerText = `${grade}%`;

            const cell2 = document.createElement('td');
            cell2.className = 'px-2 py-1';
            cell2.innerText = `${data[grade]}%`;

            row.appendChild(cell1);
            row.appendChild(cell2);

            tableBody.appendChild(row);
        });

        // Show the table
        document.getElementById('grade-table').classList.remove('hidden');
        document.getElementById('grade-footer').classList.remove('hidden');
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

evalGPA();
