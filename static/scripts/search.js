document.addEventListener('DOMContentLoaded', function () {
    const courseLinks = document.querySelectorAll('[data-modal-toggle="default-modal"]');
    const modal = document.getElementById('default-modal');
    const modalTitle = document.querySelector('#default-modal h3');
    const modalDescription = document.querySelector('#default-modal p');
    const searchInput = document.getElementById('default-search');
    const courseCards = document.querySelectorAll('.course-item');

    // Function to open modal and display course details
    courseLinks.forEach(function (link) {
        link.addEventListener('click', function (event) {
            event.preventDefault();
            const courseName = link.querySelector('.text-gray-900').innerText;
            const courseFullDescription = link.querySelector('.full-description').innerText;

            modalTitle.innerText = courseName;
            modalDescription.innerText = courseFullDescription;

            modal.showModal();
        });
    });

    // Function to perform search
    searchInput.addEventListener('input', function () {
        performSearch();
    });

    function performSearch(searchTerm = searchInput.value.toLowerCase()) {
        searchTerm = searchTerm.toLowerCase(); // Remove the redeclaration of searchTerm
    
        courseCards.forEach(function (card) {
            const courseName = card.querySelector('.text-gray-900').innerText.toLowerCase();
            const courseDescription = card.dataset.truncatedDescription.toLowerCase();
    
            if (courseName.includes(searchTerm) || courseDescription.includes(searchTerm)) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }
    

    // Function to filter courses based on categories
    function capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
    }
    
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function () {
            const selectedCategories = Array.from(checkboxes)
                .filter(cb => cb.checked)
                .map(cb => capitalizeFirstLetter(cb.value));
    
            console.log('Selected Categories:', selectedCategories);
    
            courseCards.forEach(item => {
                const categories = item.dataset.categories.split(' ').map(category => capitalizeFirstLetter(category));
                console.log('Course Categories:', categories);
    
                const matchesAnySelectedCategory = selectedCategories.some(selectedCategory => categories.includes(selectedCategory));
    
                if (selectedCategories.length === 0 || matchesAnySelectedCategory) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });
    
     
});
