// Deleting posts, comments and polls
$('.trigger-delete-post').click({ itemType: 'Post' }, setDeleteModal);
$('.trigger-delete-comment').click({ itemType: 'Comment' }, setDeleteModal);
$('.trigger-delete-poll').click({ itemType: 'Poll' }, setDeleteModal);

// Logging out
$('.trigger-logout').click(setLogoutModal);

// Edit account
$('.trigger-account-edit').click(setAccountEditModal);


/**
 * Sets the display information of a modal, and triggers it's display
 * @param {Object} infoObject format: { title, body, url, textConfirm, ariaCancel }
 */
function setModal(infoObject) {
    $('#modal-all').find('.modal-title').text(infoObject.title);
    $('#modal-all').find('.modal-body').html(infoObject.body);
    $('#modal-all').find('.modal-cancel').attr('aria-label', infoObject.ariaCancel);
    $('#modal-all').find('.modal-confirm').attr('aria-label', infoObject.title).text(infoObject.textConfirm);
    $('#modal-all').find('form').attr('action', infoObject.url);
    $('#modal-all').modal();
}


/**
 * Activates a modal to confirm deleting an item from the database
 */
function setDeleteModal(event) {
    let url = this.getAttribute('data-url');
    let itemType = event.data.itemType;
    let bodyHtml = '';
    switch (itemType) {
        case 'Post':
            bodyHtml = `
            <p>Are you sure you want to delete this post?</p>
            <p>Deleting this post cannot be undone and will remove all likes and comments.</p>`;
            break;
        case 'Comment':
            bodyHtml = `<p>Are you sure you want to delete this comment?</p>`;
            let commentParent = this.parentNode.parentNode;
            if (commentParent.querySelector('.reply-toggle')) {
                bodyHtml += `<p>Deleting this comment will delete all replies to it.</p>`;
            }
            break;
        case 'Poll':
            bodyHtml = `
            <p>Are you sure you want to delete this poll?</p>
            <p>Deleting this poll cannot be undone and will remove all user answers.</p>`;
            break;
        default:
            break;
    }
    let modalObject = {
        title: `Confirm ${itemType} Delete.`,
        body: bodyHtml,
        url: url,
        textConfirm: 'Delete',
        ariaCancel: `Keep ${itemType}`
    };
    setModal(modalObject);
}


/**
 * Activates a modal to confirm the logout of a user
 */
function setLogoutModal() {
    let url = this.getAttribute('data-url');
    let bodyHtml = '<p>Are you sure you want to log out?</p>';
    
    let modalObject = {
        title: `Confirm Logout.`,
        body: bodyHtml,
        url: url,
        textConfirm: 'Log out',
        ariaCancel: `Stay logged in`
    };
    setModal(modalObject);
}


/**
 * Activates a modal to request the user's password before editing their account
 */
function setAccountEditModal() {
    let url = this.getAttribute('data-url');
    let bodyHtml = `
    <p>Please enter your password to edit your account</p>
    <label for="password">Password</label>
    <input type="password" id="password" name="password" class="form-control">
    `;

    let modalObject = {
        title: `Confirm Identity.`,
        body: bodyHtml,
        url: url,
        textConfirm: 'Confirm',
        ariaCancel: `Cancel`
    };
    setModal(modalObject);
}