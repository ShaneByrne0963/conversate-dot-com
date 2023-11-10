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

    //
});