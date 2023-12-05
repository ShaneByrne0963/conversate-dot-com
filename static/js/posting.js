// Adds a tag entered by the user to the list of tags
$('#add-tag').click((event) => {
    event.preventDefault();
    let tagName = $('#tag').val();
    let tagElement = document.createElement('div');
    tagElement.className = 'tag-list-item mr-2 mb-2';
    tagElement.innerHTML = `
    <div class="d-flex align-items-center justify-space-between p-1">
        <em class="tag-name">#${tagName}</em>
        <button type="button" class="close ml-2 mr-1" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>
    </div>
    `;
    tagElement.querySelector('button').addEventListener('click', removeTag);
    $('#tags-list').append(tagElement);
    $('#tag').val('');
    setTagAddState(false);
});


// Updates the add tag button to be enabled only when the tag is valid
$('#tag').on('input', checkTagInput);


/**
 * Checks the value in the tag text input, updating the add button and feedback
 * message where necessary
 */
function checkTagInput() {
    let tagName = $('#tag').val();
    let feedbackMessage = (tagName) ? "You have already entered this tag" : "";
    setTagAddState(tagIsUnique(tagName), feedbackMessage);
}


/**
 * Checks if a tag does not already exist in the list of tags
 * @param {String} tagName the name of the new tag
 * @returns {Boolean} True if the tag does not already exist
 */
function tagIsUnique(tagName) {
    let existingTags = $('.tag-name').text();
    let tagList = existingTags.split('#');
    for (let tag of tagList) {
        if (tagName.toLowerCase() === tag.toLowerCase()) {
            return false;
        }
    }
    return true;
}


/**
 * Updates the active state of the "Add Tag" button and the feedback message
 * underneath the input
 * @param {Boolean} enabled Whether the button will be set to enabled/disabled
 * @param {String} feedback The message that explains to the user how to make their tag input valid
 */
function setTagAddState(enabled, feedback) {
    $('#add-tag').removeClass('disabled').removeAttr('disabled');
    $('#tag').removeClass('is-invalid');
    $('#tag-feedback').text('');
    if (!enabled) {
        $('#add-tag').addClass('disabled').attr('disabled', true);
        if (feedback) {
            $('#tag').addClass('is-invalid');
            $('#tag-feedback').text(feedback);
        }
    }
}


/**
 * Removes a tag. Is called when the "X" in a tag is clicked on
 * @param {Event} event The click event that was called
 */
function removeTag(event) {
    let tagParent = event.target.parentNode.parentNode.parentNode;
    tagParent.remove();
    checkTagInput();
}