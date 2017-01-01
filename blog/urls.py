"""rest_api_blog URL Configuration
"""

from django.conf.urls import url
from blog.views import PostList, AllPostList

urlpatterns = [
    url(r'^posts/$', PostList.as_view(), name='posts'),
    url(r'^posts/all/$', AllPostList.as_view(), name='all_posts'),
]
