# Conversate&#46;com

## Introduction

Conversate&#46;com is a forum website where people can connect with each other by writing posts, uploading images and creating polls for other people to vote on. The aim of this website is to provide a platform that gives its users a wide range of ways to express their thoughts and opinions, as well as making those expressions as accessible to other users as possible. Conversate was made using the Django framework and designed using Bootstrap

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
  - Upon logging in to the site, users are introduced to the site's home page, where they can explore a wide range of posts the site has to offer. Having every kind of post available on the home page can help newcomers who are unsure about what they are looking for discover the kind of content that best suits them.
  - If users are looking for something a little more specific, they have an option to search for posts using keywords.
  - Posts can be sorted by "Popular" (Highest number of likes) or "New" (Most recently posted)
- **To share their information with the world**
  - Users can create posts, upload images and ask questions through the use of polls.
  - Posts can be customized using a wide selection of styles, allowing the creators to add headings, divide their content into paragraphs, include lists and tables, and add links to other pages.
- **To interact with a community that relates to them**
  - Posts can have a category assigned to them. Users that are searching for a particular type of post can explore these categories and discover a community that is also interested in this topic.

> *"How do we want our users to feel while using our website?"*

- **Encouraged to interact with the community**
  - Users are required to be logged in to navigate through the majority of the website, which means if they discover a post that interests them they will always have the opportunity to like and comment on that post, as well as vote in polls they discover.

## Features

- **Posts**
  - Posts are the main attraction to Conversate. They are blocks of text created by users to send their thoughts out to the world for all to see.<br>
    ![A user post](readme_images/features/post_content.JPG)
  - All posts are made up of a title and a main body of text. The site uses Summernote's text editor to give users the ability to add style to their posts. They can add headings, paragraphs, bullet points, links, tables and horizontal rules. Text can also be styled in a number of ways, including changing the font size and setting the font to bold, italics or underlined
    ![A post using different styles of text](readme_images/features/post_styled.JPG)<br>
  - Categories can be added to a post in order to group it with other posts of a similar nature. There are a selection of categories created by the site administrators that can be chosen from
  - Images can also be added to a post. A picture is worth a thousand words, so adding one can add an invaluable layer of depth to the story the poster is trying to tell. Images can be placed above or below the main body of text<br>
    ![A post with an image at the top](readme_images/features/post_image.JPG)
  - Posts can be tagged with a list of keywords. These tags can be clicked on, revealing all posts that also have this tag. Using hashtags can increase the likelihood of the post to be seen, as it provides an extra method for posts to be queried
  - Users can choose to like posts to show appreciation to the poster. Posts with more likes are more likely to be found by exploring users. Posters cannot like their own posts
    ![A list of keywords tagging the post](readme_images/features/post_tags.JPG)
- **Comments**
  - Users can comment on posts to share thoughts or add insight of their own
  - If a user sees a comment they appreciate, they can like that comment
    ![A comment left under a post](readme_images/features/comment.JPG)
  - Comments can also be replied to so that a conversation can be started with the commenter. Replies can be replied to in a similar manner
    ![A conversation within the comments](readme_images/features/comment_replies.JPG)
- **Polls**
  - Polls are an excellent way to collect answers and gather statistics from the site's community. They are made up of a question (title), a list of between 2 and 5 answers, and an end date.
    ![A user submitted poll](readme_images/features/poll.JPG)
  - Polls can be included within a post, giving the user the ability to add more context to the poll, as well as allowing people to respond in the comments
    ![A poll that is part of a post](readme_images/features/poll_post.JPG)
  - Users can only vote for one answer in the list, and once they vote on their decision, they are unable to change their vote
  - Answers from other users cannot be seen until the user has voted, in order to prevent people from only selecting the most popular vote
    ![A poll that has revealed its answers after a vote](readme_images/features/poll_voted.JPG)
  - Once a poll has passed its due date, votes will no longer be accepted and the final results will be shown
    ![A poll that has ended](readme_images/features/poll_ended.JPG)
- **The Home Page**
  - When the user first logs in to Conversate, the home page is the first step on their journey.
  - They are welcomed with any possible kind of post made, allowing them to explore a wide variety of content until they find something that interests them.
    ![The home page](readme_images/features/home_page.JPG)
- **Categories**
  - If users are looking for something a little more specific, they can search for posts by what category they belong to.
  - A list of categories is present within the navigation that shows the categories with the most posts, making more content easily available to the user
    ![A list of categories available from the navigation](readme_images/features/category_navigation.JPG)
    ![Results for searching by category](readme_images/features/category_search.JPG)
- **Search Posts**
  - For users that are specifically looking for posts that contain certain words or phrases, they can use the search bar and find those posts
    ![Searching for posts with the word "chocolate" in the search bar](readme_images/features/search_bar.JPG)
    ![The results found 2 posts with the word "chocolate"](readme_images/features/search_results.JPG)
  - Users also have the option to search for post tags by prefixing their search with a hashtag ("#")<br>
    ![Searching for posts with the tag "Alps"](readme_images/features/search_tags.JPG)
    ![The results found 2 posts tagged with "Alps"](readme_images/features/search_tag_results.JPG)
- **"My Posts"**
  - Users can easily jump to their created posts to monitor interactions by clicking on the "My Posts" button within the navigation
    ![All the user's posts in one place](readme_images/features/my_posts.JPG)
- **Filter Posts by Likes/Newest**
  - All of the above methods of finding posts can have the results of those queries sorted by "Popular" or "New", first displaying the posts with the highest number of likes or posts that were most recently created, respectively
    ![Buttons to sort the selection of posts, with "Popular" being selected](readme_images/features/post_sort.JPG)
    ![Posts with the highest number of likes are shown as a result](readme_images/features/post_sort_results.JPG)
- **Browse Polls**
  - Along with posts, users can also browse through and vote on polls, made easy through the use of the "Polls" navigation tab
  - Here, polls are divided into 3 categories:
    - *Open polls*, where users can engage with polls and contribute their opinion to the overall score
    - *Closed polls*, if the user feels like gathering information about votes that occured in the past
    - *"My polls"*, which is a place for the user to find the answers to all their asked questions<br>
  - Posts as part of polls are included, with a link to the post so the user can get the full context of the poll, as well as engage with the comments
  ![The poll dropdown in the navigation](readme_images/features/poll_navigation.JPG)
  ![A list of open polls](readme_images/features/poll_list.JPG)

## Design

### User Interface

- **The Login/Signup Page**

### Color Scheme

I decided to use a 2-hue color scheme to design Conversate

- **Primary Color**: I chose to use a *red-orange* hue as the primary color. This hue is used mostly to decorate the user interface and headings, so it covers a significant portion of the page. I decided on this because orange is often associated with warmth, positivity, sociability and creativity, all of which are important emotions we want the users to feel in order to be encouraged to interact with the community and create content.

![The side navigation, with all elements colored a shade of orange](readme_images/design/colors/primary_color.JPG)

- **Secondary Color**: I decided on using a *light green* hue as my secondary color. This color's main purpose is to draw attention to whatever is colored by it, so it is used to color buttons and links. Posts in the post list page also use this color, but as a lighter, less saturated form in order to not be too overpowering

![A post item, showing different shades of green to attract the user's eye](readme_images/design/colors/secondary_color.JPG)

I find these two colors compliment each other very well. They look good together, while at the same time being distinct from each other. The green color draws your attention from the orange, which helps guide you through the site in the direction it wants you to go

![The two colors, side by side](readme_images/design/colors/combination.JPG)

### Typography

Conversate's text is made up of 2 separate fonts:

- **Montserrat**: This font is used for all headings<br>
  ![A heading that useses the Montserrat font](readme_images/design/typography/montserrat.JPG)
- **Roboto**: This font is used for all other types of text<br>
  ![A paragraph that useses the Roboto font](readme_images/design/typography/roboto.JPG)

I chose to use these fonts simply because they are easy to read, and work well with the feel and color scheme selected for the site

### Wireframes

#### Desktop

<details><summary>Login Page</summary><img src="readme_images/wireframes/login_desktop.jpg" alt="Login page wireframe for desktop"></details>
<details><summary>Signup Page</summary><img src="readme_images/wireframes/signup_desktop.jpg" alt="Signup page wireframe for desktop"></details>
<details><summary>Home Page (Post List)</summary><img src="readme_images/wireframes/post_list_desktop.jpg" alt="Home page wireframe for desktop"></details>
<details><summary>Post Details Page</summary>
  <img src="readme_images/wireframes/post_details_desktop.jpg" alt="Post details page wireframe for desktop">
  <img src="readme_images/wireframes/post_comments_desktop.jpg" alt="Post comment section wireframe for desktop"></details>
<details><summary>New/Edit Post Pages</summary>
  <img src="readme_images/wireframes/new_post_top_desktop.jpg" alt="Top of new post page wireframe for desktop">
  <img src="readme_images/wireframes/new_post_bottom_desktop.jpg" alt="Bottom of new post page wireframe for desktop"></details>
<details><summary>New Poll Page</summary><img src="readme_images/wireframes/new_poll_desktop.jpg" alt="New poll page wireframe for desktop"></details>
<details><summary>Poll List Page</summary><img src="readme_images/wireframes/poll_list_desktop.jpg" alt="Poll list page wireframe for desktop"></details>
<details><summary>Category List Page</summary><img src="readme_images/wireframes/category_list_desktop.jpg" alt="Category list page wireframe for desktop"></details>
<details><summary>Account Settings Page</summary><img src="readme_images/wireframes/account_settings_desktop.jpg" alt="Account Settings page wireframe for desktop"></details>

#### Mobile

<details><summary>Login Page</summary><img src="readme_images/wireframes/login_mobile.jpg" alt="Login page wireframe for mobile"></details>
<details><summary>Signup Page</summary><img src="readme_images/wireframes/signup_mobile.jpg" alt="Signup page wireframe for mobile"></details>
<details><summary>Home Page (Post List)</summary><img src="readme_images/wireframes/post_list_mobile.jpg" alt="Home page wireframe for mobile"></details>
<details><summary>Post Details Page</summary>
  <img src="readme_images/wireframes/post_details_mobile.jpg" alt="Post details page wireframe for mobile">
  <img src="readme_images/wireframes/post_comments_mobile.jpg" alt="Post comment section wireframe for mobile"></details>
<details><summary>New/Edit Post Pages</summary>
  <img src="readme_images/wireframes/new_post_top_mobile.jpg" alt="Top of new post page wireframe for mobile">
  <img src="readme_images/wireframes/new_post_bottom_mobile.jpg" alt="Bottom of new post page wireframe for mobile"></details>
<details><summary>New Poll Page</summary><img src="readme_images/wireframes/new_poll_mobile.jpg" alt="New poll page wireframe for mobile"></details>
<details><summary>Poll List Page</summary><img src="readme_images/wireframes/poll_list_mobile.jpg" alt="Poll list page wireframe for mobile"></details>
<details><summary>Category List Page</summary><img src="readme_images/wireframes/category_list_mobile.jpg" alt="Category list page wireframe for mobile"></details>
<details><summary>Account Settings Page</summary><img src="readme_images/wireframes/account_settings_mobile.jpg" alt="Account Settings page wireframe for mobile"></details>

## Agile Methodologies

This website was completed using an agile development system.

- Each feature was broken down into user stories, which are comprised of the following:
  - A set of acceptance criteria to know when the feature is complete
  - Tasks to achieve in order to implement it
  - Story points to give an estimate on how long it will take to complete.
  - An epic which groups similar user stories together

![List of user stories](readme_images/agile/user_stories.JPG)

![Details of a user story](readme_images/agile/user_story_details.JPG)

- Once finalized, these user stories were transferred to the product backlog, which was where all incomplete user stories that were not being worked on were kept.

![The product backlog](readme_images/agile/product_backlog.JPG)

- The work done was divided into week-long iterations, with a total of 7 iterations occuring to implement all the features in the website.
  - For each iteration, I added a set of user stories which I was to complete within the week, taken from the product backlog, with the aim of having the total story point number resting between 8 and 10 story points
  - Each user story was given a label:
    - "Must Have", given to user stories that must be completed within the iteration timeframe
    - "Should Have", given to user stories that don't have to be completed for this iteration, but should if possible
    - "Could Have", which are user stories that can be completed if all other user stories are finished
  - For each iteration, no more than 60% of all of its user stories were labelled with "Must have"
  - If user stories were still remaining once an iteration came to a close, they were returned to the product backlog, where they could be selected for future iterations

![Iterations for Conversate](readme_images/agile/iterations.JPG)

## Data Models

### CRUD Functionality

## Testing

### Bugs

### Manual Testing

### Automated Testing

### Browser Testing

## Validation

### W3C HTML

### W3C CSS

### JSHint

### PEP8

### Lighthouse Page Loading

### WebAIM Color Contrast

## Deployment and Local Development

### Deployment to Heroku

### Cloning Repositories

### Forking Repositories

## Credits

### Libraries/Tutorials

### Media

- Conversate was made using the [Django Framework](https://www.djangoproject.com/)
- The site was styled with the help of [Bootstrap](https://getbootstrap.com/)
- The [Django Summernote text editor](https://github.com/summernote/django-summernote) was used for the post body input
- Content used to populate the site was generated by [ChatGPT](https://chat.openai.com/)
- Color scheme was decided with the assistance of [Colormind](http://colormind.io/)
