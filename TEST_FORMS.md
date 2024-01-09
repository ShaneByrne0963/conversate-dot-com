*Note*: All found issues stated below have been resolved. `Look out for code snippet
text to view found issues`

## The Login Page

- **Any required inputs not filled in**
  - Expected result: A feedback message pops up asking the user to fill in the
required fields
  - Result: Works as intended
- **Incorrect information filled in**
  - Expected result: The user remains on the login page, and a message notifying
the user that their details are incorrect appears
  - Result: Works as intended

## The Signup Page

- **Any required inputs not filled in**
  - Expected result: A feedback message pops up asking the user to fill in the
required fields
  - Result: Works as intended
- **Username longer than 30 characters**
  - Expected result: The user cannot enter any text longer than 30 characters
  - Result: Works as intended
- **Disallowed characters in username field**
  - Expected result: An error message appears, telling the user they cannot enter
these characters
  - Result: Works as intended
- **Already existing username**
  - Expected result: The user is given feedback through an error message
  - Result: Works as intended
- **Passwords shorter than 8 characters**
  - Expected result: The user is given feedback through an error message
  - Result: Works as intended
- **Commonly used password**
  - Expected result: The user is given feedback through an error message
  - Result: Works as intended
- **Non-matching passwords**
  - Expected result: The user is given feedback through an error message
  - Result: Works as intended

## The Search Bar

- **No search query given**
- Expected result: A feedback message pops up asking the user to fill in the
required fields
  - Result: Works as intended
- **Spaces only query given**
- Expected result: A feedback message pops up asking the user to fill in the
required fields
  - Result: Works as intended
- **Query starts with a hashtag**
  - Expected result: Every word, separated by a space, is determined as a tag,
and the user is taken to a post list page with all posts containing any of
those tags
  - Result: `If the user enters multiple spaces, this adds blank tags, which
results in all posts being filtered`
- **Empty hashtag query**
  - Expected result: A feedback message pops up asking the user to fill in the
required fields
  - Result: `An error is thrown`
- **Hashtag query contains special characters**
  - Expected result: All special characters are removed from the search
  - Result: Works as intended

## The Post Comment/Comment Reply Form

- **No input**
  - Expected result: A feedback message pops up asking the user to fill in the
required fields
  - Result: Works as intended
- **Spaces only input**
  - Expected result: A feedback message pops up asking the user to fill in the
required fields
  - Result: Works as intended
- **Special characters only input**
  - Expected result: A feedback message pops up asking the user to use letters
or numbers
  - Result: Works as intended

## Polls

- **Vote on a poll without any votes selected**
  - Expected result: A feedback message appears, telling the user they have to
select one of the options
  - Result: Works as intended
- **Edit a poll without selecting a new due date**
  - Expected result: A feedback message pops up asking the user to fill in the
required fields
  - Result: Works as intended

## The Create/Edit Post Page

- **Any required inputs not filled in**
  - Expected result: A feedback message pops up asking the user to fill in the
required fields
  - Result: Works as intended
- **Spaces only title**
  - Expected result: A feedback message pops up asking the user to fill in the
required fields
  - Result: Works as intended
- **Special characters only title**
  - Expected result: A feedback message pops up asking the user to use letters
or numbers
  - Result: Works as intended
- **Spaces only body**
  - Expected result: A feedback message pops up asking the user to fill in the
required fields
  - Result: Works as intended
- **Special characters only body**
  - Expected result: A feedback message pops up asking the user to use letters
or numbers
  - Result: Works as intended
- **Upload file that is not image**
  - Expected result: The image field turns red with a feedback message stating
the uploaded file must be an image
  - Result: Works as intended
- **Tags with disallowed characters**
  - Expected result: The tag field turns red with a feedback message stating
that no special characters other than "_" and "-" are allowed
  - REsult: Works as intended
- **Tags that are the same as previously entered tags**
  - Expected result: The tag field turns red with a feedback message stating
that no two tags can be the same in a post
  - Result: Works as intended

## The Create Poll Page

All these tests were performed on the new/edit post pages with the same results

- **Any required inputs not filled in**
  - Expected result: A feedback message pops up asking the user to fill in the
required fields
  - Result: Works as intended
- **Spaces only poll title**
  - Expected result: A feedback message pops up asking the user to fill in the
required fields
  - Result: Works as intended
- **Special characters only poll title**
  - Expected result: A feedback message pops up asking the user to use letters
or numbers
  - Result: Works as intended
- **Spaces only poll answer**
  - Expected result: The poll answer field turns red with a feedback message stating
that the field is required
  - Result: Works as intended
- **Special characters only poll answer**
  - Expected result: The poll answer field turns red with a feedback message
asking the user to use letters or numbers
  - Result: Works as intended
- **The same poll answer entered twice**
  - Expected result: The poll answer field turns red with a feedback message stating
that two answers cannot be the same
  - Result: Works as intended
- **Less than 2 poll answers on submit**
  - Expected result: A feedback message pops up asking the user to add more answers
  - Result: `The user can create a poll with only 1 answer. This was checked before
but is now overridden by the text validation`

## The Account Settings Password Modal

- **Any required inputs not filled in**
  - Expected result: A feedback message pops up asking the user to fill in the
required fields
  - Result: Works as intended
- **Incorrect password entered**
  - Expected result: An alert message appears telling the user their password was
incorrect
  - Result: `The alert message doesn't appear for the "Delete Account" button`

## The Edit Account Page

- **Invalid username (Same requirements as Signup Page)**
  - Expected result: An alert message appears telling the user their new
username was invalid
  - Result: `This happens, but the username is updated and applied for the
current page`
- **Invalid Passwords (Same requirements as Signup Page)**
  - Expected result: An alert message appears telling the user their new
password was invalid
  - Result: Works as intended