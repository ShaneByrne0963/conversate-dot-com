const mobileBreakpoint = 768;

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
    resizeScreen();
    if ($('#list-of-posts').length > 0) {
        finishLoading();
    }
});

// Displays instructions on how to search by tag, appearing only once per session
$('#search-input').focus(() => {
    if (!sessionStorage.getItem('tag-hint')) {
        $('#search-hint').removeClass('d-none');
        sessionStorage.setItem('tag-hint', 'seen');
    }
});

// Toggles the side nav collapse for mobile screens
$('#side-nav-button').click(() => {
    if (!$('#side-nav-collapse').hasClass('expanding')) {
        $('#side-nav-collapse').addClass('expanding');
    }
    if ($('#side-nav-collapse').hasClass('expanded')) {
        $('#side-nav-collapse').removeClass('expanded');
    }
    else {
        $('#side-nav-collapse').addClass('expanded');
    }
});

// Prevents the mobile side nav appearing temporarily when resizing the screen
$('#side-nav-collapse').on('transitionend', function() {
    $(this).removeClass('expanding');
});

$(window).resize(resizeScreen);


/**
 * Rearranges elements in the DOM depending on the screen size
 */
function resizeScreen() {
    let screenWidth = $(document).width();
    let sideNav = $('#side-nav-container').detach();
    if (screenWidth < mobileBreakpoint) {
        $('#side-nav-collapse').append(sideNav);
    }
    else {
        $('#side-nav-large').append(sideNav);
    }
    compactPostContent();
}


/**
 * Removes any loading bar and displays any hidden content. Should be called
 * once all the Javascript called on the page load has completed
 */
function finishLoading() {
    $('.pre-load').remove();
}


/**
 * Hides text in the post preview if the content is too big for it
 */
function compactPostContent() {
    let posts = document.getElementsByClassName('post');
    for (let post of posts) {
        let anchorOverlay = post.querySelector('.post-anchor-overlay');
        let readMore = post.querySelector('.read-more');

        anchorOverlay.classList.remove('hidden-text');
        readMore.classList.remove('d-none');

        let outerHeight = post.querySelector('.post-preview').offsetHeight;
        let innerHeight = post.querySelector('.post-preview-inner').offsetHeight;

        if (innerHeight > outerHeight) {
            anchorOverlay.classList.add('hidden-text');
        }
        else {
            readMore.classList.add('d-none');
        }
    }
}


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