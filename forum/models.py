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


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    def number_of_posts(self):
        return self.tagged_posts.count()


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,
                            related_name='tagged_posts')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='added_posts')
    posted_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    edited = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return f'({self.tag}) {self.title}'

    def number_of_likes(self):
        return self.likes.count()

    def number_of_comments(self):
        return self.comments.count()

    def date_formatted(self):
        day = ''
        if self.posted_on.day < 10:
            day += '0'
        day += str(self.posted_on.day)
        month = ''
        if self.posted_on.month < 10:
            month += '0'
        month += str(self.posted_on.month)
        year = self.posted_on.year % 100
        hour = self.posted_on.hour
        minute = self.posted_on.minute
        return (f'{day}/{month}/{year},{hour}:{minute} -')


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
