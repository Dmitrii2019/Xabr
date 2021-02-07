import blogapp.views as blogapp
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views
from django.urls import path


from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, DraftListView

app_name = 'blog'

urlpatterns = [
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/', BlogListView.as_view(), name='post_list'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post_draft/', DraftListView.as_view(), name='post_draft'),

]
