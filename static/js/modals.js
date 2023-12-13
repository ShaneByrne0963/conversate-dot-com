$('.trigger-delete-post').click({ itemType: 'Post' }, setDeleteModal);
$('.trigger-delete-comment').click({ itemType: 'Comment' }, setDeleteModal);
$('.trigger-delete-poll').click({ itemType: 'Poll' }, setDeleteModal);


/**
 * Activates a modal to confirm deleting an item from the database
 */
function setDeleteModal(event) {
    let url = this.getAttribute('data-url');
    let itemType = event.data.itemType;
    $('#modal-all').find('.modal-title').text(`Conform ${itemType} Delete`);

    let bodyHtml = '';
    switch (itemType) {
        case 'Post':
            bodyHtml = `
            <p>Are you sure you want to delete this post?</p>
            <p>Deleting this post cannot be undone and will remove all likes and comments.</p>`;
            break;
        case 'Comment':
            bodyHtml =  `<p>Are you sure you want to delete this comment?</p>`;
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
    $('#modal-all').find('.modal-body').html(bodyHtml);
    $('#modal-all').find('.modal-cancel').attr('aria-label', `Keep ${itemType}`);
    $('#modal-all').find('.modal-confirm').attr('aria-label', `Confirm ${itemType} Delete`).text('Delete').attr('href', url);
    $('#modal-all').modal();
}