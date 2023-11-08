// Focus on the reply text area when it is expanded
$('.reply-collapse').on('shown.bs.collapse', (event) => {
    event.target.getElementsByClassName('form-control')[0].focus();
});