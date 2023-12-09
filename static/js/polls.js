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
    let validInput = false;
    let answerInput = $('#answers').val();

    if (answerInput && $('.answer').length < maxAnswers) {
        validInput = true;
        let existingAnswers = $('.answer').get();
        for (let answer of existingAnswers) {
            if (answerInput == answer.innerText) {
                validInput = false;
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
    currentAnswers += `
        <li class="answer list-group-item">
            <span>${answerInput}</span>
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
}


function removeAnswer(event) {
    event.target.parentNode.parentNode.remove();
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