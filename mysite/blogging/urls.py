from django.urls import path
from blogging.views import stub_view,list_view,detail_view

urlpatterns = [
    path('', PollListView.as_view(), name="blog_index"),
    path("posts/<int:post_id>/", PollDetailView.as_view(), name="blog_detail")
]
