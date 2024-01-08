from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from posts.models import Post
from posts.forms import PostForm
from django.urls import reverse_lazy

class HomeView(ListView):
    template_name = 'core/home.html'
    model = Post
    context_object_name = 'posts'

class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    success_url = reverse_lazy('posts:post-detail')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
