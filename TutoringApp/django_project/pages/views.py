from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Post


class HomePageView(TemplateView):
    template_name = "home.html"


class TutorListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"


class TutorDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class TutorCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "body", "author"]


class TutorUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]


class TutorDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")