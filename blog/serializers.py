from rest_framework import serializers
from blog.models import CustomUser, Post

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Post
        fields = ('user', 'title', 'body', 'date')

    def create(self, validated_data):
        """
        Create and return a new Post instance, given the validated data.
        """
        return Post.objects.create(**validated_data)


class CustomUserSerializer(serializers.ModelSerializer):
    # posts = serializers.PrimaryKeyRelatedField(many=True,
    #                                            queryset=Post.objects.all())

    posts = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'posts')
