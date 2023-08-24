from django.urls import path
from blogging.views import stub_view, BlogListView, BlogDetailView, add_post

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_index"),
    path("add_post/", add_post, name="add_post"),
    path("add/", add_post, name="add_post"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail")
]
