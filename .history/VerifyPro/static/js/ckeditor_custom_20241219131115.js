CKEDITOR.on('instanceReady', function(ev) {
    var editor = ev.editor;
    editor.document.getBody().setStyle('background-color', '#ffffff');
    editor.document.getBody().setStyle('font-family', 'Calibri');
    editor.document.getBody().setStyle('font-size', '14px');
});
