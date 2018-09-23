var form = document.getElementById('file-form');
var fileSelect = document.getElementById('file-select');
var uploadButton = document.getElementById('upload-button');
var name = document.getElementById('file-name');

form.onsubmit = function (event) {
    event.preventDefault();

    var name = document.getElementById('file-name').value;
    // Update button text.
    uploadButton.innerHTML = 'Uploading...';

    // The rest of the code will go here...
    // Get the selected files from the input.
    var files = fileSelect.files;

    // Create a new FormData object.
    var formData = new FormData();
    
    formData.append('name', name);

    // Loop through each of the selected files.
    for (var i = 0; i < files.length; i++) {
        var file = files[i];

        // Add the file to the request.
        formData.append('image', file);
    }

    // Set up the request.
    var xhr = new XMLHttpRequest();

    // Open the connection.
    xhr.open('POST', 'http://10.24.181.158:2567/ParseAnswers/images/', true);

    // Set up a handler for when the request finishes.
    xhr.onload = function () {
        console.log('gothere');
        if (xhr.status === 200) {
            // File(s) uploaded.
            uploadButton.innerHTML = 'Upload';
        } else {
            alert('An error occurred!');
        }
    };
    // Send the Data.
    xhr.send(formData);
}
