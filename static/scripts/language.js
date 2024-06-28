document.addEventListener('DOMContentLoaded', function () {

    function getCookie(name) {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                return decodeURIComponent(cookie.substring(name.length + 1));
            }
        }
        return null;
    }

    const selectedLanguage = getCookie('selected_language');
    const languageButton = document.querySelector('.language-button');
    if (selectedLanguage) {
        languageButton.innerText = selectedLanguage;
    } else {
        languageButton.innerText = 'English';
    }

});

function setLanguage(language) {
    const now = new Date();
    now.setFullYear(now.getFullYear() + 10);
    const expirationDate = now.toUTCString();
    document.cookie = `selected_language=${language}; expires=${expirationDate}; path=/`;
    document.querySelector('.language-button').innerText = language;
    window.location.reload();
}