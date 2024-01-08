from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import PostForm
from .models import Post
from django.urls import reverse_lazy

class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = PostForm
    model = Post
    success_url = reverse_lazy('posts:post-list')
    success_message = "A postagem foi criada com sucesso."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 10

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

class PostUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = PostForm
    model = Post
    success_url = reverse_lazy('posts:post-list')
    success_message = "A postagem foi atualizada com sucesso."

class PostDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts:post-list')
    success_message = "A postagem foi excluída com sucesso."
