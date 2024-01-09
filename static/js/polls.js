const maxAnswers = 5;

/**
 * Validates an answer input, only enabling the "Add" button when there is an
 * answer that doesn't match any other existing answer
 */
function checkAnswerInput() {
    $('#add-answer').removeClass('disabled').removeAttr('disabled');
    $('#answers').removeClass('is-invalid');
    $('#answer-feedback').removeClass('d-block');
    let validInput = false;
    let errorMessage = validateText('#answers');

    let answerInput = $('#answers').val();
    if (answerInput) {
        if (errorMessage) {
            $('#answers').addClass('is-invalid');
            $('#answer-feedback').addClass('d-block');
            $('#answer-feedback').text(errorMessage);
        }
        else if ($('.answer').length < maxAnswers) {
            validInput = true;
            let existingAnswers = $('.answer-text').get();
            for (let answer of existingAnswers) {
                if (answerInput == answer.innerText) {
                    validInput = false;
                    $('#answers').addClass('is-invalid');
                    $('#answer-feedback').addClass('d-block');
                    $('#answer-feedback').text('You have already entered this answer.');
                    break;
                }
            }
        }
    }
    if (!validInput) {
        $('#add-answer').addClass('disabled').attr('disabled', true);
    }
}


/**
 * Adds the entered answer to the list of answers
 */
function addAnswer() {
    let answerInput = $('#answers').val().trim();
    let currentAnswers = $('#answer-list').html();
    let numAnswers = $('.answer').length + 1;
    currentAnswers += `
        <li class="answer list-group-item">
            <input type="hidden" class="answer-val" name="answer-${numAnswers}" value="${answerInput}" aria-hidden="true">
            <span class="answer-text">${answerInput}</span>
            <button type="button" class="close" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </li>
    `;
    $('#answer-list').html(currentAnswers);
    $('#answers').val('');
    $('#add-answer').addClass('disabled').attr('disabled', true);
    
    // Removing all event listeners and re-adding them to avoid duplicates
    $('.close').unbind('click').click(removeAnswer);

    // Making this part of the form valid if there are 2 or more answers
    if (numAnswers >= 2) {
        setValidAnswers(true);

        // Removing the add answer input from the view once all answers have been given
        if (numAnswers >= maxAnswers) {
            $('#answer-input').addClass('d-none');
        }
    }
}


/**
 * Deletes a poll answer
 * @param {Event} event The triggered event
 */
function removeAnswer(event) {
    let parentElement = event.target.parentNode.parentNode;

    // Getting the position of the deleting element, because answers are ordered
    let position = parentElement.querySelector('.answer-val').getAttribute('name');
    let numPosition = getNumbersFromString(position);
    parentElement.remove();

    // Making sure all positions are incremental (1, 2, 3...) with no gaps
    let existingAnswers = document.getElementsByClassName('answer');
    for (let answer of existingAnswers) {
        let valueInput = answer.querySelector('.answer-val');
        let newNumPos = getNumbersFromString(valueInput.getAttribute('name'));
        if (newNumPos > numPosition) {
            newNumPos--;
            valueInput.setAttribute('name', `answer-${newNumPos}`);
        }
    }
    checkEnoughAnswers();
    // If the max number of answers existed, now there is space to add another
    $('#answer-input').removeClass('d-none');
}


/**
 * Makes the answer input invalid if there are less than 2 answers given
 */
function checkEnoughAnswers() {
    setValidAnswers($('.answer').length >= 2);
}


/**
 * Sets the answer input's validity, preventing the form from submitting if invalid
 * @param {Boolean} value If the answer input is valid
 */
function setValidAnswers(value) {
    let feedback = (value) ? '' : 'Need at least 2 answers.';
    if ($('#answers').length > 0) {
        $('#answers').get(0).setCustomValidity(feedback);
    }
}


/**
 * Updates the value of the due date to be the next day
 */
function updateDueDate() {
    // The minimum due by date is the next day
    let dueDate = new Date(Date.now() + (1000 * 60 * 60 * 24));
    let dueMonth = `${dueDate.getMonth() + 1}`.padStart(2, '0');
    let dueDay = `${dueDate.getDate()}`.padStart(2, '0');
    let dateValue = `${dueDate.getFullYear()}-${dueMonth}-${dueDay}`;
    $('.poll-date-input').attr('min', dateValue).val(dateValue);
}


/**
 * Extracts digits from a string and converts them into an integer
 * @param {String} myString The string to extract numbers from
 * @returns {Integer} All numbers found in the string
 */
function getNumbersFromString(myString) {
    return parseInt(myString.match(/[0-9]/)[0]);
}

$(document).ready(() => {
    // Answer validation
    $('#answers').on('input', checkAnswerInput);

    // Adding the answer to the list
    $('#add-answer').click(addAnswer);

    // Is called when the user resets the form
    $('.create-form').on('reset', () => {
        $('.answer').remove();
        setValidAnswers(false);
        // The timeout prevents the form clear from overriding the preset
        setTimeout(updateDueDate, 1);
    });

    // Allows the due date to be edited
    $('.btn-edit-poll').click(function() {
        updateDueDate();
        let parentNode = $(this).parent().parent().parent();
        $(parentNode).find('.poll-edit-form').removeClass('d-none');
        $(parentNode).find('.poll-date-display').removeClass('d-none').addClass('d-none');
    });

    $('.poll-edit-cancel').click(function () {
        let parentNode = $(this).parent().parent().parent().parent();
        $(parentNode).find('.poll-edit-form').removeClass('d-none').addClass('d-none');
        $(parentNode).find('.poll-date-display').removeClass('d-none');
    });

    updateDueDate();
    setValidAnswers(false);
    if ($('#poll-form').length > 0) {
        finishLoading();
    }
});