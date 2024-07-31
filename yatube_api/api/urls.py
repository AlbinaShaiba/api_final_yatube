from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import PostViewSet, GroupViewList, FollowViewList, CommentViewList


app_name = 'api'

router_v1 = SimpleRouter()

router_v1.register(r'posts', PostViewSet)
router_v1.register(r'groups', GroupViewList)
router_v1.register(r'follow', FollowViewList, basename='follow')
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewList, basename='comment')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
]
