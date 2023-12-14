// Deleting posts, comments and polls
$('.trigger-delete-post').click({ itemType: 'Post' }, setDeleteModal);
$('.trigger-delete-comment').click({ itemType: 'Comment' }, setDeleteModal);
$('.trigger-delete-poll').click({ itemType: 'Poll' }, setDeleteModal);

// Logging out
$('.trigger-logout').click(setLogoutModal);

// Reporting posts and comments
$('.trigger-report-post').click({ itemType: 'Post' }, setReportModal);


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


function setReportModal(event) {
    let url = this.getAttribute('data-url');
    let itemType = event.data.itemType;
    let bodyHtml = `
    <label for="offence">Please select the reason for reporting the post.</label>
    <select name="offence" id="offence" class="form-control">
        <option value="hateful">Offensive/Hateful content</option>
        <option value="bully">Bullying/Harassment</option>
        <option value="spam">Spam</option>
        <option value="graphic">Graphic/Violent Imagery</option>
        <option value="misinfo">Misinformation</option>
    </select>
    `;

    let modalObject = {
        title: `Report ${itemType}.`,
        body: bodyHtml,
        url: url,
        textConfirm: 'Send',
        ariaCancel: 'Cancel report'
    };
    setModal(modalObject);
}