# Testing for Conversate&#46;com

*Note*: All found issues stated below have been resolved

## Part 1 - Testing links

### The Login Page

- **The "Sign up here" link**
  - Expected Result: The user is taken to the signup page
  - Result: Works as intended
- **The "Log In" button, with valid information filled in**
  - Expected result: The user is taken to the home page
  - Result: Works as intended

### The Signup Page

- **The "Log in here" link**
  - Expected Result: The user is taken to the login page
  - Result: Works as intended
- **The "Create Account" button, with valid information filled in**
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
- **The search button, with valid information filled in**
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
  - Result: Works as intended
- **The category button**
  - Expected result: The user is presented with a list of posts that contain
the selected category
  - Result: Works as intended
- **The "Browse Categories" button**
  - Expected result: The user is taken to the "Browse Categories" page
  - Result: Works as intended
- **The poll navigation dropdown**
  - Expected result: 

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

## Part 3 - Direct URL Inputs
