$(document).ready(function() {
    const spinner = document.createElement('div');
    spinner.classList.add('spinner');
    spinner.style.display = 'none';
    document.getElementById('promptForm').appendChild(spinner);

    $('#promptForm').on('submit', function(e) {
        e.preventDefault(); // Prevent the default form submission

        var prompt = $('#prompt').val();

        // Show the spinner
        spinner.style.display = 'inline-block';

        $.ajax({
            type: 'POST',
            url: '/generate_image',
            data: { prompt: prompt },
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
            },
            complete: function() {
                // Hide the spinner
                spinner.style.display = 'none';
            }
        });
    });

    function displayImages(images_data) {
        var GalleryItem = `
            <div class="gallery-item">
                <img src="../static/generated_images/${images_data['name']}" alt="">
                <div class="description">${images_data['prompt']}</div>
            </div>
        `;
        $('.gallery').prepend(GalleryItem);
    }

    fetch('/get_images')
        .then(response => response.json())
        .then(data => {
            data.forEach(images_data => displayImages(images_data));
        })
        .catch(error => console.error(error));
});
