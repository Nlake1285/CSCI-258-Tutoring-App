from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Post, TutoringHour
from .forms import TutoringHourForm

User = get_user_model()


class HomePageView(TemplateView):
    template_name = "home.html"


class TutorListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add tutoring hours to the context
        context['tutoring_hours'] = TutoringHour.objects.filter(is_active=True).select_related('tutor')
        context['tutors'] = User.objects.filter(is_tutor=True)
        return context


class TutorDetailView(DetailView):
    model = User
    template_name = "tutor_detail.html"
    context_object_name = "tutor"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tutoring_hours'] = TutoringHour.objects.filter(
            tutor=self.object, is_active=True
        ).order_by('day_of_week', 'start_time')
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "body"]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")


class TutoringHourCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = TutoringHour
    template_name = "tutoring_hour_new.html"
    form_class = TutoringHourForm
    
    def test_func(self):
        return self.request.user.is_tutor
    
    def form_valid(self, form):
        form.instance.tutor = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("tutor_detail", kwargs={"pk": self.request.user.pk})


class TutoringHourDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TutoringHour
    template_name = "tutoring_hour_delete.html"
    
    def test_func(self):
        tutoring_hour = self.get_object()
        return self.request.user == tutoring_hour.tutor or self.request.user.is_superuser
    
    def get_success_url(self):
        return reverse_lazy("tutor_detail", kwargs={"pk": self.request.user.pk})