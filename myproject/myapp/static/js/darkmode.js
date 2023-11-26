// function myFunction() {
//     var element = document.body;
//     element.classList.toggle("dark-mode");
//   }

// Skrypt dołączony do panel.html

// Funkcja ustawiająca tryb ciemny
function setDarkMode(isDarkMode) {
    var element = document.body;
    element.classList.toggle("dark-mode", isDarkMode);
    localStorage.setItem("darkMode", isDarkMode);
}

// Funkcja obsługująca kliknięcie przycisku
function toggleDarkMode() {
    var isDarkMode = document.body.classList.contains("dark-mode");
    setDarkMode(!isDarkMode);
}

// Sprawdzenie stanu trybu ciemnego w localStorage
document.addEventListener("DOMContentLoaded", function () {
    var savedDarkMode = localStorage.getItem("darkMode");
    if (savedDarkMode !== null) {
        setDarkMode(savedDarkMode === "true");
    }
});
