const maxAnswers = 5;

// Answer validation
$('#answers').on('input', checkAnswerInput);

// Adding the answer to the list
$('#add-answer').click(addAnswer);

/**
 * Validates an answer input, only enabling the "Add" button when there is an
 * answer that doesn't match any other existing answer
 */
function checkAnswerInput() {
    $('#add-answer').removeClass('disabled').removeAttr('disabled');
    $('#answers').removeClass('is-invalid');
    $('#answer-feedback').removeClass('d-block');
    let validInput = false;
    let answerInput = $('#answers').val();
    console.log('Here');

    if (answerInput && $('.answer').length < maxAnswers) {
        validInput = true;
        let existingAnswers = $('.answer-text').get();
        for (let answer of existingAnswers) {
            if (answerInput == answer.innerText) {
                validInput = false;
                $('#answers').addClass('is-invalid');
                $('#answer-feedback').addClass('d-block');
                break;
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
    let answerInput = $('#answers').val();
    let currentAnswers = $('#answer-list').html();
    let numAnswers = $('.answer').length + 1;
    currentAnswers += `
        <li class="answer list-group-item">
            <input type="hidden" name="answer-${numAnswers}" value="${answerInput}" aria-hidden="true">
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
    event.target.parentNode.parentNode.remove();

    if ($('.answer').length < 2) {
        setValidAnswers(false);
    }
    // If the max number of answers existed, now there is space to add another
    $('#answer-input').removeClass('d-none');
}


/**
 * 
 * @param {Boolean} value If there are at least 2 answers
 */
function setValidAnswers(value) {
    let feedback = (value) ? '' : 'Need at least 2 answers.';
    $('#answers').get(0).setCustomValidity(feedback);
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
    $('#end-date').attr('min', dateValue).val(dateValue);
}

updateDueDate();
setValidAnswers(false);