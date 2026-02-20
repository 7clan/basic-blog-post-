from django.urls import path
from . import views

urlpatterns = [
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('', views.PostListView.as_view(), name='posts'),
   # URL to list all tags
path('tags/', views.get_all_tags, name='all_tags'),

# URL to show a specific tag detail by slug
path('tags/<slug:slug>/', views.tag_detail, name='tag_detail'),

# URL to post a comment
path('post/<slug:slug>/comment/', views.post_comment, name='post_comment'),
path('post/<slug:slug>/read_later/', views.ReadLaterView.as_view(), name='read_later'),
# urls.py
# URL to show the "Read Later" page listing all saved posts
path('read-later/', views.ReadLaterView.as_view(), name='read_later_list')




   

    ]