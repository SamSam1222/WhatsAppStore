// Example: Custom JavaScript for CKEditor
CKEDITOR.on('instanceReady', function(ev) {
    var editor = ev.editor;

    // Custom behavior: changing editor's background color
    editor.document.getBody().setStyle('background-color', '#f4f4f4'); // Light gray background
    editor.document.getBody().setStyle('font-family', 'Arial'); // Change font to Arial
});

// Example: Adding a custom toolbar button
CKEDITOR.plugins.add('myplugin', {
    init: function(editor) {
        editor.ui.addButton('MyButton', {
            label: 'My Button',
            command: 'myCommand',
            toolbar: 'insert'
        });

        editor.addCommand('myCommand', {
            exec: function(editor) {
                alert('My custom button clicked!');
            }
        });
    }
});
