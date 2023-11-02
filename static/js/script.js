// Enabling Bootstrap's components
window.addEventListener('DOMContentLoaded', () => {
    // Dropdown menus
    $('.dropdown-toggle').dropdown();

    // Tooltips
    $(function () {
        $('[data-toggle="tooltip"]').tooltip();
    });

    // Modals
    $('#myModal').on('shown.bs.modal', function () {
        $('#myInput').trigger('focus');
    });

    // Alerts
    $('.alert').alert();
});