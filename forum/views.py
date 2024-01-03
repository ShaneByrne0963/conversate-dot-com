from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import View
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.db.models import Q, Count
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from .models import Post, Category, Comment, SiteData, Poll, PollAnswer
from .forms import UpdateUserForm
from .core.content import get_profile, get_post_list_context, \
                          get_base_context, get_category_list_context, \
                          get_poll_list_context, get_post_context, \
                          get_post_form_context, create_poll, delete_image
from .core.slug import generate_slug, format_tag_search
from .core.messages import display_error, display_success, deny_access, \
                           display_form_errors
from datetime import datetime
import urllib.parse
import cloudinary


class ListPosts(View):

    def get(self, request):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('/accounts/login')

        posts = Post.objects.all()

        context = get_post_list_context(request, posts)
        user_profile = get_profile(request.user)
        if user_profile.sort_by_new:
            context['heading'] = "What's New"
        else:
            context['heading'] = "What's Popular"
        context['selected_tab'] = 'Home'

        return render(
            request,
            'post_list.html',
            context,
        )


class SortPosts(View):

    def get(self, request, by_new, current_dir):
        profile = get_profile(request.user)
        profile.sort_by_new = (by_new == 1)
        profile.save()
        return redirect(current_dir)


class SearchPost(View):

    def get(self, request):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('/accounts/login')

        # Redirects the user to the home page if no search query is given
        if 'search_query' not in request.GET:
            return redirect('home')
        search_input = request.GET.get('search_query')

        # Searching by tags if a hashtag is at the beginning of the search
        if search_input.strip()[0] == '#':
            search_formatted = format_tag_search(search_input)
            return HttpResponseRedirect(reverse('search_tag',
                                                args=[search_formatted]))

        query = Q(Q(title__icontains=search_input) |
                  Q(content__icontains=search_input))
        posts = Post.objects.filter(query)
        number_of_results = len(list(posts))

        # Constructing the heading
        heading = f'{number_of_results} Result'
        if number_of_results != 1:
            heading += 's'
        heading += f' for "{search_input}"'

        # Adding the extra details to the context
        context = get_post_list_context(request, posts)
        context['heading'] = heading
        context['selected_tab'] = 'Search'
        context['search_result'] = search_input
        # Converting the form inputs into a url to insert into pagination
        search_formatted = urllib.parse.quote_plus(search_input)
        search_url = f'?search_query={search_formatted}'
        context['search_url'] = search_url

        return render(
            request,
            'post_list.html',
            context,
        )


class SearchTag(View):

    def get(self, request, tag_query):
        tag_list = tag_query.split('+')
        search_result = ''

        if tag_list:
            query = Q(tags__icontains=tag_list[0])
            for tag in range(1, len(tag_list)):
                query = query | Q(tags__icontains=tag_list[tag])
            posts = Post.objects.filter(query)
            number_of_results = len(list(posts))

            # Constructing the heading
            heading = f'{number_of_results} Post'
            if number_of_results != 1:
                heading += 's'
            heading += ' tagged with '
            for i in range(len(tag_list)):
                heading += f'"{tag_list[i]}"'
                search_result += f'#{tag_list[i]}'
                if i < len(tag_list) - 1:
                    heading += ', '
                    search_result += ' '

            # Adding the extra details to the context
            context = get_post_list_context(request, posts)
            context['heading'] = heading
            context['selected_tab'] = 'Tags'
            context['search_result'] = search_result

            return render(
                request,
                'post_list.html',
                context,
            )


class CategorisedPosts(View):
    def get(self, request, category_slug):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('/accounts/login')

        category = get_object_or_404(Category, slug=category_slug)
        posts = Post.objects.filter(category=category)

        context = get_post_list_context(request, posts)
        if category.slug == 'none':
            context['heading'] = f'Posts with {category.name}'
        else:
            context['heading'] = f'Posts in Category "{category.name}"'
        context['selected_tab'] = f'Category/{category.name}'

        return render(
            request,
            'post_list.html',
            context,
        )


class BrowseCategories(View):

    def get(self, request):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('/accounts/login')

        categories = Category.objects \
                             .annotate(num_posts=Count('tagged_posts')) \
                             .filter(num_posts__gt=0) \
                             .order_by('-num_posts')

        context = get_category_list_context(request, categories)
        context['selected_tab'] = 'Browse Categories'

        return render(
            request,
            'category_list.html',
            context,
        )


class MyPosts(View):
    def get(self, request):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('/accounts/login')

        posts = Post.objects.filter(posted_by=request.user)

        context = get_post_list_context(request, posts)
        context['heading'] = f'Your Posts'
        context['selected_tab'] = 'My Posts'

        return render(
            request,
            'post_list.html',
            context,
        )


class AddPost(View):

    def get(self, request):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        context = get_post_form_context(request)
        return render(
            request,
            'new_post.html',
            context,
        )

    def post(self, request):
        title = request.POST.get('title')
        category = request.POST.get('category')
        content = request.POST.get('body')
        tags = request.POST.get('tags')
        category_object = get_object_or_404(Category, name=category)

        # Uploading the image to Cloudinary if one was given
        image_url = None
        image_position = None
        if request.FILES:
            image = request.FILES['post-image']
            image_url = cloudinary.uploader.upload(image)['public_id']
        image_position = request.POST.get('image-position')

        # Generating the slug for the post
        site_data = get_object_or_404(SiteData)
        total_posts = site_data.total_posts_created
        post_slug = generate_slug(title, category, total_posts)
        total_posts += 1
        site_data.total_posts_created = total_posts
        site_data.save()

        post = Post.objects.create(
            title=title,
            slug=post_slug,
            content=content,
            image=image_url,
            image_position=image_position,
            category=category_object,
            tags=tags,
            posted_by=request.user
        )

        # Adding a poll if one is found
        if request.POST.get('has-poll'):
            create_poll(request, post)
        display_success(request, 'Your post was created successfully!')
        return HttpResponseRedirect(reverse('view_post', args=[post_slug]))


class EditPost(View):

    def get(self, request, post_id):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        post = get_object_or_404(Post, id=post_id)

        # Preventing users that do not own the post from being able to edit it
        if post.posted_by != request.user:
            deny_access(request)
            return HttpResponseRedirect(reverse('view_post', args=[post.slug]))

        context = get_post_form_context(request)
        context['post'] = post
        return render(request, 'edit_post.html', context)

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        # Prevents the text from deleting if the user doesn't click the editor
        content = request.POST.get('body')
        if content == '':
            content = request.POST.get('content-backup')
        category = request.POST.get('category')

        post.title = request.POST.get('title')
        post.content = content
        post.edited = True
        post.category = get_object_or_404(Category, name=category)
        post.tags = request.POST.get('tags')

        # Updating the image if a new one has been selected
        if request.FILES:
            image = request.FILES['post-image']
            image_url = cloudinary.uploader.upload(image)['public_id']
            delete_image(post)
            post.image = image_url
        post.image_position = request.POST.get('image-position')

        # Adding a poll if one is found
        if request.POST.get('has-poll'):
            create_poll(request, post)
        post.save()
        display_success(request, 'Your post has been updated!')
        return HttpResponseRedirect(reverse('view_post', args=[post.slug]))


class ViewPost(View):

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        context = get_post_context(request, post)
        return render(request, 'post_details.html', context)


class LikePost(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('view_post', args=[slug]))


class DeletePost(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        delete_image(post)
        post.delete()
        display_success(request, 'Your post has been deleted')
        return redirect('home')


class ClearImage(View):

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        delete_image(post)
        post.save()
        display_success(request, 'The image has been deleted')
        return HttpResponseRedirect(reverse('edit_post', args=[post_id]))



class SendComment(View):

    def post(self, request, slug):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        post = get_object_or_404(Post, slug=slug)
        comment_text = request.POST.get('content')
        reply_id = request.POST.get('reply')
        reply_to = None

        if reply_id is not None:
            reply_to = get_object_or_404(Comment, id=int(reply_id))

        Comment.objects.create(
            post=post,
            content=comment_text,
            posted_by=request.user,
            reply_to=reply_to
        )
        display_success(request, 'Your comment was sent successfully!')
        return HttpResponseRedirect(reverse('view_post', args=[slug]))


class LikeComment(View):

    def post(self, request, comment_id):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        comment = get_object_or_404(Comment, id=comment_id)

        if comment.likes.filter(id=request.user.id).exists():
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)
        slug = comment.post.slug
        return HttpResponseRedirect(reverse('view_post', args=[slug]))


class EditComment(View):

    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        updated_body = request.POST.get('content')

        comment.content = updated_body
        comment.edited = True
        comment.save()
        slug = comment.post.slug
        display_success(request, 'Your comment has been updated!')
        return HttpResponseRedirect(reverse('view_post', args=[slug]))


class DeleteComment(View):

    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        slug = comment.post.slug
        comment.delete()
        display_success(request, 'Your comment has been deleted!')
        return HttpResponseRedirect(reverse('view_post', args=[slug]))


class AddPoll(View):

    def get(self, request):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        context = get_base_context(request)
        return render(
            request,
            'new_poll.html',
            context,
        )

    def post(self, request):
        create_poll(request)
        display_success(request, 'Your poll was created successfully!')
        return HttpResponseRedirect(reverse('browse_polls', args=['owned']))


class VotePoll(View):

    def post(self, request, poll_id, current_dir):
        vote_answer = int(request.POST.get('poll-vote'))
        poll = get_object_or_404(Poll, id=poll_id)
        poll_answers = list(poll.answers.all())

        for answer in poll_answers:
            if answer.position == vote_answer:
                answer.votes.add(request.user)
                answer.save()
                display_success(request, 'Your vote has been sent!')
                return redirect(current_dir)


class BrowsePolls(View):

    def get(self, request, poll_type):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        poll_type = poll_type.capitalize()
        polls = None
        if poll_type == 'Open':
            polls = Poll.objects.filter(due_date__gt=datetime.now()) \
                        .order_by('due_date')
        elif poll_type == 'Closed':
            polls = Poll.objects.exclude(due_date__gt=datetime.now())
        else:
            polls = Poll.objects.filter(asked_by=request.user)
            poll_type = 'Your'

        context = get_poll_list_context(request, polls)
        context['heading'] = f"{poll_type} Polls"
        context['selected_tab'] = f'Polls/{poll_type}'

        return render(
            request,
            'poll_list.html',
            context,
        )


class DeletePoll(View):

    def post(self, request, poll_id, current_dir):
        poll = get_object_or_404(Poll, id=poll_id)
        poll.delete()
        display_success(request, 'Your poll has been deleted')
        return redirect(current_dir)


class AccountSettings(View):

    def get(self, request):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('/accounts/login')

        context = get_base_context(request)
        return render(
            request,
            'account_settings.html',
            context
        )
    
    def post(self, request):

        password = request.POST.get('password')
        user = authenticate(request, username=request.user.username,
                            password=password)
        if user is not None:
            return redirect('edit_account')
        else:
            display_error(request,
                          'The password you have entered is incorrect.')
            return redirect('account_settings')


class EditAccount(View):

    def get(self, request):
        # Redirects the user to the login page if not logged in
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        context = get_base_context(request)
        context['user_form'] = UpdateUserForm(instance=request.user)
        context['password_form'] = SetPasswordForm(request.user)
        return render(
            request,
            'edit_account.html',
            context
        )
    
    def post(self, request):
        form_valid = False
        user_form = UpdateUserForm(request.POST, instance=request.user)
        password_form = None
        password_change = request.POST.get('change-password')
        if user_form.is_valid():
            if password_change:
                password_form = SetPasswordForm(request.user, request.POST)
                if password_form.is_valid():
                    form_valid = True
                    user = password_form.save()
                    update_session_auth_hash(request, user)
            else:
                form_valid = True
        if form_valid:
            user_form.save()
            display_success(request, 'Your details have been updated!')
            return redirect('account_settings')
        else:
            display_form_errors(request, user_form)
            if password_change:
                display_form_errors(request, password_form)
            
            context = get_base_context(request)
            context['user_form'] = user_form
            context['password_form'] = password_form
            return render(
                request,
                'edit_account.html',
                context
            )


class DeleteAccount(View):

    def post(self, request):
        password = request.POST.get('password')
        user = authenticate(request, username=request.user.username,
                            password=password)
        if user is not None:
            user = get_object_or_404(User, id=request.user.id)

            # Removing all images uploaded by the user from cloudinary
            posts = list(user.added_posts.all())
            for post in posts:
                delete_image(post)

            user.delete()
            display_success(request, 'Your account has been deleted')
            return redirect('/accounts/login')
        else:
            return redirect('account_settings')


class Error404(View):

    def get(self, request, *args, **kwargs):
        context = get_base_context(request)
        error_page = render(request, '404.html', context)
        return HttpResponseNotFound(error_page.content)
