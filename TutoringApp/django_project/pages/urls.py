# pages/urls.py
from django.urls import path

from .views import (PostCreateView, PostDeleteView, PostDetailView,
                    PostUpdateView, TutorDetailView, TutoringHourCreateView,
                    TutoringHourDeleteView, TutorListView)

urlpatterns = [
    path("", TutorListView.as_view(), name="home"),
    path("post/new/", PostCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("tutor/<int:pk>/", TutorDetailView.as_view(), name="tutor_detail"),
    path("hours/new/", TutoringHourCreateView.as_view(), name="hours_new"),
    path("hours/<int:pk>/delete/", TutoringHourDeleteView.as_view(), name="hours_delete"),
]