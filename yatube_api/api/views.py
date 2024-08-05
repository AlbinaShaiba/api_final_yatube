from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

from rest_framework import filters

from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import permissions

from api.serializers import PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer
from api.permissions import OwnerOrReadOnly
from posts.models import Post, Group, Comment, Follow, User


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = LimitOffsetPagination
    permission_classes = [OwnerOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewList(viewsets.ReadOnlyModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

class CommentViewList(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [OwnerOrReadOnly, ]

    def get_comment_post(self):
        return get_object_or_404(Post, id=self.kwargs['post_id'])

    def get_queryset(self):
        return self.get_comment_post().comments.all()
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user,
                        post=self.get_comment_post())


class FollowViewList(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter, )
    permission_classes = [permissions.IsAuthenticated, ]
    search_fields = ('following__username',)

    def get_user(self):
        return get_object_or_404(User, id=self.request.user.id)

    def get_queryset(self):
        return self.get_user().following.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

