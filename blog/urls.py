import blog.views
from django.urls import path

urlpatterns = [
    path('', blog.views.index),
    path('post/<slug>/', blog.views.post_detail, name='blog_post_detail'),
        ]
