// Focus on the reply text area when it is expanded
$('.reply-collapse').on('shown.bs.collapse', (event) => {
    event.target.getElementsByClassName('form-control')[0].focus();
});


/**
 * Is called when the post details page is loaded. Puts replies within their
 * respective comment and sorts them by posted_on, with the oldest replies
 * being at the top
 */
function organizeReplies() {
    let comments = [];
    let replies = $('.reply');
    // Sorting the replies into their respective comments
    for (let reply of replies) {
        let foundIndex = getComment(reply, comments);
        if (foundIndex >= 0) {
            insertReply(reply, comments[foundIndex]);
        }
        else {
            let timestamp = reply.getAttribute('data-timestamp');
            comments.push({
                id: reply.getAttribute('data-reply-to'),
                replies: [{
                    element: reply,
                    timestamp: timestamp
                }]
            });
        }
    }
    // Attaching the reply objects to each comment
    for (let comment of comments) {
        let commentElement = document.getElementById(`comment-${comment.id}`);
        let replySection = commentElement.getElementsByClassName('replies')[0];
        for (let reply of comment.replies) {
            replySection.appendChild(reply.element);
            reply.element.classList.remove('d-none');
        }
    }
}


/**
 * Finds the comment that a reply belongs to, and returns the index of that
 * comment in the comments array. Returns -1 if no such comment exists
 * @param {Element} reply The reply to get the comment for
 * @param {Array} comments A list of comment objects that have found replies
 * @returns {Integer} The index of the found comment, or -1 if none
 */
function getComment(reply, comments) {
    let commentId = reply.getAttribute('data-reply-to');
    for (let i = 0; i < comments.length; i++) {
        let comment = comments[i];
        if (comment.id === commentId) {
            return i;
        }
    }
    return -1;
}


/**
 * Inserts a reply into a comment, keeping the newest comments at the bottom
 * @param {Element} newReply The reply element to be inserted into the comment
 * @param {Object} comment An object of the comment {id, replies}
 */
function insertReply(newReply, comment) {
    let timestamp = newReply.getAttribute('data-timestamp');

    for (let i = 0; i < comment.replies.length; i++) {
        let reply = comment.replies[i];
        if (timestamp <= reply.timestamp) {
            comment.replies.splice(i, 0, {
                element: newReply,
                timestamp: timestamp
            });
            return;
        }
    }
    comment.replies.push({
        element: newReply,
        timestamp: timestamp
    });
}

/**
 * Is called when a user clicks on the edit button for one of their comments.
 * Replaces the comment with a text area and a save and cancel button
 * @param {Event} event The edit button that was clicked on
 * @param {Boolean} enable Whether to enable or disable the text area
 */
function editComment(event) {
    // Moving up the DOM to find the root comment element
    let comment = event.target;
    do {
        comment = comment.parentNode;
    }
    while (!comment.classList.contains('comment'));

    let commentBody = comment.querySelector('.comment-body');
    let commentEditField = comment.querySelector('.comment-edit-field');

    if (event.data.enable) {
        // First disabling any other enabled edits
        $('.cancel-edit').trigger('click', {
            enable: false
        });

        commentBody.classList.add('d-none');
        // Prepopulating the text area with the original comment text
        editTextArea = commentEditField.querySelector('textarea');
        editTextArea.value = comment.querySelector('.comment-text').innerText;
        commentEditField.classList.remove('d-none');
    }
    else {
        commentBody.classList.remove('d-none');
        commentEditField.classList.add('d-none');
    }
}


window.addEventListener('DOMContentLoaded', organizeReplies);
$('.edit-comment').click({ enable: true }, editComment);
$('.cancel-edit').click({ enable: false }, editComment);