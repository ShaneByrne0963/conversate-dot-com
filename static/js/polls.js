$('#answers').on('input', checkAnswerInput);

/**
 * Validates an answer input, only enabling the "Add" button when there is an
 * answer that doesn't match any other existing answer
 */
function checkAnswerInput() {
    $('#add-answer').removeClass('disabled').removeAttr('disabled');
    let validInput = false;
    let answerInput = $('#answers').val();

    if (answerInput) {
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
        $('#add-answer').addClass('disabled').attr('disabled');
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
    $('#end-date').attr('min', dateValue).val(dateValue);
}

updateDueDate();