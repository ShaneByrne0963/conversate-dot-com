// Enabling Bootstrap's components
window.addEventListener('DOMContentLoaded', () => {
    // Dropdown menus
    $('.dropdown-toggle').dropdown();

    $(function () {
        // Tooltips
        $('[data-toggle="tooltip"]').tooltip();
    });

    // Modals
    $('#modal-logout').on('shown.bs.modal', function () {
        $('#nav-logout').trigger('focus');
    });

    // Alerts
    $('.alert').alert();

    // Popovers
    $(function () {
        $('[data-toggle="popover"]').popover({
            html: true
        });
    });
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
})