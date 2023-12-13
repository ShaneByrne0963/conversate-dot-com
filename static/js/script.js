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

// Hiding the search hint when the close button is clicked
$('#search-hint-close').click(() => {
    $('#search-hint').addClass('d-none');
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