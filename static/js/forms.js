// Changes the function of the "Enter" key depending on what input is focused on
$(document).keypress(function (event) {
    if (event.which == '13') {
        event.preventDefault();
        if ($('input:focus').length > 0) {
            let inputId = $('input:focus').attr('id');
            switch(inputId) {
                // Tag input
                case 'tag-input-text':
                    if (!$('#add-tag').hasClass('disabled')) {
                        $('#add-tag').trigger('click');
                    }
                    break;
                // Poll answer input
                case 'answers':
                    if (!$('#add-answer').hasClass('disabled')) {
                        $('#add-answer').trigger('click');
                    }
                    break;
                // Remove focus for everything else
                default:
                    $('input:focus').blur();
                    break;
            }
        }
        else {
            // If no inputs are focused, attempt to submit the form
            $('.create-form').find('button[type="submit"]').trigger('click');
        }
    }
});