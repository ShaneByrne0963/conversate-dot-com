// Adds a tag entered by the user to the list of tags
$('#add-tag').click((event) => {
    event.preventDefault();
    let tagName = $('#tag').val();
    let tagElement = document.createElement('div');
    tagElement.className = 'tag-list-item mr-2 mb-2';
    tagElement.innerHTML = `
    <div class="d-flex align-items-center justify-space-between p-1">
        <em class="tag-name">#${tagName}</em>
        <button type="button" class="close ml-2 mr-1" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>
    </div>
    `;
    $('#tags-list').append(tagElement);
    $('#tag').val('');
    console.log($('.tag-name').text());
});