// sort.js
$(document).ready(function () {
    // Inicjacja przeciągania i upuszczania zdjęć
    $(".sortable-image").sortable({
        axis: 'x',  // Ogranicz przeciąganie do osi poziomej
        handle: '.drag-handle',  // Ustaw obszar do przeciągania
        update: function (event, ui) {
            // Pobieranie aktualnej kolejności obrazków
            var imageIds = $(".sortable-image .image").map(function () {
                return $(this).data("image-id");
            }).get();

            // Wysłanie żądania AJAX w celu zaktualizowania kolejności
            $.ajax({
                url: "{% url 'myapp:reorder_images' %}",
                type: 'POST',
                data: { image_ids: imageIds },
                success: function (data) {
                    // Obsłuż sukces, na przykład wyświetl komunikat
                    console.log('Kolejność zdjęć została zaktualizowana.');
                },
                error: function (xhr, status, error) {
                    console.error("Błąd aktualizacji kolejności: " + error);
                },
            });
        },
    });
});
