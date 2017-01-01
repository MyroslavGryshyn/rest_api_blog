from django.http import Http404

from rest_framework import status
from rest_framework import mixins
from rest_framework import filters
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from blog.models import Post
from blog.serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List all user posts, or create a new post.
    """

    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'body')

    def get_queryset(self):
        """
        Filtering queryset by user.
        """
        user = self.request.user
        return Post.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AllPostList(generics.ListAPIView):
    """
    List all posts with offset.
    """

    queryset = Post.objects.filter()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'body')
