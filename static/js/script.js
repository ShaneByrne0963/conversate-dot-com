// Enabling Bootstrap's components
window.addEventListener('DOMContentLoaded', () => {
    // Dropdown menus
    $('.dropdown-toggle').dropdown();

    $(function () {
        // Tooltips
        $('[data-toggle="tooltip"]').tooltip();
    });

    // Alerts
    $('.alert').alert();

    // Popovers
    $(function () {
        $('[data-toggle="popover"]').popover({
            html: true
        });
    });

    startPollAnimation();
});

// Displays instructions on how to search by tag, appearing only once per session
$('#search-input').focus(() => {
    if (!sessionStorage.getItem('tag-hint')) {
        $('#search-hint').removeClass('d-none');
        sessionStorage.setItem('tag-hint', 'seen');
    }
});

/**
 * Updates the width of each poll result to animate them
 */
function startPollAnimation() {
    let answers = document.getElementsByClassName('poll-result');
    for (let answer of answers) {
        answer.style.width = answer.innerText;
    }
}


/**
 * Gets if a checkbox that triggers a collapse is checked, and sets the state of
 * the collapse accordingly
 * @returns {Boolean} If the checkbox that enables the collapse is checked
 */
function getCheckboxCollapse() {
    let checked = $('.check-collapse').is(':checked');
    let collapseState = (checked) ? 'show' : 'hide';
    $('.check-collapse-content').collapse(collapseState);
    return checked;
}