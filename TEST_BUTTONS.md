# Testing buttons and anchors for Conversate&#46;com

*Note*: All found issues stated below have been resolved. `Look out for code snippet
text to view found issues`

### The Login Page

- **The "Sign up here" link**
  - Expected Result: The user is taken to the signup page
  - Result: Works as intended
- **The "Log In" button**
  - Expected result: The user is taken to the home page
  - Result: Works as intended

### The Signup Page

- **The "Log in here" link**
  - Expected Result: The user is taken to the login page
  - Result: Works as intended
- **The "Create Account" button**
  - Expected result: An account with the filled in details is created and the
user is taken to the home page
  - Result: Works as intended

### The Base Template

- **The Conversate Logo**
  - Expected Result: The user is taken to the home page
  - Result: Works as intended
- **The "New Post" icon**
  - Expected Result: The user is taken to the "New Post" page
  - Result: Works as intended
- **The "New Poll" icon**
  - Expected Result: The user is taken to the "New Poll" page
  - Result: Works as intended
- **The username dropdown**
  - Expected Result: A dropdown menu appears with the options "Account Settings"
and "Log out"
  - Result: Works as intended
- **The "Account Settings" option**
  - Expected Result: The user is taken to the "Account Settings" page
  - Result: Works as intended
- **The "Log out" option**
  - Expected Result: A modal appears in front of the screen, asking the user to
confirm they wish to log out
  - Result: Works as intended
- **The search bar**
  - Expected Result: A popup appears under the search bar telling the user how
to search by tag
  - Result: Works as intended
- **The search hint dismiss button**
  - Expected result: The search himt button is dismissed
  - Result: Works as intended
- **The search button**
  - Expected Result: The user is taken to the "Post list" page, with posts
filtered by the query the user entered
  - Result: Works as intended
- **The post sort buttons, in a post list page**
  - Expected Result: The page refreshes, ordering the posts by the user's choice
  - Result: Works as intended
- **The post sort buttons, not in a post list page**
  - Expected Result: The buttons are disabled and cannot be clicked
  - Result: Works as intended
- **The home page navigation button**
  - Expected Result: The user is taken to the home page
  - Result: Works as intended
- **The category navigation dropdown**
  - Expected result: A collapse is toggled, revealing a list of categories
  - Result: `Works as intended, but for screens with a smaller height, the
dropdown causes the main screen to overflow. This creates two scrollbars that
are side-by-side, which can cause confusion. To fix this, I will reduce the
maximum number of categories that can be shown in the dropdown from 6 to 4`
- **The category button**
  - Expected result: The user is presented with a list of posts that contain
the selected category
  - Result: Works as intended
- **The "Browse Categories" button**
  - Expected result: The user is taken to the "Browse Categories" page
  - Result: Works as intended
- **The poll navigation dropdown**
  - Expected result: A collapse is toggled, revealing the pages "Open Polls",
"Closed Polls", and "My Polls"
  - Result: Works as intended
- **The "Open Polls" button**
  - Expected result: The user is taken to the poll list page, with posts
filtered by if the due date has not been reached
  - Result: Works as intended
- **The "Closed Polls" button**
  - Expected result: The user is taken to the poll list page, with posts
filtered by if the due date has been reached
  - Result: Works as intended
- **The alert message dismiss**
  - Expected result: The message is dismissed
  - Result: Works as intended

### The Post List Page

- **The post title**
  - Expected result: The user is taken to the post's full details in the
"Post Details" page
  - Result: Works as intended
- **The post category**
  - Expected result: The user is taken to another post list page, where they
can find a list of all posts within that category
  - Result: Works as intended
- **The post body preview**
  - Expected result: The user is taken to the post's full details in the
"Post Details" page
  - Result: Works as intended
- **The "Read More" anchor under long post bodies**
  - Expected result: The user is taken to the post's full details in the
"Post Details" page
  - Result: Works as intended
- **The post's tags**
  - Expected result: The user is taken to another post list page, where they
can find a list of all posts containing that tag
  - Result: Works as intended

### The Post Details Page

- **The post category**
  - Expected result: The user is taken to another post list page, where they
can find a list of all posts within that category
  - Result: Works as intended
- **Any links within the post's body**
  - Expected result: The user is taken to the link in a new tab
  - Result: `When creating a link, the user has an option to open the link in
a different tab or within the same tab. However, we want all outside links to
always open in a different tab, as this is a good UX practice, so I will remove
the checkbox using CSS to force all links to open in a new tab`
- **A poll answer radio button**
  - Expected result: The vote is selected and all other votes are deselected
  - Result: `Works as intended, but the user has to click on the radio button
or on the answer text itself, whereas if they click within any of the empty
parts of the container, nothing happens. This can cause frustration if the
user is trying to select the vote by clicking on the container, with no
feedback being given.`
- **The poll vote button**
  - Expected result: The vote is sent, the current results of the vote are
displayed to the user and the user cannot vote again
  - Result: Works as intended
- **The clear answer button**
  - Expected result: The selected answer in the vote becomes deselected
  - Result: Works as intended
- **The Edit Poll" button**
  - Expected result: The poll's due date is replaced by an inline form, with a
date input, a "Save" button and a "Cancel" button
  - Result: Works as intended
- **The "Save Poll" button**
  - Expected result: The poll's due date is updated
  - Result: Works as intended
- **The poll cancel edit button**
  - Expected result: The inline form disappears, and is replaced by the original
due date
  - Result: Works as intended
- **The "Delete Poll" button**
  - Expected result: A modal appears, requesting confirmation to delete the poll
  - Result: Works as intended
- **The post's tags**
  - Expected result: The user is taken to another post list page, where they
can find a list of all posts containing that tag
  - Result: Works as intended
- **The post like button, in a post not owned by the user**
  - Expected result: The user "likes"/"unlikes" the post, depending on if they
had previously liked the post or not. The number of likes on the post
increases/decreases by 1
  - Result: Works as intended
- **The post like button, in a post owned by the user**
  - Expected result: The interactivity of the button is removed, but still shows
the poster the number of likes on the page
  - Result: Works as intended
- **The comment button**
  - Expected result: The text area to send a comment is focused on
  - Result: Works as intended
- **The post edit button**
  - Expected result: This button should only exist if the user owns the post,
and takes the user to the "Edit Post" page
  - Result: Works as intended
- **The post delete button**
  - Expected result: This button should only exist if the user owns the post,
and causes a modal to appear asking for confirmation to delete the post
  - Result: Works as intended
- **The "Send Comment" button**
  - Expected result: The user's comment is sent to the post, and sits at the top
of the comments section
  - Result: Works as intended
- **The "Clear Comment" button**
  - Expected result: All the text the user entered in the comment input is deleted
  - Result: Works as intended
- **The "Like Comment" button, for a comment not owned by the user**
  - Expected result: The user "likes"/"unlikes" the comment, depending on if they
had previously liked the comment or not. The number of likes on the comment
increases/decreases by 1
  - Result: Works as intended
- **The reply button in the comment footer**
  - Expected result: A reply textarea appears under the comment footer, with a
"Reply" and "Cancel" button, and the textarea is focused on. For replies to replies,
the textarea is prefilled with "@<username>", ONLY if the person the user is
replying to is not the original commenter, or the user themselves
  - Result: `Works as intended, but multiple comment reply textareas can be
expanded at the same time, which can be confusing. I will add an accordion bootstrap
component to only allow one dropdown at a time`
- **The reply submit button**
  - Expected result: The reply is sent and is hidden within the comment reply
section
  - Result: Works as intended
- **The reply cancel button**
  - Expected result: The dropdown containing the reply form is hidden
  - Result: Works as intended
- **The comment edit button**
  - Expected result: The comment body is replaced by a textarea, with the
previous content pre-filled in. The post footer disappears, and is replaced
by 2 buttons: "Save" and "Cancel"
  - Result: Works as intended
- **The save comment button**
  - Expected result: The comment is updated, and is marked with "(Edited)"
  - Result: Works as intended
- **The cancel edit comment button**
  - Expected result: The textarea disappears, and is replaced with the
original comment layout
  - Result: Works as intended
- **The coment delete button**
  - Expected result: A modal appears, asking the user for confirmation if
they want to delete the comment
  - Result: Works as intended
- **View replies toggle**
  - Expected result: The reply section dropdown is toggled, and the text
changes to "View/Hide replies" depending on what is showing
  - Result: `Works as intended, but double-clicking on the button can cause
the text to go out of sync with the dropdown (i.e. the text says "Hide replies"
when the replies are hidden. I will change the text update event from the toggle
click to the Bootstrap collapse events`

### The New Post Page

- **The "Clear Image" button**
  - Expected Result: The image is cleared from the preview, and will not
persist after the post is created
  - Result: Works as intended
- **The "Add Tag" button**
  - Expected result: A tag is added to the list of tags
  - Result: Works as intended
- **The "Remove Tag" button**
  - Expected result: The tag is removed from the list of tags
  - Result: Works as intended
- **The "Include Poll" checkbox**
  - Expected result: If checked, the poll collapse shows, and if not, the poll
collapse hides
  - Result: Works as intended
- **The "Add Answer" button**
  - Expected result: The answer is added, and if the number of answers has
reached the maximum, the poll answer input disappears
  - Result: Works as intended
- **The "Delete Answer" button**
  - Expected result: The answer is removed, and if the previous number of
answers was the maximum, the poll answer input reappears
  - Result: Works as intended
- **The "Create Post" button**
  - Expected result: The post is created, with all the properties specified
by the user within the form
  - Result: Works as intended
- **The post form clear button**
  - Expected result: All data previously entered by the user is cleared
  - Result: `The content within the Summernote text editor remains, and even
though the "Include Poll" checkbox is unchecked, the collapse doesn't hide`

### The Edit Post Page

- **The "Clear Image" button**
  - Expected Result: If an image is already present before the edit, then a modal
will appear, asking the user for confirmation to delete the image. If not, then
the image is cleared from the preview, and will not persist after the post is
created
  - Result: Works as intended
- **The "Add Tag" button**
  - Expected result: A tag is added to the list of tags
  - Result: Works as intended
- **The "Remove Tag" button**
  - Expected result: The tag is removed from the list of tags
  - Result: Works as intended
- **The "Include Poll" checkbox**
  - Expected result: If checked, the poll collapse shows, and if not, the poll
collapse hides
  - Result: `Checkbox collapse always hides after showing`
- **The "Add Answer" button**
  - Expected result: The answer is added, and if the number of answers has
reached the maximum, the poll answer input disappears
  - Result: Works as intended
- **The "Delete Answer" button**
  - Expected result: The answer is removed, and if the previous number of
answers was the maximum, the poll answer input reappears
  - Result: Works as intended
- **The "Delete Poll" button**
  - Expected result: A modal appears asking the user for confirmation of the
poll delete
  - Result: Works as intended
- **The "Save Post" button**
  - Expected result: The post is updated, with all the properties specified
by the user within the form
  - Result: Works as intended
- **The "Cancel Edit" button**
  - Expected result: The user is taken back to the post detail page
  - Result: Works as intended

### The New Poll Page

- **The "Add Answer" button**
  - Expected result: The answer is added, and if the number of answers has
reached the maximum, the poll answer input disappears
  - Result: Works as intended
- **The "Delete Answer" button**
  - Expected result: The answer is removed, and if the previous number of
answers was the maximum, the poll answer input reappears
  - Result: Works as intended
- **The form clear button**
  - Expected result: All previously entered data is cleared
  - Result: `If the form is cleared with the maximum number of answers, the
answer input is missing`

### The Poll List Page

- **The poll's post reference**
  - Expected result: The user is taken to the post where the poll is referenced
  - Result: Works as intended
- **The "Delete Poll" button
  - Expected result: A modal appears, asking for confirmation to delete the poll
  - Result: Works as intended
- **The answer select input**
  - Expected result: The answer that resides in the clicked container is selected
  - Result: Works as intended
- **The poll vote button**
  - Expected result: The vote is sent, the current answers are shown and the user
cannot vote again
  - Result: Works as intended
- **The clear vote button**
  - Expected result: The selected vote is cleared
  - Result: Works as intended
- The "Edit Poll" button
  - Expected result: The poll's due date is replaced by an inline form, with a date
input, a "Save" button and a "Cancel" button
  - Result: Works as intended
- **The poll save button**
  - Expected result: The poll's due date is updated
  - Result: Works as intended
- **The cancel poll edit button**
  - Expected result: The inline form disappears, and is replaced by the original
due date
  - Result: Works as intended

### The Account Settings Page

- **The "Edit Username" button**
  - Expected result: A modal appears, requesting the user's password before allowing
the user to edit their settings
  - Result: Works as intended
- **The "Edit Email" button**
  - Expected result: A modal appears, requesting the user's password before allowing
the user to edit their settings
  - Result: Works as intended
- **The "Delete Account" button**
  - Expected result: A modal appears, requesting the user's password before allowing
the user to delete their account
  - Result: Works as intended

### The Edit Account Page

- **The password checkbox**
  - Expected result: A dropdown is toggled, revealing/hiding 2 password input fields
  - Result: Works as intended
- **The "Update Account" button**
  - Expected result: the account details are updated
  - Result: Works as intended
- **The cancel account edit button**
  - Expected result: The user is taken to the account settings page
  - Result: Works as intended

### Modals

- **The modal dismiss button**
  - Expected result: The modal is dismissed
  - Result: Works as intended
- **The modal cancel button**
  - Expected result: The modal is dismissed
  - Result: Works as intended
- **The user logout modal**
  - Expected result: The user is logged out and is taken to the login page
  - Result: Works as intended
- **The post delete modal**
  - Expected result: The selected modal is deleted
  - Result: Works as intended
- **The comment delete modal**
  - Expected result: The selected comment is deleted
  - Result: Works as intended
- **The poll delete modal**
  - Expected result: The selected poll is deleted
  - Result: Works as intended
- **The clear image modal**
  - Expected result: The image is removed from the post
  - Result: Works as intended
- **The "Edit Account" modal**
  - Expected result: the user is taken to the edit account page
  - Result: Works as intended
- **The "Delete Account" modal**
  - Expected result: The user's account is deleted, and is taken to the
login page
  - Result: Works as intended

### Non-Authenticated Users

- **The login button**
  - Expected result: The user is taken to the login page
  - Result: Works as intended
- **Links within the post body**
  - Expected result: Should still open the links in a new tab
  - Result: Works as intended
- **The poll vote button**
  - Expected result: No radio inputs appear, the results are not shown if the
due date hasn't been reached, and the vote button has been replaced with text
that says "Please log in to vote"
  - Result: `The radio buttons are present, and the user can send a vote, which
causes a 500 error. This check was not implemented during the development phase,
so I will add a check for this`
- **The post/comment like buttons**
  - Expected result: The buttons are disabled, and the number of likes is shown
  - Result: Works as intended
- **The post comment button**
  - Expected result: The comments section is focused on
  - Result: Works as intended
- **The comment reply buttons**
  - Expected result: The buttons should not exist in the comment footer
  - Result: `The comment buttons are not there, but the line separator that
divides the like button and comment button is still there, which looks
strange with the like button by itself. I will remove this for this case`
- **The "View Replies" button under comments with replies**
  - Expected result: Should work the same as if the user was authenticated
  - Result: Works as intended
- **All other links**
  - Expected result: The user is taken to the login page
  - Result: `The post tag buttons produce a server 500 error`