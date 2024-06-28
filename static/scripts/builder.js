let courseData = {};

fetch('/static/course_data.json')
    .then(response => response.json())
    .then(data => {
        courseData = data;
    })
    .catch(error => console.error('Error loading course data:', error));

function openModal(cardElement, subject, gradeLevel) {
    const modal = document.getElementById('myModal');
    const courseList = document.getElementById('courseList');
    const modalTitle = document.getElementById('modalTitle');
    const searchInput = document.getElementById('default-search');

    modalTitle.textContent = `Search ${subject} Courses for Grade ${gradeLevel}`;
    searchInput.setAttribute('data-subject', subject);
    searchInput.setAttribute('data-grade', gradeLevel);
    searchInput.setAttribute('data-card-id', cardElement.querySelector('span').id);
    courseList.innerHTML = '';

    modal.classList.remove('hidden');
}

function closeModal() {
    const modal = document.getElementById('myModal');
    modal.classList.add('hidden');
}

function filterCourses() {
    const searchInput = document.getElementById('default-search');
    const subject = searchInput.getAttribute('data-subject');
    const gradeLevel = searchInput.getAttribute('data-grade');
    const searchTerm = searchInput.value.toLowerCase();
    const courseList = document.getElementById('courseList');

    courseList.innerHTML = '';

    if (!courseData[subject]) return;

    const courses = Object.entries(courseData[subject]).filter(([courseName, courseDetails]) => {
        const gradeLevels = courseDetails['Grade_Level'].split('/');
        return gradeLevels.includes(gradeLevel.toString()) &&
               (courseName.toLowerCase().includes(searchTerm) || courseDetails['Description'].toLowerCase().includes(searchTerm)) &&
               courseDetails['Elective'] === "No";
    });

    // Limit the results to 5
    const limitedCourses = courses.slice(0, 5);

    limitedCourses.forEach(([courseName, courseDetails]) => {
        const li = document.createElement('li');
        li.className = 'cursor-pointer p-2 hover:bg-gray-200 dark:hover:bg-gray-600';
        li.textContent = courseName;
        li.onclick = () => selectCourse(courseName, courseDetails, searchInput.getAttribute('data-card-id'));
        courseList.appendChild(li);
    });

    // Ensure the scroll properties are applied
    if (courses.length > 5) {
        courseList.classList.add('max-h-40', 'overflow-y-auto');
    } else {
        courseList.classList.remove('max-h-40', 'overflow-y-auto');
    }
}

function getShortDescription(description, wordLimit) {
    const words = description.split(' ');
    if (words.length <= wordLimit) {
        return description;
    }
    return words.slice(0, wordLimit).join(' ') + '...';
}

function selectCourse(courseName, courseDetails, cardId) {
    const cardElement = document.getElementById(cardId).closest('a');
    const cardTextElement = document.getElementById(cardId);

    if (courseName.includes("Integrated")) {
        cardTextElement.textContent = courseName.replace("Integrated", "");
    } else if (courseName.includes("College Prep")) {
        cardTextElement.textContent = courseName.replace("College Prep", "");
    } else if (courseName.includes("Honors")) {
        cardTextElement.textContent = courseName.replace("Honors", "");
    } else if (courseName.includes("Advanced Placement")) {
        cardTextElement.textContent = courseName.replace("Advanced Placement", "");
    } else {
        cardTextElement.textContent = courseName;
    }

    // Add centering class to card text element
    cardTextElement.className = "block text-center text-sm"; // Reduced font size

    const labelsContainer = document.createElement('div');
    labelsContainer.className = "flex justify-center space-x-2 mt-2";

    // Add course type label
    if (courseName.includes("Integrated")) {
        labelsContainer.innerHTML += '<span class="bg-pink-100 text-pink-800 text-xs font-medium px-2.5 py-0.5 rounded dark:bg-pink-900 dark:text-pink-300">Integrated</span>';
    } else if (courseName.includes("College Prep")) {
        labelsContainer.innerHTML += '<span class="bg-green-100 text-green-800 text-xs font-medium px-2.5 py-0.5 rounded dark:bg-green-900 dark:text-green-300">College Prep</span>';
    } else if (courseName.includes("Honors")) {
        labelsContainer.innerHTML += '<span class="bg-yellow-100 text-yellow-800 text-xs font-medium px-2.5 py-0.5 rounded dark:bg-yellow-900 dark:text-yellow-300">Honors</span>';
    } else if (courseName.includes("Advanced Placement")) {
        labelsContainer.innerHTML += '<span class="bg-indigo-100 text-indigo-800 text-xs font-medium px-2.5 py-0.5 rounded dark:bg-indigo-900 dark:text-indigo-300">Advanced Placement</span>';
    } else {
        labelsContainer.innerHTML += '<span class="bg-green-100 text-green-800 text-xs font-medium px-2.5 py-0.5 rounded dark:bg-green-900 dark:text-green-300">Integrated</span>';
    }

    // Add credits label
    if (courseDetails.Credits.includes("6")) {
        labelsContainer.innerHTML += '<span class="bg-blue-100 text-blue-800 text-xs font-medium px-2.5 py-0.5 rounded dark:bg-blue-900 dark:text-blue-300">Full Year</span>';
    } else if (courseDetails.Credits.includes("3")) {
        labelsContainer.innerHTML += '<span class="bg-gray-100 text-gray-800 text-xs font-medium px-2.5 py-0.5 rounded dark:bg-gray-700 dark:text-gray-300">Semester</span>';
    }

    // Update card element with labels
    const labelsElement = cardElement.querySelector('.labels');
    labelsElement.innerHTML = ''; // Clear existing labels
    labelsElement.appendChild(labelsContainer); // Append the new labels

    // Replace SVG with course description
    const shortDescription = getShortDescription(courseDetails.Description, 1);
    const descriptionElement = cardElement.querySelector('.flex.justify-center.p-4');
    descriptionElement.innerHTML = `<p class="text-gray-500 dark:text-gray-400 text-center text-xs"><b>Course ID: </b>${courseDetails.Course_ID}</p>`;
    closeModal();
}

document.getElementById('toggleElective').addEventListener('change', function() {
    var fullYearElective = document.getElementById('fullYearElective');
    var halfYearElective1 = document.getElementById('halfYearElective1');
    var halfYearElective2 = document.getElementById('halfYearElective2');
    
    if (this.checked) {
        fullYearElective.classList.add('hidden');
        halfYearElective1.classList.remove('hidden');
        halfYearElective2.classList.remove('hidden');
    } else {
        fullYearElective.classList.remove('hidden');
        halfYearElective1.classList.add('hidden');
        halfYearElective2.classList.add('hidden');
    }
});