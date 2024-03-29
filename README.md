# Conversate&#46;com

## Introduction

Conversate&#46;com is a forum website where people can connect with each other
by writing posts, uploading images and creating polls for other people to vote
on. The aim of this website is to provide a platform that gives its users a
wide range of ways to express their thoughts and opinions, as well as making
those expressions as accessible to other users as possible. Conversate was made
using the Django framework and designed using Bootstrap

![The Conversate home page](assets/images/design/user_interface/main.JPG)

## Design Thinking Process

> *"Why would a user want to visit our website?"*

- To discover information easily and efficiently
- To share their information with the world
- To interact with a community that relates to them

> *"How do we want our users to feel while using our website?"*

- Encouraged to interact with the community

### Problem Statement

> *"How can we make information easy to share and access for everyone?"*

### Solutions

> *"Why would a user want to visit our website?"*

- **To discover information easily and efficiently**
  - Upon logging in to the site, users are introduced to the site's home page,
where they can explore a wide range of posts the site has to offer. Having
every kind of post available on the home page can help newcomers who are unsure
about what they are looking for discover the kind of content that best suits
them.
  - If users are looking for something a little more specific, they have an
option to search for posts using keywords.
  - Posts can be sorted by "Popular" (Highest number of likes) or "New"
(Most recently posted)
- **To share their information with the world**
  - Users can create posts, upload images and ask questions through the use
of polls.
  - Posts can be customized using a wide selection of styles, allowing the
creators to add headings, divide their content into paragraphs, include lists,
and add links to other pages.
- **To interact with a community that relates to them**
  - Posts can have a category assigned to them. Users that are searching for a
particular type of post can explore these categories and discover a community
that is also interested in this topic.

> *"How do we want our users to feel while using our website?"*

- **Encouraged to interact with the community**
  - Users are required to be logged in to navigate through the majority of the
website, which means if they discover a post that interests them they will
always have the opportunity to like and comment on that post, as well as vote
in polls they discover. The only thing that non-authenticated users can see is
any full post, which allows users to share posts with non-users, in the hopes
of getting them to join in on the conversation.

## Features

<details><summary><strong>Posts</strong></summary><ul>
<li>Posts are the main attraction to Conversate. They are blocks of text
created by users to send their thoughts out to the world for all to see.<br>
<img src="assets/images/features/post_content.JPG" alt="A user post"></li>
<li>All posts are made up of a title and a main body of text. The site uses
Summernote's text editor to give users the ability to add style to their posts.
They can add headings, paragraphs, bullet points, links and horizontal rules.
Text can also be styled in a number of ways, including changing the font size
and setting the font to bold, italics or underlined<br>
<img src="assets/images/features/post_styled.JPG" alt="A post using different styles of text"></li>
<li>Categories can be added to a post in order to group it with other posts of
a similar nature. There are a selection of categories created by the site
administrators that can be chosen from</li>
<li>Images can also be added to a post. A picture is worth a thousand words,
so adding one can add an invaluable layer of depth to the story the poster is
trying to tell. Images can be placed above or below the main body of text<br>
<img src="assets/images/features/post_image.JPG" alt="A post with an image at the top"></li>
<li>Posts can be tagged with a list of keywords. These tags can be clicked on,
revealing all posts that also have this tag. Using hashtags can increase the
likelihood of the post to be seen, as it provides an extra method for posts to
be queried</li>
<li>Users can choose to like posts to show appreciation to the poster. Posts
with more likes are more likely to be found by exploring users. Posters
cannot like their own posts<br>
<img src="assets/images/features/post_tags.JPG" alt="A list of keywords tagging the post"></li>
</ul></details>

<details><summary><strong>Comments</strong></summary><ul>
<li>Users can comment on posts to share thoughts or add insight of their own</li>
<li>If a user sees a comment they appreciate, they can like that comment<br>
<img src="assets/images/features/comment.JPG" alt="A comment left under a post"></li>
<li>Comments can also be replied to so that a conversation can be started with the
commenter. Replies can be replied to in a similar manner<br>
<img src="assets/images/features/comment_replies.JPG" alt="A conversation within the comments">
</li></ul></details>

<details><summary><strong>Polls</strong></summary><ul>
<li>Polls are an excellent way to collect answers and gather statistics from the site's community.
They are made up of a question (title), a list of between 2 and 5 answers, and an end date.<br>
<img src="assets/images/features/poll.JPG" alt="A user submitted poll"></li>
<li>Polls can be included within a post, giving the user the ability to add more context to the
poll, as well as allowing people to respond in the comments<br>
<img src="assets/images/features/poll_post.JPG" alt="A poll that is part of a post"></li>
<li>Users can only vote for one answer in the list, and once they vote on their decision, they are
unable to change their vote</li>
<li>Answers from other users cannot be seen until the user has voted, in order to prevent people
from only selecting the most popular vote<br>
<img src="assets/images/features/poll_voted.JPG" alt="A poll that has revealed its answers after a vote"></li>
<li>Once a poll has passed its due date, votes will no longer be accepted and the final results
will be shown<br>
<img src="assets/images/features/poll_ended.JPG" alt="A poll that has ended">
</li></ul></details>

<details><summary><strong>The Home Page</strong></summary><ul>
<li>When the user first logs in to Conversate, the home page is the first step on their journey.</li>
<li>They are welcomed with any possible kind of post made on the site, allowing them to explore
a wide variety of content until they find something that interests them.<br>
<img src="assets/images/features/home_page.JPG" alt="The home page">
</li></ul></details>

<details><summary><strong>Categories</strong></summary><ul>
<li>If users are looking for something a little more specific, they can search for
posts by what category they belong to.</li>
<li>A list of categories is present within the navigation that shows the categories
with the most posts, making more content easily available to the user<br>
<img src="assets/images/features/category_navigation.JPG" alt="A list of categories available from the navigation">
<img src="assets/images/features/category_search.JPG" alt="Results for searching by category">
</li></ul></details>

<details><summary><strong>Search Posts</strong></summary><ul>
<li>For users that are specifically looking for posts that contain certain words or
phrases, they can use the search bar and find those posts<br>
<img src="assets/images/features/search_bar.JPG" alt="Searching for posts with the word 'chocolate' in the search bar">
<img src="assets/images/features/search_results.JPG" alt="The results found 2 posts with the word 'chocolate'"></li>
<li>Users also have the option to search for post tags by prefixing their search with a hashtag ("#")<br>
<img src="assets/images/features/search_tags.JPG" alt="Searching for posts with the tag 'Alps'">
<img src="assets/images/features/search_tag_results.JPG" alt="The results found 2 posts tagged with 'Alps'"></li>
</li></ul></details>

<details><summary><strong>"My Posts"</strong></summary><ul>
<li>Users can easily jump to their created posts to monitor interactions by clicking
on the "My Posts" button within the navigation<br>
<img src="assets/images/features/my_posts.JPG" alt="All the user's posts in one place">
</li></ul></details>

<details><summary><strong>Filter Posts by Likes/Newest</strong></summary><ul>
<li>All of the above methods of finding posts can have the results of those queries
sorted by "Popular" or "New", first displaying the posts with the highest number of
likes or posts that were most recently created, respectively<br>
<img src="assets/images/features/post_sort.JPG" alt="Buttons to sort the selection of posts, with 'Popular' being selected">
<img src="assets/images/features/post_sort_results.JPG" alt="Posts with the highest number of likes are shown as a result">
</li></ul></details>

<details><summary><strong>Browse Polls</strong></summary><ul>
<li>Along with posts, users can also browse through and vote on polls, made
easy through the use of the "Polls" navigation tab</li>
<li>Here, polls are divided into 3 categories:<ul>
  <li>Open polls, where users can engage with polls and contribute their opinion
  to the overall score</li>
  <li>Closed polls, if the user feels like gathering information about votes that
  occured in the past</li>
  <li>"My polls", which is a place for the user to find the answers to all their
  asked questions</li></ul></li>
<li>Posts as part of polls are included, with a link to the post so the user can
get the full context of the poll, as well as engage with the comments<br>
<img src="assets/images/features/poll_navigation.JPG" alt="The poll dropdown in the navigation">
<img src="assets/images/features/poll_list.JPG" alt="A list of open polls">
</li></ul></details>

## Design

### User Interface

<details><summary><strong>The Login/Signup Page</strong></summary><ul>
<li>This is where the site users begin their journey. Compared to the rest of the site, the layout for these pages is simple, with the Conversate brand logo on the left, the form to log in/sign up on the right, a navbar with the logo on top and a simple post footer at the bottom to mark the end of the page</li>
<li>I wanted these pages to be minimalistic prevent any distractions from the main action of these pages, which is to log in/sign up to the website</li></ul>
<img src="assets/images/design/user_interface/login.jpg" alt="The login page">
<img src="assets/images/design/user_interface/signup.JPG" alt="The signup page">
</details>

<details><summary><strong>The Main User Interface</strong></summary>
<p>Apart from the login and signup pages, all other pages use the same user interface to maintain consistency and prevent confusion among users when navigating the site</p>
<img src="assets/images/design/user_interface/main.JPG" alt="The main user interface">
The user interface is made up of 2 components:<ul>
    <li><strong>The top navigation</strong>
    <ul>
        <li>This part holds the Converate brand logo on its left, a place where users would expect to find it</li>
        <li>Its main purpose is to contain the user action buttons, such as creating posts, creating polls and managing user settings. These are grouped together on the right hand side of the screen
        <img src="assets/images/design/user_interface/navigation_top.JPG" alt="The top navigation"></li>
        <li>If the user hovers over the create post or create poll icon, they will expand revealing a label that signifies their purpose. This helps new users in understanding the functions of these buttons<br>
        <img src="assets/images/design/user_interface/icon_expanded.JPG" alt="The create post icon expanded"></li>
    </ul></li>
    <li><strong>The side navigation</strong><br>
    <ul>
        <li>This part is responsible for the site navigation. It includes a search bar, an option to sort posts by popular/new, and links to the home page, post categories, polls and user-owned posts<br>
        <img src="assets/images/design/user_interface/navigation_side.JPG" alt="The side navigation"></li>
    </ul></li>
    <li>For mobile screens, due to space constraints, the side navigation is hidden, and a collapse icon appears beside the logo. When clicked, this icon expands the side navigation over the main content, allowing it to be visible only when the user wants it to be<br>
    <img src="assets/images/design/user_interface/navigation_collapse.JPG" alt="The side navigation expanded over the main content"></li>
    <li>All components of the user interface have fixed positions, which gets rid of the annoyance of the user having to scroll to the top to continue to navigate the site<br>
    <img src="assets/images/design/user_interface/navigation_scroll.JPG" alt="The side navigation stays in the same place when scrolling"></li>
</ul>
</details>

<details><summary><strong>The Search Bar</strong></summary><ul>
    <li>The design of the search bar is nothing new, only consisting of a search text input and a button to trigger the search. Most users will recognise this layout and be able to use it intuitively<br>
    <img src="assets/images/features/search_bar.JPG" alt="The search bar"></li>
    <li>The search bar also has a function to search posts by tags by prefixing the search with a hashtag ("#"). This is explained to the user with a popup alert below the search bar when the user attempts to type something in it. This only appears once per session to prevent it from becoming an annoying popup<br>
    <img src="assets/images/design/user_interface/search_hint.JPG" alt="The search hint that pops up when the search bar is clicked"></li>
</ul></details>

<details><summary><strong>Content Navigation</strong></summary><ul>
    <li>The content navigation buttons are prioritized by how much content they can present to the user, with the highest volume of posts (The home page, where you can find all posts) listed at the top, and the lowest volume of posts (Most likely the number of user-owned posts) at the bottom</li>
    <li>The page button that the user is currently on is colored in a slightly lighter tint than the rest of the buttons to make it easier for the user to tell what page they are on<br>
    <img src="assets/images/design/user_interface/content_navigation.JPG" alt="The content navigation, ordered by highest volume of posts"></li>
</ul></details>

<details><summary><strong>Post Sorting Buttons</strong></summary><ul>
    <li>All searches for posts can be ordered by the highest number of votes or by most recently posted, with 2 buttons situated above the content navigation</li>
    <li>For consistency, the selected button is colored in the same manner as the selected tab<br>
    <img src="assets/images/design/user_interface/post_sort.JPG" alt="Buttons to sort posts above the content navigation"></li>
    <li>If the user is on a page where the post sorting buttons have no purpose, the buttons will disable, with a faded appearance and complete loss of interaction. I decided to keep the buttons there instead of removing them to maintain the consistent structure of the user interface<br>
    <img src="assets/images/design/user_interface/post_sort_disabled.JPG" alt="Disabled sort buttons on the new post page"></li>
</ul></details>

<details><summary><strong>New/Edit Post Pages</strong></summary><ul>
    <li>The new/edit post consists of a list of inputs for customizing the properties of the post. They are stacked within a column, with the exception of the image inputs for larger screens, which sits on its own to the right. I find that compacting the information this way prevents the inputs from becoming oversized, leaving an excess of blank space across the page<br>
    <img src="assets/images/design/user_interface/new_post_page.JPG" alt="The new post page interface"></li>
    <li>For smaller screens, the image inputs are moved into the same column as the rest of the inputs, and the image preview and option to place the image are hidden if no image has been selected, and will reveal themselves if the user inputs an image. This saves the user from having to scroll through unnecessary content<br>
    <img src="assets/images/design/user_interface/new_post_mobile.JPG" alt="Image position on mobile phones"></li>
    <li>For the same reasons, the poll inputs are only shown when the user has selected to include a poll in their post<br>
    <img src="assets/images/design/user_interface/poll_collapsed.JPG" alt="Poll inputs are collapsed when poll is not selected"><br><img src="assets/images/design/user_interface/poll_expanded.JPG" alt="Poll inputs are expanded when poll is selected"></li>
    <li>These pages have had their enter key press customized to perform actions depending on what input the user is interacting with.
    <ul>
        <li>Pressing enter while focused on the tag input will add a tag to the list of existing tags, if valid</li>
        <li>Pressing enter while focused on the poll answer input will add the answer if it is valid</li>
        <li>Pressing enter in the body text editor will add a new paragraph</li>
        <li>Pressing enter for any other text input will make that input lose focus</li>
        <li>Pressing enter when no input is selected will attempt to submit the form</li>
    </ul>
    The default action of pressing enter attempts to press the first button it finds in the form, which can lead to unexpected results. Having custom behaviours can greatly improve the user experience, and can avoid any frustrations for accidentally submitting the form prematurely
    </li>
</ul></details>

<details><summary><strong>Confirmation Modal</strong></summary><ul>
    <li>When a user attempts to log out, edit or delete their account, or delete
    a post, comment or poll, a modal will appear, asking for confirmation that
    the user really wishes to perform this action. This is good practice to
    provide an extra safety barrier in case the user accidentally clicks one of
    these buttons<br>
    <img src="assets/images/design/user_interface/modal.JPG" alt="A modal confirming the user action"></li>
    <li>For extra sensitive actions, such as editing/deleting the account, the
    modal is enforced with a password confirmation, to confirm the person
    attempting the action is the owner of the account<br>
    <img src="assets/images/design/user_interface/modal_password.JPG" alt="The modal requesting the user's password"></li>
</ul></details>

<details><summary><strong>Alerts</strong></summary><ul>
    <li>Once a user performs an action, after the new page loads an alert
    message will pop at the beginning of the main content section, alerting the
    user if their action was successful or not</li>
    <li>Users can dismiss alerts by clicking on their close icon, or will be
    dismissed automatically after 5 seconds, so that the messages can get out
    of the way of the main content once it has served its purpose</li>
    <li>Successful alerts are blue in color, and unsuccessful ones are red<br>
    <img src="assets/images/design/user_interface/alert_success.JPG" alt="A successful login alert"></li>
    <img src="assets/images/design/user_interface/alert_fail.JPG" alt="An unsuccessful alert"></li>
</ul></details>

### Content Layout

<details><summary><strong>Post Previews</strong></summary><ul>
    <li>Post previews are made up of a header, main body and footer. They are a
    sample of a post aimed at giving the user a sneak peak of the full post,
    making them want to click on it to find out more or read the comments<br>
    <img src="assets/images/design/layout/post_preview.JPG" alt="A preview of a post found on the home page"></li>
    <li>The header is situated at the top of the preview, which is what the user
    would see first, so it is made up of the post's main details such as the
    title, category, user and time since posted</li>
    <li>If the title of the post is too long, a reduced version of it will be
    shown in the preview for space reduction<br>
    <img src="assets/images/design/layout/post_header.JPG" alt="A post header"></li>
    <li>The main body contains the post's main content and its tags. The post
    preview has a limited height to prevent a single post from taking up too
    much space, so if the content requires more space than given, the text will
    appear to fade out at the bottom, and an anchor labelled "Read More..." will
    also appear. This implies to the user that there is more to be seen within
    the full post, tempting them to click to find out more</li>
    <li>If the post has any tags, they will be shown just below the text body.
    These tags can emphasise keywords that may not be visible in the body
    preview, giving the user a more clear idea of the topic of the post without
    having to click to get an understanding. The user should click out of
    curiosity, not out of confusion!</li>
    <li>Images or polls are not shown in the preview because they could take up
    too much space on the screen, causing the user to have to scroll more
    through posts they may not like<br>
    <img src="assets/images/design/layout/post_body.JPG" alt="The post's main content"></li>
    <li>The post footer rests at the end of the post, containing the post's
    number of likes and comments. If the user has got to this point without
    clicking, this is the last thing they see before moving on to the next post,
    so maybe seeing the level of interactivity happening with this post might
    convince them to click and see what the interactions are about<br>
    <img src="assets/images/design/layout/post_footer.JPG" alt="A post footer"></li>
</ul></details>

<details><summary><strong>Post Details</strong></summary><ul>
    <li>The post details page follows a near identical format to it's preview,
    but with the title and content's full context, as well as showing images,
    polls and comments</li>
    <li>Images can be placed either before or after the text body, giving the
    creative power to the user to decide what position workd best for their
    post<br>
    <img src="assets/images/design/layout/post_details.JPG" alt="The full context of a post"></li>
    <li>Polls, however, are always included at the bottom of the post. Polls
    attached to posts generally have something to do with the post itself, so
    it is better for the user to read the post to get a better understanding on
    the poll they are about to vote for<br>
    <img src="assets/images/design/layout/post_poll.JPG" alt="A post with a poll at the bottom"></li>
    <li>The post footer is almost the exact same as in the preview, with the
    exception of the date of posting at the right hand side, as well as the
    ability to interact with the like and comment buttons<br>
    <img src="assets/images/design/layout/post_detail_footer.JPG" alt="Full post footer"></li>
    <li>If the user created the post, 2 extra buttons appear to edit or delete
    the post, giving the user full control over their posts even after creating
    them<br>
    <img src="assets/images/design/layout/post_footer_owned.JPG" alt="Post footer with extra buttons"></li>
</ul></details>

<details><summary><strong>Comments</strong></summary><ul>
    <li>Comments begin by stating the name of the user who posted it, and how
    long ago they posted it. I did this because I felt it's better to figure
    out the "Who" and the "When" before moving on to the "What" of the
    comment</li>
    <li>The comment footer uses the exact same structure as the post footer
    (except for the date), in order to have a consistent layout that is
    easier to follow<br>
    <img src="assets/images/design/layout/comment.JPG" alt="A comment beneath a post"></li>
    <li>Comments are ordered by newest first, so the freshest conversations
    are more likely to be seen<br>
    <img src="assets/images/design/layout/comments_order.JPG" alt="Two comments, with the newest comment on top"></li>
    <li>Replies are grouped with the comment they are replying to, with the
    reply section required to be expanded, which neatly organizes comment
    conversations together without taking up too much space</li>
    <li>Replies are sorted by oldest first, so the conversation can be viewed
    in the order it happened<br>
    <img src="assets/images/design/layout/comment_replies.JPG" alt="The reply section expanded beneath the original comment"></li>
</ul></details>

<details><summary><strong>Polls</strong></summary><ul>
    <li>Polls are made up of a title/question, a set of up to 5 answers and a
    due date. They can have a post attached to them to add context and allow
    other users to like and comment on the poll<br>
    <li>Users can only see the results of a poll after they have voted or after
    the due date, so that the user isn't biased towards the most popular vote.
    For the same reason, users cannot change their vote once they make a
    decision<br>
    <img src="assets/images/design/layout/poll_unanswered.JPG" alt="An unanswered poll"></li>
    <li>Creators of the poll cannot edit them, to prevent making them look like
    people voted for something they didn't. If users want to change the poll,
    they can delete the poll and start a new one, allowing other users to
    change their vote accordingly<br>
    <img src="assets/images/design/layout/poll_owned.JPG" alt="A poll with a delete button"></li>
</ul></details>

### Color Scheme

- Originally, I had intended on using a orange/green color scheme to design Conversate

![The original color scheme of Conversate](assets/images/design/colors/original_design.JPG)

- However, upon reaching the testing phase, I discovered that orange is a tricky color
in terms of accessibility. White-on-orange does not give enough contrast for visually
impaired users to differentiate foreground from background
- At first, I had considered implementing a separate mode for visually impaired users,
but I did not want to remind the users of their impairment making them choose the
option, so I concluded the design of the site must change

![The new design of the site](assets/images/design/colors/new_design.png)

- The new design uses a *blue* hue as the primary color. This is considered a calming
color and symbolizes inspiration. We want the users to feel welcomed, inspired and
encouraged to interact with the site, si I feel this was a good color to use. This
color is mainly found in the user interface
- It also uses a *red* hue as the secondary color. Mainly used for buttons or navigation
links, red is a powerful color that can easily catch the attention of the user. This
color is used sparingly in order to prevent the user from feeling overwhelmed
- I also reduced the amount of color used compared to the original design, in order to
keep the navigation through the site clear and simple
- Overall, while I am fond of the original design, I understand the importance of
accessibility, and going forward, will determine the readability of font colors
during implementation rather than in the testing phase to prevent this from
happening again

### Typography

Conversate's text is made up of 2 separate fonts:

- **Montserrat**: This font is used for all headings<br>
  ![A heading that useses the Montserrat font](assets/images/design/typography/montserrat.JPG)
- **Roboto**: This font is used for all other types of text<br>
  ![A paragraph that useses the Roboto font](assets/images/design/typography/roboto.JPG)

I chose to use these fonts simply because they are easy to read, and work well
with the feel and color scheme selected for the site

### Wireframes

#### Desktop

<details><summary>Login Page</summary><img src="assets/images/wireframes/login_desktop.jpg" alt="Login page wireframe for desktop"></details>
<details><summary>Signup Page</summary><img src="assets/images/wireframes/signup_desktop.jpg" alt="Signup page wireframe for desktop"></details>
<details><summary>Home Page (Post List)</summary><img src="assets/images/wireframes/post_list_desktop.jpg" alt="Home page wireframe for desktop"></details>
<details><summary>Post Details Page</summary>
  <img src="assets/images/wireframes/post_details_desktop.jpg" alt="Post details page wireframe for desktop">
  <img src="assets/images/wireframes/post_comments_desktop.jpg" alt="Post comment section wireframe for desktop"></details>
<details><summary>New/Edit Post Pages</summary>
  <img src="assets/images/wireframes/new_post_top_desktop.jpg" alt="Top of new post page wireframe for desktop">
  <img src="assets/images/wireframes/new_post_bottom_desktop.jpg" alt="Bottom of new post page wireframe for desktop"></details>
<details><summary>New Poll Page</summary><img src="assets/images/wireframes/new_poll_desktop.jpg" alt="New poll page wireframe for desktop"></details>
<details><summary>Poll List Page</summary><img src="assets/images/wireframes/poll_list_desktop.jpg" alt="Poll list page wireframe for desktop"></details>
<details><summary>Category List Page</summary><img src="assets/images/wireframes/category_list_desktop.jpg" alt="Category list page wireframe for desktop"></details>
<details><summary>Account Settings Page</summary><img src="assets/images/wireframes/account_settings_desktop.jpg" alt="Account Settings page wireframe for desktop"></details>

#### Mobile

<details><summary>Login Page</summary><img src="assets/images/wireframes/login_mobile.jpg" alt="Login page wireframe for mobile"></details>
<details><summary>Signup Page</summary><img src="assets/images/wireframes/signup_mobile.jpg" alt="Signup page wireframe for mobile"></details>
<details><summary>Home Page (Post List)</summary><img src="assets/images/wireframes/post_list_mobile.jpg" alt="Home page wireframe for mobile"></details>
<details><summary>Post Details Page</summary>
  <img src="assets/images/wireframes/post_details_mobile.jpg" alt="Post details page wireframe for mobile">
  <img src="assets/images/wireframes/post_comments_mobile.jpg" alt="Post comment section wireframe for mobile"></details>
<details><summary>New/Edit Post Pages</summary>
  <img src="assets/images/wireframes/new_post_top_mobile.jpg" alt="Top of new post page wireframe for mobile">
  <img src="assets/images/wireframes/new_post_bottom_mobile.jpg" alt="Bottom of new post page wireframe for mobile"></details>
<details><summary>New Poll Page</summary><img src="assets/images/wireframes/new_poll_mobile.jpg" alt="New poll page wireframe for mobile"></details>
<details><summary>Poll List Page</summary><img src="assets/images/wireframes/poll_list_mobile.jpg" alt="Poll list page wireframe for mobile"></details>
<details><summary>Category List Page</summary><img src="assets/images/wireframes/category_list_mobile.jpg" alt="Category list page wireframe for mobile"></details>
<details><summary>Account Settings Page</summary><img src="assets/images/wireframes/account_settings_mobile.jpg" alt="Account Settings page wireframe for mobile"></details>

## Agile Methodologies

This website was completed using an agile development system.

- Each feature was broken down into user stories, which are comprised of the following:
  - A set of acceptance criteria to know when the feature is complete
  - Tasks to achieve in order to implement it
  - Story points to give an estimate on how long it will take to complete.
  - An epic which groups similar user stories together

![List of user stories](assets/images/agile/user_stories.JPG)

![Details of a user story](assets/images/agile/user_story_details.JPG)

![Epics that grouped user stories together](assets/images/agile/epics.JPG)

- Once finalized, these user stories were transferred to the product backlog, which was where all incomplete user stories that were not being worked on were kept.

![The product backlog](assets/images/agile/product_backlog.JPG)

- The work done was divided into week-long iterations, with a total of 7 iterations occuring to implement all the features in the website.
  - For each iteration, I added a set of user stories which I was to complete within the week, taken from the product backlog, with the aim of having the total story point number resting between 8 and 10 story points
  - Each user story was given a label:
    - "Must Have", given to user stories that must be completed within the iteration timeframe
    - "Should Have", given to user stories that don't have to be completed for this iteration, but should if possible
    - "Could Have", which are user stories that can be completed if all other user stories are finished
  - For each iteration, no more than 60% of all of its user stories were labelled with "Should have"
  - If user stories were still remaining once an iteration came to a close, they were returned to the product backlog, where they could be selected for future iterations

![Iterations for Conversate](assets/images/agile/iterations.JPG)

## Data Models

![Spreadsheet of models used in Conversate](assets/images/models/data_model.JPG)

### CRUD Functionality

#### Profile

- **Create**: The Profile model is created when a user creates an account. It
is used to store extra information about a user, currently only storing a single
boolean value, sort_by_new. This stores the post order preference of the user so
they do not have to keep setting their preference when entering the site
- **Read**: It's value is read every time a page with a list of posts is
loaded, checking the user's preference and ordering the posts according to what
has been selected
- **Update**: Every time the user clicks one of the post sorting buttons
above the post navigation links, the page will refresh, update the sort_by_new
value and order the posts by this new value
- **Delete**: The Profile object is deleted when a user deletes their account

#### Post

- **Create**: Users can create a post in the "Create Post" page. If an image is
included in the post, it is uploaded to Cloudinary
- **Read**
  - The post can be queried in a post list and displayed as a preview
 along with other posts, where all fields, except the image, comments and poll,
 can be seen.
  - If the user clicks on this preview, the full post is shown with all fields
in the model being put to use
- **Update**
  - Users can find a button in the footer of their own posts to edit
that post.
  - Once the user successfully edits a post, the "edited" boolean field
is set to "True"
  - If the image is updated, the old image is deleted from Cloudinary before the
new one takes its place
  - In the "Post Edit" page, the user can remove an image by clicking the delete
icon in the top-right corner of the image container. This will remove the image
from Cloudinary without having to save the edit
- **Delete**
  - Beside the post edit button, there is another button to delete the post.
After confirming the delete, the post will be removed, and the image will be
removed from Cloudinary
  - If the user deletes their account, all posts belonging to them will be
deleted, and all images will be removed from Cloudinary

#### Comment

- **Create**: Comments can be created in the comments section of a post, by
either the comment input underneath the post, or under a comment for a reply<br>
![Both types of inputs to send a comment/reply](assets/images/models/comment_inputs.JPG)
- **Read**: Comments are loaded with the post they are commented on, and can be
found at the bottom of the page
- **Update**: Users can find the edit comment button in the comment footer. The
comment is then replaced by a textarea input prepopulated with the original
comment<br>
![A comment in edit mode](assets/images/models/comment_edit.JPG)
- **Delete**: Situated beside the edit button, the user can also delete the
comment. If the user or post is deleted, the comment will be deleted as a
result

#### Category

Users do not have permission to create categories. They must be created by
admins, so I decided to not implement CRUD functionality without the admin panel
for this model.

#### Poll

- **Create**: Polls can be created in the "New Poll" page, or as part of a post
in the "New Post" page
- **Read**: Polls can be found in the "Poll" tab group in the side navigation,
or at the bottom of the post it is attached to
- **Update**
  - In order to make polls as legitimate and fair as possible, the
poll title and answers cannot be edited. This prevents users from manipulating
the question or answers to make the poll mean something different than what the
voters have voted for
  - However, what won't affect the results is the due date. Users are allowed to
change the due date even if the poll has already ended
![Interface to edit the poll's due date](assets/images/models/poll_edit.JPG)
- **Delete**: Polls can be deleted by the user by clicking on the trash icon on
the top-right corner of the poll. If the user or post it belongs to is deleted,
the poll will be deleted as well

#### PollAnswer

- **Create**: For each answer the user enters when creating a poll, a poll
answer is created. I decided to do it this way so that the number of answers for
a poll can be customized, with the number stored as the constant "maxAnswers" in
the "polls.js" file
- **Read**: These answers are loaded by their polls and used for radio inputs
for the user to select their answer
- **Update**: Like the poll, the body of these answers cannot be changed to keep
the poll fair, However, when the user casts a vote, they are added to the
selected poll answer's "votes" value
- **Delete**: Answers can only be deleted when the poll they belong to is
deleted

#### SiteData

- **Create**: Only one item exists in this model, which is used for any
variables the site needs to store. Currently it only stores the number of posts
created
- **Read**: Every time a post is created, the total_posts_created value is read
and converted into a customized miniature UUID, used to generate a part of the
post's slug
- **Update**: When this value is read, the number_of_posts value is increased
by 1
- **Delete**: The item in this model should not be deleted, but if it is, a new
one will be created when the data is requested, setting the value of
total_posts_created to 0

## Testing

### Bugs

- **Tags disappear after post edit**
  - *Expected result*: All previously entered tags should remain if kept by the
user
  - *Solution*: The hidden input used to store the tags did not have its value
set to the original list of tags on page load, so if the user updates the post
without editing the tags, the tag data is lost. To fix, set this input's value
to the post's tags
- **Clicking on the poll checkbox collapse again during the collapse animation**
**will cause the collapse and the checkbox to become out of sync**
  - *Expected result*: If the checkbox is checked, the poll collapse should be
shown, and vice versa
  - *Solution*: Once the collapse animation is finished, the checkbox is checked
again, and if the checkbox and collapse are out of sync then the collapse is
updated again to synchronize them once again
- **Images remain on Cloudinary if the user deletes their account without**
**deleting their posts first**
  - *Expected result*: If the user deletes their account, all their posts, and
their images along with it, should be deleted, as leaving them could cause a
data overflow on Cloudinary
  - *Solution*: If a user deletes their account, before the deletion, iterate
through all their posts and delete the images individually
- **Body text of post is sometimes deleted after editing a post**
  - *Expected result*: The body text of the post should always save with what is
in the text editor
  - *Solution*: Summernote does not update its value unless the user clicks into
it, so if the user edits the post without changing the content, the body input
will be left blank. The solution I came up with was to store the original text
in a hidden input, and if the body text is found to be blank on submission, set
the text value to this input
- **Image position moves to top of post after editing the post**
  - *Expected result*: Image should stay in the position it was set to be in
  - *Solution*: On the edit post page, the select input was always set to
"Top of page", despite what the user had previously entered, so if the post
were to be edited without altering this input, it would default to the top of
the page. To fix this, add an if statement in the edit_post template to update
the select input depending on what the original image_position is

### Manual Testing

Manual testing is broken into 3 categories, and can be found here:

- [Buttons and anchors](TEST_BUTTONS.md)
- [Form validation](TEST_FORMS.md)

*Note*: All found issues stated in these documents have been resolved. `Look out
for code snippet text to view found issues`

### Automated Testing

#### Unittest

Unittest was used to test the following Python files:

<details><summary><strong>slug&#46;py</strong></summary>
This file contains the functions responsible for handling
slug creation. It consists of the following functions:<ul>
<li><strong>generate_slug</strong>: This function generates a unique slug for
each post, giving the ability for multiple posts with the same title to coexist.
It takes the title of the post and the slug of the post's category as
parameters. It does so by starting the slug with "(category_slug)-". It then
sets the random seed to the total number of posts on the site, and generates 8
random characters (digits or letters) using that seed. Finally, it will add the
title, which will be converted to a slug-friendly format, to the end of the
slug.<br>
The rules I tested for this function are as follows:<ul>
    <li>The "title" parameter must be a string</li>
    <li>The "category_slug" parameter must be a string</li>
    <li>The function returns a string</li>
    <li>A set of 8 randomly generated characters is present in the output (This
could be tested because the random numbers are seeded, so will always return
"SoMUq2gZ" for seed 0)</li>
    <li>The category slug is present in the output</li>
    <li>A slugified version of the title input is present within the slug<br>
<img src="assets/images/testing/test_generate_slug.JPG" alt="The test cases for generate_slug"></li>
<li>This function contains also updates the SiteData Django model to add 1 to
its total number of posts. This cannot be tested using unittest, as it requires
Django configuration, but was tested manually to confirm it works. The automated
test on this function was run without this code snippet and produced positive
results</li>
</ul></li>
<li><strong>generate_character_set</strong>: This function returns a sequence of
random characters as a string. It takes in 2 parameters, the seed for random
generation and the amount of characters that will exist in the string<br>
The rules I tested for this function are as follows:<ul>
    <li>The "seed" parameter must be an integer</li>
    <li>The "number_of_characters" parameter must be an integer</li>
    <li>number_of_characters must be between 1 and 100 (negative seed numbers
is fine)</li>
    <li>The function returns a variable of type "string"</li>
    <li>The length of the string equals the number_of_characters parameter</li>
    <li>The output is consistent with the seed input (seed 0 always gives
"SoMUq2gZ", seed 100 gives "9ttYNbJp")<br>
<img src="assets/images/testing/test_generate_chars.JPG" alt="The test cases for generate_character_set"></li>
</ul></li>
<li><strong>get_character</strong>: This function takes in an index as a
parameter and returns a specific character that has that index.<br>
The rules I tested for this function are as follows:<ul>
    <li>"index" parameter must be an integer</li>
    <li>index must be between 0 and 61</li>
    <li>The function returns a variable of type "string"</li>
    <li>An index value of less than 10 returns a set number character</li>
    <li>An index value between 10 and 35 returns a set lowercase letter</li>
    <li>An index value between 36 and 61 returns a set uppercase letter<br>
<img src="assets/images/testing/test_get_char.JPG" alt="The test cases for get_character"></li>
</ul></li>
<li><strong>format_tag_search</strong>: This function takes in a query entered
by the user in the search bar and converts it into a useable URL, removing all
special characters besides the allowed "_" and "-", and replaces any spaces with
a "+" symbol<br>
The rules I tested for this function are as follows:<ul>
    <li>The "tag_list" parameter must be a string</li>
    <li>The function returns a variable of type "string"</li>
    <li>The output removes any special characters from the input</li>
    <li>The output keeps underscores "_" in the input</li>
    <li>The output keeps dashes "-" in the input</li>
    <li>The output replaces spaces " " with pluses "+" in the input<br>
<img src="assets/images/testing/test_format_tags.JPG" alt="The test cases for format_tag_search"></li>
</ul></li>
<li>All tests have passed on running the test file (after removing the model
SiteData and all its references)<br>
<img src="assets/images/testing/test_slug.JPG" alt="The results of test_slug.py"></li>
</ul>
</details>

<details><summary><strong>pagination&#46;py</strong></summary>
This file is responsible for creating a list of page numbers for the pagination
bar. Only a limited number of pages can be displayed, so the first page, last
page and all pages within a specified radius of the current page is shown.<br>
It contains only one function that was tested automatically:<ul>
<li><strong>get_page_range</strong>: This function returns an object containing
the range of numbers with the current page in the middle and has a length of the
constant MAX_PAGES - 2 (The 2 missing is for the first and last page). For
example, a current page of 24 with a MAX_PAGES of 9 will produce
[20, 21, 23, 24, 25, 26, 27]<br>
The rules I tested for this function are as follows:<ul>
    <li>The "page_index" parameter must be an integer</li>
    <li>The "last_page" parameter must be an integer</li>
    <li>The "num_pages" parameter must be an integer</li>
    <li>The "page_index" parameter must be between 1 and the "last_page"
parameter</li>
    <li>"last_page" cannot be less than "num_pages"</li>
    <li>"num_pages" cannot be less than 1</li>
    <li>"num_pages" must be an odd number (to allow the current page to be in
the middle)</li>
    <li>The "page_range" key of the object output must have a length of
"num_pages"</li>
    <li>If the current page is not at the beginning or end of the list of pages,
then it sits directly in the middle of the list of pages</li>
    <li>The list of pages always includes the first page</li>
    <li>The list of pages always includes the last page</li>
    <li>If there is a gap between the first page and the group of pages
surrounding the current one, the returned key of "start_gap" must be True</li>
    <li>If there isn't a gap, the returned key of "start_gap" must be False</li>
    <li>If there is a gap between the last page and the group of pages
surrounding the current one, the returned key of "end_gap" must be True</li>
    <li>If there isn't a gap, the returned key of "end_gap" must be False<br>
<img src="assets/images/testing/test_page_range_1.JPG" alt="First half of get_page_range test cases">
<img src="assets/images/testing/test_page_range_2.JPG" alt="Second half of get_page_range test cases"></li>
</ul></li>
<li>All tests have passed on running the test file<br>
<img src="assets/images/testing/test_pagination.JPG" alt="The results of test_pagination.py"></li>
</ul>
</details>

I used the Red, Green, Refactor (RGR) method to implement these test cases. This
involves creating a test case that is known to fail:

![The "Red" part of a test life cycle](assets/images/testing/test_red.JPG)

Then, the bare minimum amount of code is written to make the test pass:

![The "Green" part of a test life cycle](assets/images/testing/test_green.JPG)

And finally, where applicable, the code is refactored to make it more clean and
reuseable, and the cycle of the test starts again. The benefir of using this
system is that once the code has been completed, there is no need to manually
test it afterwards, as all test cases have already been accounted for

#### Jest

All of my JavaScript files involve manipulating the DOM, so I decided that
using the DOM to test my scripts instead of using Jest's mocking function was
more efficient. JavaScript functions that involved clicking on buttons and
anchors were all tested and can be found within the
[button testing section](TEST_BUTTONS.md), and the JavaScript that involved
form validation was tested and can be found in the
[form validation section](TEST_FORMS.md)

### Browser Testing

- Google Chrome: Conversate was developed using Google Chrome, and all manual
testing was done on this browser, with no issues detected
- Microsoft Edge: Conversate was tested on Microsoft Edge with no issues. The
design, functionality, animations and responsiveness remains the exact same as
Google Chrome
- Firefox: After testing Conversate on Firefox, the only difference I found is
that the bold text in the navigation bar looks slightly wider than on Edge and
Chrome. This is merely cosmetic so I don't find any issue with this

Logo on Chrome:

![Logo on Chrome](assets/images/testing/logo_chrome.JPG)

Logo on Firefox:

![Logo on Firefox](assets/images/testing/logo_firefox.JPG)

### Known Issues/Unfixed Bugs

The "required" attribute in the Summernote input field doesn't work, which
allows users to submit a post without any body text. However, I was able to find
a workaround for this:

- I created a text input field, giving it the width of the Summernote container,
positioning it at the bottom of the container and giving it a low z-index to
hide it behind the screen
- I gave this field a custom validation of "Please fill out this field.", which
prevents the form from submitting
- Every time the summernote text field is updated, it is checked for any content
within it. If it has content, the custom validity is removed, but if there isn't,
it will remain, or be created if it was already removed
- This gives the illusion that the Summernote text area is requiring input within
it

![Feedback from the Summernote editor](assets/images/testing/summernote_required.JPG)

## Validation

### W3C HTML

I could not produce valid W3C HTML results, due to Django's template tags, and
if statements using opening tags with no closing tags and vice versa, causing
errors

![List of HTML errors caused by Django](assets/images/validation/html.png)

### W3C CSS

![style.css validation](assets/images/validation/css.png)

### JSHint

<details><summary>script.js</summary>
<img src="assets/images/validation/js/script.png" alt="Validation for script.js">
</details>

<details><summary>posting.js</summary>
<img src="assets/images/validation/js/posting.png" alt="Validation for posting.js">
</details>

<details><summary>comments.js</summary>
<img src="assets/images/validation/js/comments.png" alt="Validation for comments.js">
</details>

<details><summary>polls.js</summary>
<img src="assets/images/validation/js/polls.png" alt="Validation for polls.js">
</details>

<details><summary>forms.js</summary>
<img src="assets/images/validation/js/forms.png" alt="Validation for forms.js">
</details>

<details><summary>modals.js</summary>
<img src="assets/images/validation/js/modals.png" alt="Validation for modals.js">
</details>

<details><summary>accountSettings.js</summary>
<img src="assets/images/validation/js/account_settings.png" alt="Validation for accountSettings.js">
</details>

### PEP8

<details><summary>views.py</summary>
<img src="assets/images/validation/python/views.png" alt="Validation for views.py">
</details>

<details><summary>models.py</summary>
<img src="assets/images/validation/python/models.png" alt="Validation for models.py">
</details>

<details><summary>urls.py</summary>
<img src="assets/images/validation/python/urls.png" alt="Validation for urls.py">
</details>

<details><summary>content.py</summary>
<img src="assets/images/validation/python/content.png" alt="Validation for content.py">
</details>

<details><summary>slug.py</summary>
<img src="assets/images/validation/python/slug.png" alt="Validation for slug.py">
</details>

<details><summary>categories.py</summary>
<img src="assets/images/validation/python/categories.png" alt="Validation for categories.py">
</details>

<details><summary>forms.py</summary>
<img src="assets/images/validation/python/forms.png" alt="Validation for forms.py">
</details>

<details><summary>messages.py</summary>
<img src="assets/images/validation/python/messages.png" alt="Validation for messages.py">
</details>

<details><summary>pagination.py</summary>
<img src="assets/images/validation/python/pagination.png" alt="Validation for pagination.py">
</details>

<details><summary>dates.py</summary>
<img src="assets/images/validation/python/dates.png" alt="Validation for dates.py">
</details>

<details><summary>tests.py</summary>
<img src="assets/images/validation/python/tests.png" alt="Validation for tests.py">
</details>

### Lighthouse

Lighthouse tests for the site's accessibility, such as aria labels and color contrast.
All pages tested received a high percentage in terms of performance, accessibility,
best practices and search engine optimization

<details><summary><strong>The Login Page</strong></summary>
<img src="assets/images/validation/lighthouse/login.jpg" alt="The login page lighthouse results">
</details>

<details><summary><strong>The Signup Page</strong></summary>
<img src="assets/images/validation/lighthouse/login.jpg" alt="The signup page lighthouse results">
</details>

<details><summary><strong>The Post List Page</strong></summary>
<img src="assets/images/validation/lighthouse/post_list.jpg" alt="The post list page lighthouse results">
</details>

<details><summary><strong>The Post Details Page</strong></summary>
<img src="assets/images/validation/lighthouse/post_details.jpg" alt="The post details page lighthouse results">
</details>

<details><summary><strong>The New Post Page</strong></summary>
<img src="assets/images/validation/lighthouse/new_post.jpg" alt="The new post page lighthouse results">
</details>

<details><summary><strong>The Edit Post Page</strong></summary>
<img src="assets/images/validation/lighthouse/edit_post.jpg" alt="The edit post page lighthouse results">
</details>

<details><summary><strong>The Browse Categories Page</strong></summary>
<img src="assets/images/validation/lighthouse/browse_categories.jpg" alt="The browse categories page lighthouse results">
</details>

<details><summary><strong>The Account Settings Page</strong></summary>
<img src="assets/images/validation/lighthouse/account_settings.jpg" alt="The account settings page lighthouse results">
</details>

<details><summary><strong>The Edit Account Page</strong></summary>
<img src="assets/images/validation/lighthouse/edit_account.jpg" alt="The edit account page lighthouse results">
</details>

## Deployment and Local Development

### Deployment to Heroku

Converaste&#46;com has been deployed to Heroku. I ensured that the site was deployed
here in the early stages of development in order to prevent any last-minute
frustrations, and regularly kept an eye on the deployed version throughout the
site's development to make sure that it didn't break in the process.

Before pushing the Django project to GitHub, make sure:
- All sensitive information, such as the secret key and any database links,
are solely stored in the env&#46;py file, and that file is stored in the
&#46;gitignore file
- There is a list of all installed packages in the requirements&#46;txt file.
This is so that Heroku knows what modules it needs for the website to function,
and can be done by entering the command `pip3 freeze --local > requirements.txt`
- The DEBUG variable is set to False on the deployed website

The steps to deploy are as follows:

- Navigate to Heroku's main dashboard
- On the upper right hand side of the site, click on "New", then
"Create new app"
- Give the app a name, select your region, and click "Create app"
- Once the app is created, navigate to the "Settings" tab
- Scroll down to the "Config Vars" section and click "Reveal Config Vars".
Two text input fields should appear: "KEY" and "VALUE":
  - Add KEY "PORT" with VALUE "8000"
  - Add KEY "IP" with VALUE "8000"
  - Add KEY "SECRET_KEY" with the VALUE of your secret key
  - Add KEY "DATABASE_URL" with the VALUE of the url of your database
  - Add KEY "CLOUDINARY_URL" with the VALUE of the url of your cloudinary database
  - For my project, I added an extra config var called "DEVELOPMENT", which
    controlled the DEBUG setting, and set it to "False"
- Navigate to the "Deploy" tab
- In the Deployment method section, select GitHub and connect to GitHub
underneath
- Search for the desired repository and click "Connect" once found
- Underneath, you can enable automatic deploys or deploy the workspace
manually. Select one and the workspace will be deployed

### Cloning Repositories

The site was cloned onto my desktop. The steps to clone are as follows:

- In the GitHub repository, click on the green button that says "Code".
A drop-down menu will appear
- In the "Local" tab of the drop-down, there will be a link under the "HTTPS"
section. Click the copy button to the right of the link.
- In the search bar of your PC desktop, search for terminal and open.
- Type the following command:
`git clone https://github.com/ShaneByrne0963/conversate-dot-com.git`
- The site will be cloned to your desktop.

### Forking Repositories

The site was created using a forked repository created by Code Institute. This
repository can be found
[here](https://github.com/Code-Institute-Org/ci-full-template).

The steps to fork are as follows:

- Navigate to the page of the repository you wish to fork.
- Click on the green button that says "Use this template". A drop-down will
appear underneath, and select "create a new repository"
- Enter a repository name where specified.
- Ensure the site is set to public
- Click "Create repository from template". GitHub will begin to build a
new project from that template.

## Credits

- Conversate was made using the [Django Framework](https://www.djangoproject.com/)
- The site was styled with the help of [Bootstrap](https://getbootstrap.com/)
- The [Django Summernote text editor](https://github.com/summernote/django-summernote)
was used for the post body input
- Content used to populate the site was generated by [ChatGPT](https://chat.openai.com/)
- Color scheme was decided with the assistance of [Colormind](http://colormind.io/)
