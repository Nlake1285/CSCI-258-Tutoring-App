# pages/urls.py
from django.urls import path

from .views import (HomePageView, TutorCreateView, TutorDeleteView,
                    TutorDetailView, TutorListView, TutorUpdateView)

urlpatterns = [
    path("", TutorListView.as_view(), name="home"),
    path("post/new/", TutorCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", TutorDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", TutorUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", TutorDeleteView.as_view(), name="post_delete"),
]