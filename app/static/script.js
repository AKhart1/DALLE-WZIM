$(document).ready(function() {
    $('#promptForm').on('submit', function(e) {
        e.preventDefault();
        var prompt = $('#prompt').val();

        $.ajax({
            type: 'POST',
            url: '/generate_image', // Ensure this endpoint is correct
            data: { prompt: prompt },
            // contentType: 'application/json',
            success: function(response) {
                if (response.image_url) {
                    var newGalleryItem = `
                    <div class="gallery-item">
                        <img src="${response.image_url}" alt="">
                        <div class="description">${prompt}</div>
                    </div>
                `;
                $('.gallery').prepend(newGalleryItem);
                } else {
                    alert('Error: ' + response.error);
                }
            },
            error: function(response) {
                alert('Failed to generate image.');
            }
        });
    });
});
