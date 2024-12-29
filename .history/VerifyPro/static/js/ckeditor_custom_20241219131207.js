CKEDITOR.replace('editor', {
    contentsCss: '{% static "ckeditor/ckeditor_custom.css" %}',  // Make sure custom CSS is linked
    height: 400,
    width: '100%',
});

CKEDITOR.on('instanceReady', function(ev) {
    var editor = ev.editor;
    
    // Apply styles directly if needed
    editor.document.getBody().setStyle('background-color', '#ffffff');
    editor.document.getBody().setStyle('font-family', 'Calibri');
    editor.document.getBody().setStyle('font-size', '14px');
});