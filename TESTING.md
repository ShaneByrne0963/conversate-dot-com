# Testing for Conversate&#46;com

*Note*: All found issues stated below have been resolved

## Part 1 - Testing links

This section assumes all information is valid when forms are submitted. See
Part 2 for form input checks

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
  - Expected result: The user is taken to the link
  - Result: Works as intended
- **A poll answer radio button**
  - Expected result: The vote is selected and all other votes are deselected
  - Result: `Works as intended, but the user has to click on the radio button
or on the answer text itself, whereas if they click within any of the empty
parts of the container, nothing happens. This can cause frustration if the
user is trying to select the vote by clicking on the container, with no
feedback being given.`
- **The poll vote button**
  - Expected result: The 
- **The clear answer button**
  - Expected result: The selected answer in the vote becomes deselected
  - Result: Works as intended
- **The post's tags**
  - Expected result: The user is taken to another post list page, where they
can find a list of all posts containing that tag
  - Result: Works as intended
- **The post like button, in a post not owned by the user
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
- The "Send Comment" button
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

### Non-Authenticated Users

- **The login button**
  - Expected result: The user is taken to the login page
  - Result: Works as intended
- **Links within the post body**
  - Expected result: Should still open the links
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
  - Result: `The following links produced unintended results:`
    - The post tag: Produces a server 500 error

## Part 2 - Testing Form Data

- **The "Log In" button, with no inputs filled in**
  - Expected Result: A feedback message pops up asking the user to fill in the
username field
  - Result: Works as intended
- **The "Log In" button, with only the username field filled in**
  - Expected Result: A feedback message pops up asking the user to fill in the
password field
  - Result: Works as intended
- **The "Log In" button, with only the password field filled in**
  - Expected Result: A feedback message pops up asking the user to fill in the
username field
  - Result: Works as intended
- **The "Log In" button, with incorrect information filled in**
  - Expected result: The user remains on the login page, and a message notifying
the user that their details are incorrect appears
  - Result: Works as intended
- **The "My Polls" button**
  - Expected result: The user is taken to the poll list page, where they can find
a list of all the polls they have created
  - Result: Works as intended

- **The poll vote button, without any votes selected**
  - Expected result: A feedback message appears, telling the user they have to
select one of the options
  - Result: Works as intended
- The "Send Comment" button, without any text entered
  - Expected result: A feedback message appears, requesting the user to fill out
the comment field
  - Result: Works as intended
- The "Send Comment" button, with only white space "  " entered
  - Expected result: A feedback message appears, requesting the user to fill out
the comment field
  - Result: `The user is able to send comments that are blank by using the space
bar. I will add a check for this`
- The "Send Comment" button, only containing symbols
  - Expected result: A feedback message appears, requesting the user to enter a
message that contains letters or numbers
  - Result: `The user can enter comments that don't contain any letters or numbers.
I will add a fix for this`

## Part 3 - Direct URL Inputs