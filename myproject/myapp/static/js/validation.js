// validation.js
$(document).ready(function () {
    // Ustaw funkcję obsługi zdarzenia na zmianę zawartości pola username
    $("#username").on("input", function () {
        // Pobierz zawartość pola username
        var username = $(this).val();
        // Sprawdź, czy zawiera niedozwolone znaki
        if (!isValidUsername(username)) {
            // Jeśli zawiera niedozwolone znaki, wyświetl komunikat o błędzie
            $("#error-message").text("Użyłeś niedozwolonych znaków.");
            // Uniemożliwienie zatwierdzenia formularza
            $("#registrationForm").prop("disabled", true);
        } else {
            // Jeśli nie zawiera niedozwolonych znaków, wyczyść komunikat o błędzie
            $("#error-message").text("");
            // Włącz możliwość zatwierdzenia formularza
            $("#registrationForm").prop("disabled", false);
        }
    });
});

// Funkcja sprawdzająca, czy nazwa użytkownika zawiera dozwolone znaki
function isValidUsername(username) {
    var pattern = /^[a-zA-Z0-9]+$/;
    return pattern.test(username);
}
