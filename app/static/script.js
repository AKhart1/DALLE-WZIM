$(document).ready(function() {
    $('#promptForm').on('submit', function(e) {
        e.preventDefault();
        var prompt = $('#prompt').val();

        $.ajax({
            type: 'POST',
            url: '/generate_image', // Corrected URL
            data: { prompt: prompt },
            success: function(response) {
                if (response.image_url) {
                    $('#generatedImage').attr('src', response.image_url).show();
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