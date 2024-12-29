// Wait for the CKEditor instance to be ready
CKEDITOR.on('instanceReady', function (evt) {
    var editor = evt.editor;  // Get the CKEditor instance
    var editorBody = editor.document.getBody();  // Get the body of the editor content
    
    // Set the background color and text color for the editor
    editorBody.setStyle('background-color', '#f0f0f0');  // Set the background color
    editorBody.setStyle('color', '#333333');  // Optionally, change the text color
});
