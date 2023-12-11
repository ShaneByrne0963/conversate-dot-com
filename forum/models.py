from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class SiteData(models.Model):
    # region Explanation for why this is necessary
    """
    Used for slug generation. If the total number of active posts was used
    instead, then deleting posts can cause repeated character sets,
    increasing the risk of duplicate slugs
    """
    # endregion
    total_posts_created = models.IntegerField(default=0)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True, related_name='profile')
    sort_by_new = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    icon = models.CharField(max_length=30, default="fa-tag")

    def __str__(self):
        return self.name

    def number_of_posts(self):
        return self.tagged_posts.count()


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='tagged_posts')
    image = CloudinaryField('image', blank=True)
    image_position = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='added_posts')
    posted_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    tags = models.CharField(max_length=200, blank=True)
    edited = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return f'({self.category}) {self.title}'

    def number_of_likes(self):
        return self.likes.count()

    def number_of_comments(self):
        return self.comments.count()

    def tag_list(self):
        tags_separate = self.tags.split('#')
        # Removes the blank tag at the start of the list
        tags_separate.pop(0)
        return tags_separate


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    content = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='added_comments')
    posted_on = models.DateTimeField(auto_now_add=True)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE,
                                 related_name='replies', blank=True, null=True)
    edited = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name="comment_likes",
                                   blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return f'{self.posted_by}: {self.content}'

    def number_of_likes(self):
        return self.likes.count()

    def number_of_replies(self):
        return self.replies.count()


class Poll(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    post = models.OneToOneField(Post, on_delete=models.CASCADE,
                                related_name='poll', blank=True, null=True)

    class Meta:
        ordering = ['-due_date']
    
    def __str__(self):
        return f'[{self.category}] {self.title}'
    
    def number_of_answers(self):
        return self.answers.count()
    
    def poll_status(self, user_id):
        """
        Gets the status of the poll:
        -1: The poll is closed and the user has not voted
        0: The poll is open and the user has not voted
        >1: The user has voted for the number that is returned
        """
        answers = list(self.answers.all())
        for answer in answers:
            if answer.votes.filter(id=user_id).exists():
                return answer.position
        return 0


class PollAnswer(models.Model):
    body = models.CharField(max_length=100)
    position = models.IntegerField()
    poll = models.ForeignKey(Poll, related_name='answers',
                             on_delete=models.CASCADE)
    votes = models.ManyToManyField(User, related_name='votes')

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.poll} => {self.body}'
    
    def number_of_votes(self):
        return self.votes.count()
    
    def vote_percentage(self):
        total_votes = 0
        poll_answers = self.poll.answers.all()
        for answer in poll_answers:
            total_votes += answer.votes.count()
        return round((self.votes.count() / total_votes) * 100)
