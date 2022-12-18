from django.conf.urls import include
from django.urls import path
from accounts import views

from .views import (
    PostListView,
    DraftPostListView,
    PublishedPostListView,
    ArchivedPostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('',PostListView.as_view(), name='list'),
    path('<drafts/', DraftPostListView.as_view(), name='draft_list'),
    path('published/', PublishedPostListView.as_view(), name='published_list'),
    path('archived/', ArchivedPostListView.as_view(), name='archived_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('new/', PostCreateView.as_view(), name="new"),
    path('<int:edit>/edit/', PostUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    
    
]
