// Focus on the reply text area when it is expanded
$('.reply-collapse').on('shown.bs.collapse', (event) => {
    event.target.getElementsByClassName('form-control')[0].focus();
});


/**
 * Is called when the post details page is loaded. Puts replies within their
 * respective comment
 */
function organizeReplies() {
    let replies = $('.reply');
    for (let reply of replies) {
        let commentId = reply.id;
        commentId = commentId.replace('reply-to-', '');
        let comment = document.getElementById(`comment-${commentId}`);
        let replySection = comment.getElementsByClassName('replies')[0];
        console.log(replySection);
        replySection.appendChild(reply);
    }
}
window.addEventListener('DOMContentLoaded', organizeReplies);