import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post
from blog.forms import CommentForm

# for cache
# from django.views.decorators.cache import cache_page
# for changing the cache when the headers change (e.g. user)
# from django.views.decorators.vary import vary_on_cookie

logger = logging.getLogger(__name__)

# Create your views here.
# @cache_page(300) # this cache depends on the URL and not the user! careful! (@cache_page
# @vary_on_cookie # changes the cache if the cookie was changed
def index(request):
  posts = Post.objects.filter(published_at__lte=timezone.now())
  logger.debug("Got %d posts", len(posts))
  return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, slug):
  post = get_object_or_404(Post, slug=slug)

  if request.user.is_active:
    if request.method == 'POST':
      comment_form = CommentForm(request.POST)

      if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.content_object = post
        comment.creator = request.user
        comment.save()
        logger.info(
          "Created comment on Post %d for user %s", post.pk, request.user
          )
        return redirect(request.path_info)
    else:
      comment_form = CommentForm()
  else:
    comment_form = None
  return render(request, 'blog/post_detail.html', {'post':post, 'comment_form': comment_form})