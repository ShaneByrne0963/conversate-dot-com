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