from django.urls import path
from django.contrib import admin
from comments.views import CommentCreateView
from posts.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet)


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('admin/', admin.site.urls),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='add_comment'),
]

urlpatterns += router.urls