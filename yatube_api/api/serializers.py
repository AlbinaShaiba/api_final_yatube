from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post, Group, Follow, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')


class  FollowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    following = serializers.StringRelatedField()

    class Meta:
        fields = ['user', 'following', ]
        model = Follow


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('post', )
        model = Comment
