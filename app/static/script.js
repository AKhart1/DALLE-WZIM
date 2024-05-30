$(document).ready(function() {
    $('#promptForm').on('submit', function(e) {
        e.preventDefault(); // Prevent the default form submission

        var prompt = $('#prompt').val();

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
            }
        });
    });
    const imageContainer = document.getElementById('image-container');

    function displayImage(images_data) {

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
        data.forEach(images_data => displayImage(images_data));
      })
      .catch(error => console.error(error));
});
