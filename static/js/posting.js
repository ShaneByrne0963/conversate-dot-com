const tagCharLimit = 200;

// Adds a tag entered by the user to the list of tags
$('#add-tag').click((event) => {
    event.preventDefault();
    let tagName = $('#tag-input-text').val();
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
    $('#tag-input-text').val('');
    setTagAddState(false);
    updateTagListValue();
});


// Updates the add tag button to be enabled only when the tag is valid
$('#tag-input-text').on('input', checkTagInput);

// Adds the ability to remove already entered tags
$('.tag-list-item').find('button').click(removeTag);

// Displays a preview of the uploaded image.
// Source: https://stackoverflow.com/questions/18457340/how-to-preview-selected-image-in-input-type-file-in-popup-using-jquery
$('#post-image').change(() => {
    let imageFiles = $('#post-image').prop('files');
    $('#post-image').removeClass('is-invalid');
    $('#image-feedback').removeClass('d-block');
    if (imageFiles && imageFiles[0]) {
        // Validation of the upload, ensuring it is an image
        let uploadFile = imageFiles[0].type;
        let allowedFiles = $('#post-image').attr('accept').replace(' ', '').split(',');

        if (allowedFiles.includes(uploadFile)) {
            let reader = new FileReader();
            reader.readAsDataURL(imageFiles[0]);
            reader.onload = function (event) {
                $('#preview-image').removeClass('d-none').attr('src', event.target.result);
                $('#preview-empty').addClass('d-none');
                // Reveal the preview and image position for mobile screens
                $('#image-options-small').collapse('show');
                addClearImageButton();
            };
        }
        else {
            $('#post-image').addClass('is-invalid').val(null);
            $('#image-feedback').addClass('d-block');
            $('#preview-image').addClass('d-none');
            $('#preview-empty').removeClass('d-none');
            $('#image-options-small').collapse('hide');
        }
    }
});

// Is called when the user resets the form
$('form').on('reset', () => {
    $('.tag-list-item').remove();
    $('#poll-collapse').collapse('hide');
    clearImage();
});

// Updates the poll collapse when the user clicks on the checkbox
$('.check-collapse').on('input', updatePollCollapse);
$('.check-collapse-content').on('shown.bs.collapse', updatePollCollapse);
$('.check-collapse-content').on('hidden.bs.collapse', updatePollCollapse);


/**
 * Adds a button to clear an image from the post
 */
function addClearImageButton() {
    if ($('#delete-image').length == 0) {
        let deleteButton = document.createElement('button');
        deleteButton.id = 'delete-image';
        deleteButton.setAttribute('type', 'button');
        deleteButton.setAttribute('aria-label', 'Delete this image.');
        deleteButton.innerHTML = `<i class="fa-solid fa-trash"></i>`;
        deleteButton.className += 'btn';
        deleteButton.addEventListener('click', clearImage);
        $('#preview').append(deleteButton);
    }
}


/**
 * Removes an image that has not yet been uploaded to cloudinary from the post
 */
function clearImage() {
    $('#post-image').val('');
    $('#preview-image').attr('src', '').removeClass('d-none').addClass('d-none');
    $('#preview-empty').removeClass('d-none');
    $('#delete-image').remove();

    // Hide the preview and image position inputs for mobile
    $('#image-options-small').collapse('hide');
}


/**
 * Shows or hides the poll collapse div, depending on if the checkbox is
 * checked or not
 */
function updatePollCollapse() {
    if (getCheckboxCollapse()) {
        $('#poll-title').attr('required', 'true');
        $('#due-date').attr('required', 'true');
        checkEnoughAnswers();
    }
    else {
        $('#poll-title').removeAttr('required');
        $('#due-date').removeAttr('required');
        setValidAnswers(true);
    }
}


/**
 * Checks the value in the tag text input, updating the add button and feedback
 * message depending on if the entered tag is valid or not
 */
function checkTagInput() {
    let tagName = $('#tag-input-text').val();
    let tagIsValid = true;
    let feedbackMessage = "";

    if (tagName === "") {
        tagIsValid = false;
    }
    else if (!tagObeysCharLimit(tagName)) {
        tagIsValid = false;
        feedbackMessage = 'You have exceeded your tag character limit.';
    }
    else if (!tagHasAllowedChars(tagName)) {
        tagIsValid = false;
        feedbackMessage = 'Tag must only contain letters, numbers, "-" or "_".';
    }
    else if (!tagIsUnique(tagName)) {
        tagIsValid = false;
        feedbackMessage = "You have already entered this tag.";
    }
    setTagAddState(tagIsValid, feedbackMessage);
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
 * Checks if a tag name does not contain any invalid characters
 * @param {String} tagName The tag entered by the user
 * @returns {Boolean} If the tag only contains allowed characters
 */
function tagHasAllowedChars(tagName) {
    // Allows all letters, numbers, "_" and "-"
    allowedChars = /[a-zA-Z0-9_-]/g;
    remainingChars = tagName.replace(allowedChars, '');
    return (remainingChars === '');
}


/**
 * Checks if the tag entered by the user is within the character limit allowed
 * for tags, including the list of other tags previously entered
 * @param {String} tagName The name of the new tag
 * @returns {Boolean} True if the new tag will not exceed the character limit
 */
function tagObeysCharLimit(tagName) {
    let existingTags = $('.tag-name').text();
    existingTags += `#${tagName}`;
    return (existingTags.length <= tagCharLimit);
}


/**
 * Updates the active state of the "Add Tag" button and the feedback message
 * underneath the input
 * @param {Boolean} enabled Whether the button will be set to enabled/disabled
 * @param {String} feedback The message that explains to the user how to make their tag input valid
 */
function setTagAddState(enabled, feedback) {
    $('#add-tag').removeClass('disabled').removeAttr('disabled');
    $('#tag-input-text').removeClass('is-invalid');
    $('#tag-feedback').text('');
    if (!enabled) {
        $('#add-tag').addClass('disabled').attr('disabled', true);
        if (feedback) {
            $('#tag-input-text').addClass('is-invalid');
            $('#tag-feedback').text(feedback);
        }
    }
}


/**
 * Updates the tag input value that will be sent to the database
 */
function updateTagListValue() {
    $('#tags').val($('.tag-name').text());
}


/**
 * Removes a tag. Is called when the "X" in a tag is clicked on
 * @param {Event} event The click event that was called
 */
function removeTag(event) {
    let tagParent = event.target.parentNode.parentNode.parentNode;
    tagParent.remove();
    checkTagInput();
    updateTagListValue();
}


/**
 * Attaches the input event listener to the summernote text field when it is created
 */
function summernoteInit() {
    let iFrame = $('iframe').get(0);
    let summernote = iFrame.contentWindow.document;
    let contentField = summernote.querySelector('.note-editing-area');
    if (contentField) {
        contentField.addEventListener('input', checkBodyValid);
        // Prepopulating the text field if the post is being edited
        let previousInput = document.querySelector('#previous-content');
        if (previousInput) {
            contentField.querySelector('.note-editable').innerHTML = previousInput.getAttribute('value');
            checkBodyValid();
        }
        // Preventing the toolbar dropdowns from overflowing out of the editor
        $('iframe').attr('scrolling', 'no');

        // Removing the option to open the link in the same tab
        $(contentField).find('.sn-checkbox-open-in-new-window').addClass('d-none');

        // Reveals the form when all elements are in place
        finishLoading();
    }
    else {
        // document.onload runs before iframe is fully loaded
        // window.onload also runs before iframe is fully loaded
        // The best way to attach the event listener is to keep checking until
        // the specific "".note-editing-area" element is found
        setTimeout(summernoteInit, 1);
    }
}

/**
 * Checks if there is any text within the main body for the post to be valid
 */
function checkBodyValid() {
    let feedback = $('#summernote-feedback').get(0);
    feedback.setCustomValidity('Please fill out this field.');
    let iFrame = $('iframe').get(0);
    let contentField = iFrame.contentWindow.document.querySelector('.note-editing-area');
    if (contentField) {
        // Summernote uses HTML to display their text
        // We want to make sure there is some inner text within any of the elements
        // for the form to be valid
        let contentElements = contentField.children;
        for (let element of contentElements) {
            let text = element.innerText;
            text = text.trim();
            text = text.replace('\n', '');
            if (text !== '') {
                let textSpecialChars = text.replace(/[a-zA-Z0-9]/, '');
                if (text === textSpecialChars) {
                    feedback.setCustomValidity('Field must contain letters or numbers.');
                }
                else {
                    feedback.setCustomValidity('');
                }
            }
        }
    }
}


// Sets the poll answer input to valid if the checkbox is checked
$(document).ready(() => {
    updatePollCollapse();
    checkBodyValid();
    summernoteInit();
});