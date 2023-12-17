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

// Sets the password change input to valid if the checkbox is checked
$(document).ready(() => {
    updatePasswordCollapse();
});