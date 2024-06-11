$(document).ready(function() {
    $('#prompt').on('focus', function() {
        $(this).attr('placeholder', '');
    }).on('blur', function() {
        if ($(this).val() === '') {
            $(this).attr('placeholder', 'Wyszukaj...');
        }
    });

    // Function to set the theme
    function setTheme(theme) {
        document.body.classList.remove('light-theme', 'dark-theme');
        document.body.classList.add(theme);
        localStorage.setItem('theme', theme);
        $('#theme-switcher').prop('checked', theme === 'dark-theme');
    }

    // Get the saved theme from localStorage
    const savedTheme = localStorage.getItem('theme') || 'light-theme';
    setTheme(savedTheme);

    // Event listener for the theme switcher
    $('#theme-switcher').on('change', function() {
        const newTheme = this.checked ? 'dark-theme' : 'light-theme';
        setTheme(newTheme);
    });

    const spinner = document.createElement('div');
    spinner.classList.add('spinner');
    spinner.style.display = 'none';
    document.getElementById('promptForm').appendChild(spinner);

    document.getElementById("random-prompt-btn").addEventListener("click", function() {
        // Fetch the generated description from Flask route
        fetch('/generate-description')  // Change to /generate-description
            .then(response => response.text())
            .then(description => {
                // Get the search input element
                var searchInput = document.getElementById("prompt");
                // Set the description in the input field
                searchInput.value = description;
            })
            .catch(error => console.error('Error:', error));
    });
    

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
