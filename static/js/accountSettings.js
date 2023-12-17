$('.check-collapse').on('input', updatePasswordCollapse);


function updatePasswordCollapse() {
    if (getCheckboxCollapse()) {
        $('#password1').attr('required', 'true');
        $('#password2').attr('required', 'true');
    }
    else {
        $('#password1').removeAttr('required');
        $('#password2').removeAttr('required');
    }
}